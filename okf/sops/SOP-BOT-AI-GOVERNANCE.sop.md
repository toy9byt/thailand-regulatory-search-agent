---
sop_id: "SOP-BOT-AI-GOVERNANCE"
title: "Standard Operating Procedure: Financial Services AI/ML Governance & Ethical AI"
version: "1.0.0"
domain: AI_ETHICS_AND_MODEL_RISK
regulator: "Bank of Thailand (BOT) & ETDA AIGC"
statutory_anchor: "BOT AI/ML Financial Sector Principles & ETDA AI Governance Guidelines for Executives"
severity: "HIGH"
tags:
  - ai-governance
  - explainability
  - model-risk-management
  - anti-bias-lending
---

# Scope & Objective
Governs the lifecycle of Artificial Intelligence and Machine Learning models deployed by Thai commercial banks, covering automated retail credit underwriting, alternative data scoring, and Generative AI customer interactions.

## Step 1: Algorithmic Explainability & Transparency (Non-Black Box)
- Machine Learning models determining credit approval, pricing, or risk tiers must implement verifiable feature attribution (SHAP values or Integrated Gradients).
- Adverse Action Notices must provide the applicant with the top 3 dominant factors that led to credit rejection.

## Step 2: Algorithmic Fairness & Anti-Bias Audit
- Perform demographic parity and disparate impact audits across training datasets.
- Ensure protected attributes (gender, age, religion, geographic origin) or their proxies are strictly excluded from credit scoring weights.

## Step 3: Model Risk Management (MRM) & Concept Drift Monitoring
- Independent Model Validation (IMV) team must audit model architecture and backtest against downturn scenarios before production release.
- Real-time monitoring of Population Stability Index (PSI). Any drift with PSI > 0.25 mandates automatic model pause and human retraining.

## Step 4: Automated Decision-Making (ADM) Contestability (PDPA Section 30)
- Bank must provide a mechanism for customers to contest an automated AI rejection and demand human underwriter review within 30 days.

## Audit Evidence Checklist
1. Independent Model Validation (IMV) approval charter.
2. Disparate impact statistical audit report signed by CRO.
3. Model drift monitoring dashboard logs with automated alert history.
4. Documented workflow for processing PDPA Section 30 human review requests.
