---
sop_id: "SOP-OIC-BANCASSURANCE-E-CONSENT"
title: "Standard Operating Procedure: Digital Bancassurance Electronic Sales & Consent"
version: "1.0.0"
domain: INSURANCE_DISTRIBUTION_GOVERNANCE
regulator: "Office of Insurance Commission (OIC / คปภ.)"
statutory_anchor: "ประกาศ คปภ. เรื่อง การบริหารจัดการความเสี่ยงด้านเทคโนโลยีสารสนเทศ พ.ศ. 2563 ข้อ 6"
severity: "HIGH"
tags:
  - oic-bancassurance
  - electronic-consent
  - tablet-sales
  - insurtech
---

# Scope & Objective
Applies to commercial banks and licensed bancassurance agents selling life and non-life insurance products through mobile tablets or digital branch kiosks.

## Step 1: Digital Identity Verification & e-KYC
- Verify customer identity via DIP-CHIP Smart Card reader or NDID (National Digital ID) with liveness biometric detection.
- Prohibit branch staff from signing or entering OTPs on behalf of the customer.

## Step 2: Unbundled Electronic Consent Capture
- Insurance application UI must separate terms: policyholder agreement, underwriting consent, and marketing/cross-selling opt-in must be independent checkboxes.
- Pre-ticked checkboxes are strictly prohibited under both OIC and PDPA regulations.

## Step 3: Cryptographic Timestamping & Digital Policy Issuance
- Electronic proposal documents and signatures must be timestamped with an ETDA-accredited Certificate Authority (CA).
- Automated generation of tamper-evident PDF/A policy documents delivered to customer verified email within 24 hours.

## Audit Evidence Checklist
1. Electronic signature CA certificate and timestamp audit trail.
2. Bancassurance Tablet Mobile Device Management (MDM) configuration profile.
3. Sample digital policy issuance confirmation records with verified timestamp.
