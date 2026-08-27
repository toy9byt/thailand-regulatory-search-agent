---
sop_id: "SOP-BOT-122563-CLOUD-OUTSOURCING"
title: "Standard Operating Procedure: Bank of Thailand Cloud IT Risk Outsourcing & Right-to-Audit"
version: "1.0.0"
domain: BANKING_CLOUD_GOVERNANCE
regulator: "Bank of Thailand (BOT / ธปท.)"
statutory_anchor: "ประกาศ สนส. 12/2563 ข้อ 5.2 (การจ้างบุคคลภายนอกด้านระบบงานสารสนเทศ)"
severity: "HIGH"
tags:
  - bot-122563
  - cloud-migration
  - right-to-audit
  - csp-contract-addendum
---

# Scope & Objective
This SOP defines mandatory statutory procedures for Thai Private Commercial Banks procuring material Public Cloud services (IaaS, PaaS, SaaS) under Bank of Thailand Notification SorNorSor. 12/2563.

## Step 1: Pre-Procurement Ingress Sanitization
- Prior to entering contract negotiations, redact customer PII, internal IP schemes, and employee personal contacts.
- Determine if the cloud workload qualifies as "Material IT Outsourcing" (Core Banking, Payment Switch, Customer Ledger).

## Step 2: Mandatory Bilateral Contract Clauses (Clause 5.2.2)
All cloud agreements must include an explicit **Right to Audit Clause**:
- **Statutory Audit Rights:** The Cloud Service Provider (CSP) must grant the commercial bank, its internal/external auditors, and Bank of Thailand statutory examiners unrestricted right to inspect operations, logs, and security controls.
- **Notice Window:** Standard on-site or remote audit notification window must not exceed 30 business days.
- **Third-Party Certifications:** CSP must furnish annual SOC 2 Type II, ISO 27001, and CSA STAR audit reports.

## Step 3: Cloud Exit Strategy & Business Continuity (Clause 5.2.3)
- Bank must formulate a documented Cloud Exit Plan allowing transition to an alternate CSP or on-premise within 90 days.
- Minimum 1 automated Disaster Recovery (DR) failover drill per year with RTO <= 4 hours and RPO <= 15 minutes.

## Audit Evidence Checklist
1. Board Risk Committee approval minutes for cloud procurement.
2. Signed Bilateral CSP Contract Addendum containing BOT Right to Audit.
3. Annual DR simulation test report signed by CISO.
