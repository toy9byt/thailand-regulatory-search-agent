---
sop_id: "SOP-PDPA-CROSS-BORDER-TRANSFER"
title: "Standard Operating Procedure: Financial Data Cross-Border Cloud Transfer (PDPA Sections 28-29)"
version: "1.0.0"
domain: FINANCIAL_DATA_PRIVACY
regulator: "Personal Data Protection Commission (PDPC / สคส.)"
statutory_anchor: "PDPA B.E. 2562 Sections 28 & 29 and PDPC Cross-Border Notifications B.E. 2566"
severity: "CRITICAL"
tags:
  - pdpa-cross-border
  - standard-contractual-clauses
  - transfer-impact-assessment
  - cmek-encryption
---

# Scope & Objective
Applies to commercial banks, securities intermediaries, and insurance firms transferring customer financial PII (KYC records, transaction logs, biometric data) to Public Cloud regions located outside the Kingdom of Thailand.

## Step 1: Destination Adequacy & Assessment (Section 28)
- Evaluate whether the target destination country or international organization has adequate personal data protection standards as announced by the PDPC.
- If destination country lacks adequacy designation, proceed via Section 29 legal transfer mechanisms.

## Step 2: Section 29 Transfer Safeguards (SCCs & BCRs)
- **Standard Contractual Clauses (SCCs):** Incorporate PDPC-approved or ASEAN/EU SCC model clauses into bilateral Cloud Service Provider (CSP) Data Processing Addendums (DPA).
- **Binding Corporate Rules (BCRs):** For intra-group cross-border replication across multinational banking affiliates, verify approved BCRs with PDPC.

## Step 3: Technical Safeguards & Encryption
- Enforce Customer-Managed Encryption Keys (CMEK) with keys stored in Thailand (Cloud KMS / HSM).
- Enforce TLS 1.3 in transit and AES-256 at rest; CSP administrators must have zero plaintext decryption access.

## Step 4: 72-Hour Data Breach Notification Protocol (Section 37(4))
- If a security incident compromises cross-border financial data, notify the PDPC without delay within 72 hours of becoming aware.

## Audit Evidence Checklist
1. Transfer Impact Assessment (TIA) documenting recipient cloud region and legal basis.
2. Executed Bilateral Data Processing Addendum (DPA) containing Standard Contractual Clauses.
3. KMS Key Management & Access Log Audit confirming zero unapproved external key access.
