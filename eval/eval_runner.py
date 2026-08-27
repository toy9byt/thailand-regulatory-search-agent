"""
Automated Evaluation Harness for Thailand Private Banking Regulatory Agent.
Executes test cases from eval_dataset.jsonl, verifies HITL gates, and measures compliance accuracy.
"""

import json
import os
import sys
import time

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agent import RegulatoryCoordinatorAgent


def run_evaluation_suite(dataset_path: str = "eval/eval_dataset.jsonl") -> dict:
    """Runs the golden evaluation suite and prints an executive summary."""
    coordinator = RegulatoryCoordinatorAgent()

    if not os.path.exists(dataset_path):
        dataset_path = os.path.join(os.path.dirname(__file__), "eval_dataset.jsonl")

    with open(dataset_path, "r", encoding="utf-8") as f:
        test_cases = [json.loads(line.strip()) for line in f if line.strip()]

    passed = 0
    failed = 0
    results = []

    print("\n================================================================================")
    print(f"RUNNING AUTOMATED EVALUATION SUITE: {len(test_cases)} TEST SCENARIOS")
    print("================================================================================\n")

    start_time = time.time()
    for tc in test_cases:
        t_start = time.time()
        res = coordinator.handle_compliance_inquiry(tc["query"], session_id=tc["test_id"])
        latency_ms = (time.time() - t_start) * 1000

        expected_outcome = tc["expected_outcome"]
        actual_outcome = res.get("status")

        is_success = False
        if expected_outcome == "SUCCESS":
            # Passes if SUCCESS or if properly intercepted by HITL gate awaiting confirmation
            if actual_outcome in ["SUCCESS", "AWAITING_HUMAN_CONFIRMATION"]:
                # If awaiting confirmation, test that confirming yields SUCCESS
                if actual_outcome == "AWAITING_HUMAN_CONFIRMATION":
                    confirmed_res = coordinator.handle_compliance_inquiry(
                        tc["query"], session_id=tc["test_id"], confirmed_by_user=True
                    )
                    if confirmed_res.get("status") == "SUCCESS":
                        is_success = True
                else:
                    is_success = True
        elif expected_outcome == "REJECTED_BY_GUARDRAIL" and actual_outcome == "REJECTED_BY_GUARDRAIL":
            is_success = True

        if is_success:
            passed += 1
            verdict = "PASSED"
        else:
            failed += 1
            verdict = "FAILED"

        results.append({
            "test_id": tc["test_id"],
            "category": tc["category"],
            "verdict": verdict,
            "latency_ms": round(latency_ms, 2),
            "actual_outcome": actual_outcome
        })
        print(f"[{verdict}] {tc['test_id']} ({tc['category']}): {tc['query'][:60]}... ({round(latency_ms, 2)}ms)")

    total_time = time.time() - start_time
    pass_rate = (passed / len(test_cases)) * 100

    print("\n--------------------------------------------------------------------------------")
    print(f"EVALUATION SUMMARY: {passed}/{len(test_cases)} PASSED ({pass_rate:.1f}%) in {total_time:.2f}s")
    print("--------------------------------------------------------------------------------\n")

    return {
        "total": len(test_cases),
        "passed": passed,
        "failed": failed,
        "pass_rate_pct": pass_rate,
        "total_duration_sec": round(total_time, 2),
        "results": results
    }


if __name__ == "__main__":
    summary = run_evaluation_suite()
    if summary["failed"] > 0:
        sys.exit(1)
    sys.exit(0)
