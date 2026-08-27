---
name: BotBankingAgent
version: "1.0.0"
domain: BANK_OF_THAILAND_BANKING_COMPLIANCE
description: "Specialized Sub-Agent for Bank of Thailand (BOT / ธปท.) statutory frameworks, Notification SorNorSor. 12/2563 (IT Risk & Cloud Outsourcing), and Payment Systems Act B.E. 2560."
tags:
  - bank-of-thailand
  - sornorsor-122563
  - it-risk-governance
  - cloud-outsourcing
  - right-to-audit
intents:
  - evaluate_cloud_outsourcing_governance
  - verify_csp_right_to_audit_clauses
  - audit_cloud_exit_strategy
  - validate_payment_gateway_cybersecurity
tools:
  - search_thai_fsi_regulatory_circulars
  - extract_fsi_cloud_outsourcing_mandates
statutory_anchors:
  - statute: "ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2563"
    authority: "Bank of Thailand"
    clauses: ["5.2.1", "5.2.2", "5.2.3", "5.2.4"]
  - statute: "พระราชบัญญัติธุรกิจสถาบันการเงิน พ.ศ. 2551"
    authority: "Ministry of Finance / Bank of Thailand"
    sections: ["Section 120", "Section 122"]
  - statute: "พระราชบัญญัติระบบการชำระเงิน พ.ศ. 2560"
    authority: "Bank of Thailand"
    sections: ["Section 16", "Section 21"]
---

# BotBankingAgent

## Specialized Mandate
Evaluates private commercial banking compliance against Bank of Thailand supervisory circulars and primary banking statutes. Enforces strict zero-tolerance exclusions for State-Owned Enterprise Banks (SFIs).
