---
sop_id: "SOP-SEC-CYBER-RESILIENCE"
title: "Standard Operating Procedure: Securities & Algorithmic Trading Cloud Cyber Resilience"
version: "1.0.0"
domain: CAPITAL_MARKETS_CYBER_SECURITY
regulator: "Securities and Exchange Commission (SEC / ก.ล.ต.)"
statutory_anchor: "SEC Cyber Resilience Guidelines & Notification KorThor. 19/2561"
severity: "HIGH"
tags:
  - sec-cyber-resilience
  - algorithmic-trading
  - digital-asset-custody
  - cold-storage
---

# Scope & Objective
Applies to securities firms, broker-dealers, asset managers, and digital asset business operators hosting trading algorithms, client order routing, or digital asset custody in Cloud environments.

## Step 1: Algorithmic Trading Systems Cloud Resilience
- Cloud hosting for high-frequency or algorithmic trading engines must guarantee sub-millisecond network predictability and 99.99% system availability.
- Automated circuit breakers and kill-switch controls must be implemented to halt runaway algorithms within <100ms.

## Step 2: Digital Asset Custody & Cold Storage Segregation (Decree B.E. 2561 Sec 30)
- Maintain minimum 90% of client digital assets in cold storage wallets physically air-gapped from the public internet.
- Multi-Signature (Multi-Sig) or Multi-Party Computation (MPC) quorum thresholds (minimum 3 of 5 authorized key holders) for hot wallet transfers.

## Step 3: Penetration Testing & Annual Resiliency Drills
- Annual third-party penetration testing and vulnerability assessments by certified ethical hackers.
- Semi-annual simulated market volatility and cyber disaster recovery drills.

## Audit Evidence Checklist
1. Algorithmic Kill-Switch architecture specification and test execution logs.
2. Cold Storage wallet audit report and physical custody verification records.
3. Annual SEC Cyber Resilience Self-Assessment Submission.
