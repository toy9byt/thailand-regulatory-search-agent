---
sop_id: "SOP-NCSA-DATA-CENTER-CII"
title: "Standard Operating Procedure: Critical Information Infrastructure (CII) Data Center Cybersecurity & Incident Escalation"
version: "1.0.0"
domain: DATA_CENTER_CYBERSECURITY_GOVERNANCE
regulator: "National Cyber Security Agency (NCSA / สกมช.)"
statutory_anchor: "Cybersecurity Act B.E. 2562 Sections 49, 50, 53 & 73"
severity: "CRITICAL"
tags:
  - ncsa-cybersecurity
  - data-center
  - cii-standards
  - 24h-escalation
  - t-b-cert
---

# Scope & Objective
Applies to On-Premise, Colocation, and Cloud Data Centers supporting regulated banking, payment, and securities systems designated as Critical Information Infrastructure (CII) under the Thailand Cybersecurity Act B.E. 2562.

## Step 1: Data Center Physical & Technical Baseline Controls (Section 50)
- Enforce biometric physical access control with visitor logs retained >= 90 days.
- Maintain dual-feed electrical redundancy (UPS + backup diesel generators with >= 48 hours continuous fuel storage).
- Maintain multi-zone environmental sensors (temperature, humidity, early water leak detection, FM-200 / Novec clean agent fire suppression).

## Step 2: Critical Cyber Threat 24-Hour Mandatory Escalation (Section 53 & 73)
- Upon detection of a Critical or Serious Cyber Threat (Ransomware, Core Network Outage, DDoS, or unauthorized root access to Data Center hypervisors):
  1. Notify NCSA Incident Response Team (ncsa-incident@ncsa.or.th / hotline) **within 24 hours**.
  2. Notify Sectoral CERT: Thailand Banking Sector CERT (T-B CERT) in parallel.
  3. Dispatch initial containment report detailing compromised IP ranges and mitigation actions.

## Step 3: Annual Independent Third-Party Cyber Audit (Section 50(2))
- Commission an independent third-party audit conducted by certified practitioners (CISA, CISSP, ISO Lead Auditor).
- Submit the completed audit report to NCSA within 30 days of completion.

## Audit Evidence Checklist
1. Official NCSA CII Registration Certificate.
2. Data Center Tier III / Tier IV Certification or equivalent SLA agreement.
3. Incident Response Playbook specifying statutory 24-hour NCSA/T-B CERT escalation.
4. Annual Independent Cybersecurity Audit Report with NCSA submission acknowledgment.
