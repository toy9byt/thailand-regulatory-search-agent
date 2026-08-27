# Thailand FSI Regulatory Search & Compliance Agent

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Architecture-Google_ADK_Multi--Agent-green)](https://github.com/google/adk-python)

An enterprise-grade, autonomous multi-agent regulatory intelligence and compliance orchestration system engineered specifically for the **Financial Services Industry (FSI) in Thailand**.

The agent automates statutory discovery, cross-regulator mandate extraction, and enterprise GRC control formulation across the four primary Thai financial authorities:
1. **Bank of Thailand (ธปท. / BOT):** Notification SorNorSor. 12/2563 (IT Risk & Cloud Outsourcing), Payment Systems Act B.E. 2560, and Financial Institutions Businesses Act B.E. 2551.
2. **Securities and Exchange Commission (ก.ล.ต. / SEC):** Cyber Resilience Guidelines, Cloud Algorithmic Trading Systems, and Digital Asset Emergency Decree B.E. 2561.
3. **Office of Insurance Commission (คปภ. / OIC):** Insurance IT Governance Notification B.E. 2563, Digital Policy Issuance, and Bancassurance electronic sales consent standards.
4. **Personal Data Protection Commission (สคส. / PDPC):** Personal Data Protection Act (PDPA B.E. 2562) Section 28-29 Cross-Border Cloud Transfers, 72-Hour Data Breach Notifications, and DPO mandates.
5. **AI Governance & Ethical AI (ธปท. / ETDA AIGC / สคส.):** Bank of Thailand AI/ML Principles (Explainability, Anti-Bias in Credit Scoring, Model Risk Management), ETDA Thailand AI Governance Clinic (AIGC) Guidelines, and PDPA Automated Decision-Making (ADM) safeguards.
6. **National Cyber Security Agency (สกมช. / NCSA):** Cybersecurity Act B.E. 2562 (Sections 49, 50, 53 & 73) on Critical Information Infrastructure (CII) Data Center baseline standards, 24-hour mandatory cyber threat incident escalation (NCSA & T-B CERT), and annual independent cybersecurity audits.

> [!IMPORTANT]
> **Scope Restriction — Thai Private Commercial Banks Only (Not SFIs):**
> Within the banking sector, this agent is strictly limited to **Thai Private Commercial Banks** and their consolidated financial business groups governed under the *Financial Institutions Businesses Act B.E. 2551*.
> 
> **It explicitly excludes and rejects:**
> - **State-Owned Enterprise Banks / Specialized Financial Institutions (SFIs):** Government Savings Bank (ธนาคารออมสิน), Bank for Agriculture and Agricultural Cooperatives (BAAC / ธ.ก.ส.), Government Housing Bank (GH Bank / ธอส.), SME D Bank, EXIM Thailand, and Islamic Bank of Thailand.
> - **Public Sector Procurement & e-Bidding:** *Government Procurement and Supplies Management Act B.E. 2560* (พ.ร.บ. การจัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ พ.ศ. 2560) and Comptroller General's Department directives.
> - **State Supervisory Authorities:** State Enterprise Policy Office (SEPO / สคร.) and State Audit Office (SAO / สตง.) directives.
> 
> *Queries regarding public procurement or SFIs are automatically intercepted and rejected by the Pre-Execution Input Guardrail.*

---

## 1. System Architecture

<p align="center">
  <img src="docs/images/system_architecture.png" alt="Thailand FSI Regulatory Search & Compliance Agent End-to-End Architecture" width="100%" />
</p>

<details>
<summary><b>🔍 View Mermaid.js Text Definition</b></summary>

```mermaid
flowchart TD
    subgraph L1["1. Ingress & Security Guardrails Layer"]
        User["FSI Compliance Officer / Cloud Architect"]
        PII["PII Redaction Scrubber (Thai ID, Accounts, Cards)"]
        IG["Input Guardrail (Prompt Injection & SFI Rejection)"]
        User --> PII --> IG
    end

    subgraph L2["2. Orchestration & Strategic Routing Layer"]
        Router["Tiered Thinking Model Router"]
        Coord["RegulatoryCoordinatorAgent (Root Dispatcher)"]
        IG --> Router --> Coord

        Flash["Gemini 3.7 Flash Fast Mode (thinking_budget: 0)"]
        Pro["Gemini 3.7 Flash Deep Think (thinking_budget: 4096) / Pro Fallback"]
        Router -.-> Flash
        Router -.-> Pro

        subgraph SubAgents["Specialized Domain Sub-Agents"]
            BotAgent["BotBankingAgent (BOT SorNorSor. 12/2563, Payments)"]
            SecAgent["SecMarketAgent (SEC Cyber Resilience, Trading)"]
            OicAgent["OicInsuranceAgent (OIC IT Governance, Bancassurance)"]
            PdpaAgent["PdpaComplianceAgent (PDPA Cross-Border PII, DPO)"]
            GrcAgent["GrcSynthesizerAgent (CO-REG-TH Matrix & Redlines)"]
        end

        Coord --> BotAgent
        Coord --> SecAgent
        Coord --> OicAgent
        Coord --> PdpaAgent
        BotAgent & SecAgent & OicAgent & PdpaAgent --> GrcAgent
    end

    subgraph L3["3. Pydantic v2 Tools & Statutory Grounding"]
        Tools["Domain Tools with Guided Error Recovery"]
        BotAgent & SecAgent & OicAgent & PdpaAgent --> Tools
        Repo[("Thai FSI Statutory Knowledge Store")]
        SFIFilter{"SFI / State Bank Filter"}
        Tools --> SFIFilter
        SFIFilter -- "Private FSI Mandate" --> Repo
        SFIFilter -- "SFI / Gov Rule" --> Drop["Excluded Item Audit (EXCLUDED)"]
    end

    subgraph L4["4. Context, Memory & Session Layer"]
        Const["System Constitution (Legal Hierarchy & Non-PR Rule)"]
        SessionStore[("Persistent Session Store (SQLite / Cloud SQL)")]
        Compactor["Sliding Window History Compactor"]
        AsyncMem["Async Memory Worker (Knowledge Indexing)"]

        Coord <--> Const
        Coord <--> SessionStore
        SessionStore --> Compactor
        Coord -. "asyncio.create_task" .-> AsyncMem
    end

    subgraph L5["5. Observability, Tracing & HITL Safety"]
        OTel["OpenTelemetry Distributed Tracing (W3C traceparent)"]
        JSONLog["Structured JSON Logger (INTENT_EMITTED => OUTCOME_RECORDED)"]
        HITL{"Human-in-the-Loop Hook (Sev-1 Breach / Policy Override)"}
        OG["Output Guardrail (100% Grounding Verifier & PII Scrubber)"]

        Coord --> OTel
        Tools --> JSONLog
        GrcAgent --> HITL
        HITL -- "Approved" --> OG
        HITL -- "High Stakes" --> Confirm["Await Human Officer Confirmation"]
        OG --> Output["Actionable Enterprise GRC Report & Redlines"]
    end
```
</details>

---

## 2. Key FSI Use Cases & Regulatory Coverage

| FSI Sector | Regulatory Authority | Primary Statutes & Standards | In-Scope Workloads & Use Cases |
| :--- | :--- | :--- | :--- |
| **Private Commercial Banking** | **Bank of Thailand (BOT / ธปท.)** | • Notification SorNorSor. 12/2563<br>• Financial Institutions Businesses Act B.E. 2551<br>• Payment Systems Act B.E. 2560 | Core banking cloud migrations, right-to-audit clauses, CSP exit strategies, multi-cloud resiliency, sub-contracting governance. |
| **Capital Markets & Securities** | **Securities and Exchange Commission (SEC / ก.ล.ต.)** | • Cyber Resilience Guidelines<br>• Notification KorThor. 19/2561<br>• Digital Asset Business Decree B.E. 2561 | Algorithmic trading hosting, wealth management microservices, digital asset custody (cold storage segregation). |
| **Insurance & InsurTech** | **Office of Insurance Commission (OIC / คปภ.)** | • IT Governance Notification B.E. 2563<br>• Digital Bancassurance Sales Guidelines | Electronic policy issuance consent, tablet-based branch sales compliance, digital customer verification. |
| **Financial Data Privacy** | **Personal Data Protection Commission (PDPC / สคส.)** | • Personal Data Protection Act (PDPA B.E. 2562)<br>• Subordinate Notifications on Sec 28–29 | Cross-border financial cloud data transfers, adequate protection assessments, 72-hour breach escalation protocols. |
| **AI Governance & Ethical AI** | **Bank of Thailand (BOT), ETDA & PDPC** | • BOT Guidelines on AI/ML in Financial Services<br>• ETDA AI Governance Guidelines for Executives (AIGC)<br>• PDPA Sec 30 (Automated Decision-Making) | Algorithmic credit underwriting explainability (SHAP/feature attribution), anti-bias testing in alternative data scoring, model risk management (MRM) drift controls, consumer AI disclosure, and right-to-human-review objection workflows. |
| **CII & Data Centers** | **National Cyber Security Agency (NCSA / สกมช.)** | • Cybersecurity Act B.E. 2562 (Sec 49, 50, 53, 73)<br>• NCSA Notification on CII Baseline Standards B.E. 2564 | Data Center physical and environmental resilience (dual-power, biometric access, CCTV >= 90 days), mandatory 24-hour incident notification to NCSA and T-B CERT, and annual third-party independent cybersecurity audit submission. |

---

---

---

## 3. Critical User Journeys (CUJs)

### 🔹 CUJ 1: Core Banking Cloud Migration & Right-to-Audit Contract Addendum
* **Primary Persona:** Lead Cloud Architect & Head of IT Risk Compliance
* **Business Trigger:** The bank is migrating its core payment gateway and transaction ledgers to Public Cloud (Google Cloud / AWS). The CSP's standard master services agreement (MSA) does not explicitly grant statutory inspection rights to regulatory examiners.
* **Agentic Multi-Agent Execution Flow:**
  1. **Ingress Sanitization:** The compliance officer submits the proposed cloud architecture and CSP contract clause. The **Dual-Boundary PII Scrubber** immediately sanitizes internal server hostnames and internal administrator emails.
  2. **Security & Scope Guardrail:** `InputGuardrail` validates that the query pertains strictly to a private commercial bank (not an SFI or public procurement).
  3. **Domain Agent Dispatch:** `RegulatoryCoordinatorAgent` dispatches the inquiry to `BotBankingAgent`.
  4. **Statutory Grounding:** The tool `search_thai_fsi_regulatory_circulars` matches `OBL-BOT-122563-02` (*BOT Notification SorNorSor. 12/2563 Clause 5.2.2: Right to Audit*).
  5. **Enterprise GRC Synthesis:** `GrcSynthesizerAgent` compiles harmonized control `CO-REG-TH-FSI-001` and produces an enforceable bilateral contract addendum clause granting Bank of Thailand examiners on-site and remote inspection access with a 30-day notice window.
* **Deterministic Deliverable:** Production-ready bilateral CSP contract redline, board risk assessment document, and BOT regulatory inspection evidence checklist.

---

### 🔹 CUJ 2: Generative AI & Alternative Credit Scoring Governance
* **Primary Persona:** Chief Risk Officer (CRO) & Head of AI / Data Analytics
* **Business Trigger:** The bank's digital consumer lending unit intends to deploy an automated credit scoring ML model utilizing alternative non-traditional data (utility & telco usage), paired with a Generative AI conversational assistant for applicant interactions.
* **Agentic Multi-Agent Execution Flow:**
  1. **Ingress Sanitization:** Officer asks: *"What governance, anti-bias, and explainability controls must we satisfy under Bank of Thailand and ETDA standards before launching AI digital lending?"*
  2. **Strategic Tiered Routing:** `ModelRouter` selects **Gemini 3.7 Flash Extended Thinking (budget: 4096)** for deep statutory synthesis across multiple conflicting authorities.
  3. **Multi-Agent Collaboration:** Dispatches in parallel to `AiGovernanceAgent` and `PdpaComplianceAgent`.
  4. **Multi-Regulator Grounding:** Identifies BOT AI/ML Explainability & Transparency mandates (`OBL-BOT-AI-01`), BOT Fairness & Anti-Bias rules (`OBL-BOT-AI-02`), ETDA AIGC Executive Guidelines (`OBL-ETDA-AIGC-01`), and PDPA Section 30 Automated Decision-Making (`OBL-PDPC-AI-01`).
  5. **Enterprise GRC Synthesis:** Synthesizes `CO-REG-TH-FSI-005`, generating requirements for SHAP feature attribution in adverse action notices, demographic parity audits, automated drift triggers (PSI > 0.25), and an objection workflow allowing denied borrowers to demand manual human underwriter review.
* **Deterministic Deliverable:** End-to-end Enterprise AI Model Governance Policy, Model Risk Management (MRM) validation charter, and adverse action notice templates.

---

### 🔹 CUJ 3: Cross-Border Cloud Disaster Recovery (DR) & Financial PII Transfer
* **Primary Persona:** Data Protection Officer (DPO) & Chief Information Security Officer (CISO)
* **Business Trigger:** The bank is architecting an active-passive disaster recovery failover in a secondary cloud region located outside Thailand (Singapore / Japan). Customer banking transaction histories and KYC biometric vectors will replicate continuously across borders.
* **Agentic Multi-Agent Execution Flow:**
  1. **Ingress Sanitization:** DPO inputs proposed cross-region replication topology. The PII Scrubber redacts sample customer identifiers.
  2. **Domain Collaboration:** `RegulatoryCoordinatorAgent` dispatches to `BotBankingAgent` and `PdpaComplianceAgent`.
  3. **Statutory Reconciliation:** Reconciles PDPA Sections 28–29 (*Adequacy of Foreign Data Protection, Standard Contractual Clauses, Binding Corporate Rules*) with BOT SorNorSor. 12/2563 Clause 5.2.3 (*Cloud Exit Strategy and Business Continuity Planning*).
  4. **Enterprise GRC Synthesis:** Compiles `CO-REG-TH-FSI-003`, mandating Customer-Managed Encryption Keys (CMEK), bilateral Standard Contractual Clauses (SCCs), and semi-annual failover drills with a validated 4-hour Recovery Time Objective (RTO).
* **Deterministic Deliverable:** Formal Cross-Border Transfer Impact Assessment (TIA), bilateral Data Processing Addendum (DPA), and BCP supervisory inspection pack.

---

### 🔹 CUJ 4: Digital Bancassurance Tablet Sales & Electronic Consent
* **Primary Persona:** Head of Bancassurance & Retail Operations Director
* **Business Trigger:** Bank branch relationship managers recommend and sell insurance policies to retail banking customers via branch tablets using paperless electronic signatures.
* **Agentic Multi-Agent Execution Flow:**
  1. **Ingress Sanitization:** Branch operations lead inquires on regulatory requirements for paperless insurance sales at physical branches.
  2. **Domain Collaboration:** Dispatched to `OicInsuranceAgent` and `PdpaComplianceAgent`.
  3. **Statutory Grounding:** Cites OIC IT Governance Notification B.E. 2563 (*Clause 6: Electronic Insurance Policy Distribution Standards*) and PDPA Section 19 (*Explicit Unbundled Consent*).
  4. **Enterprise GRC Synthesis:** Produces `CO-REG-TH-FSI-004` establishing technical controls: biometric e-KYC liveness detection, cryptographic timestamping, strictly unbundled consent checkboxes (separating marketing from underwriting), and automated PDF policy delivery to customer email.
* **Deterministic Deliverable:** Branch electronic sales UX flow compliance specification, audit trail logging protocol, and OIC supervisory inspection pack.

---

## 4. Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── agent.py                 # Coordinator Agent & Root Dispatcher
│   ├── constitution.py          # Regulatory Constitution & Statutory Hierarchy
│   ├── guardrails.py            # Input/Output Guardrails & Human-in-the-Loop Hooks
│   ├── memory.py                # Persistent Session State & Async Compactor
│   ├── observability.py         # OpenTelemetry Tracing, JSON Logger & PII Redaction
│   ├── router.py                # Strategic Model Router (Tiered Thinking)
│   ├── secrets.py               # Secret Manager Client Wrapper
│   ├── subagents/
│   │   ├── __init__.py
│   │   ├── ai_agent.py          # AI Governance Specialist (BOT AI/ML, ETDA AIGC)
│   │   ├── bot_agent.py         # Bank of Thailand (BOT) Specialist
│   │   ├── grc_agent.py         # Enterprise GRC Synthesizer Sub-Agent
│   │   ├── ncsa_agent.py        # NCSA Cybersecurity Act & Data Center CII Specialist
│   │   ├── oic_agent.py         # Office of Insurance Commission (OIC) Specialist
│   │   ├── pdpa_agent.py        # PDPC Data Privacy Specialist
│   │   └── sec_agent.py         # Securities & Exchange Commission (SEC) Specialist
│   └── tools/
│       ├── __init__.py
│       ├── ai_governance_tools.py # AI Governance, Explainability & Model Drift Tools
│       ├── bot_tools.py         # BOT IT Risk (สนส. 12/2563) & Payments Tools
│       ├── error_handler.py     # Guided Error Handling & Recovery Instructors
│       ├── grc_tools.py         # CO-REG-TH Control Synthesis Tools
│       ├── ncsa_tools.py        # NCSA Cybersecurity Act & Data Center CII Tools
│       ├── oic_tools.py         # OIC IT Governance & InsurTech Tools
│       ├── pdpa_tools.py        # PDPA Cross-Border Transfer Tools
│       ├── schemas.py           # Strict Pydantic v2 Input/Output Schemas
│       └── sec_tools.py         # SEC Cyber Resilience Tools
├── eval/
│   ├── eval_dataset.jsonl       # Golden Evaluation Dataset (Positive & SFI Rejection Cases)
│   ├── eval_runner.py           # Automated Test Harness & Metric Scorer
│   └── test_agent_eval.py       # Pytest Integration Suite
├── infra/
│   └── terraform/
│       ├── main.tf              # Cloud Run, Secret Manager & Trace Terraform
│       ├── outputs.tf
│       └── variables.tf
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI Workflow (Lint, Test, Eval)
├── .env.example                 # Zero-secret environment template
├── .gitignore                   # Strict security ignore rules
├── LICENSE                      # Apache 2.0 License
├── pyproject.toml               # Project dependencies & build config
└── README.md
```

---

## 5. Quickstart Guide

### Prerequisites
- Python 3.10+
- `uv` (recommended) or `pip`
- Google Cloud Project with Gemini API access enabled

### Installation
```bash
# Clone the repository
git clone https://github.com/toy9byt/thailand-regulatory-search-agent.git
cd thailand-regulatory-search-agent

# Install dependencies using uv
uv sync --extra dev

# Alternatively using standard pip
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Environment Configuration
```bash
# Copy template configuration
cp .env.example .env

# Configure your Google Cloud Project or Gemini API Key in .env
# GEMINI_API_KEY=your_key_here
```

### Running Automated Evaluations
```bash
# Run unit tests and regression assertions
uv run pytest

# Execute the golden regulatory evaluation harness
uv run python eval/eval_runner.py
```

---

---

## 6. Infrastructure Provisioning & Deployment Guide (Terraform & Agent CLI)

The agent platform supports automated, production-grade deployment across Google Cloud using either **Infrastructure as Code (Terraform)** or the **Google Agents CLI (`agents-cli`)**.

### Option A: Infrastructure as Code Provisioning via Terraform

All necessary cloud infrastructure (Cloud Run, Secret Manager, Cloud Trace, IAM roles, and Service Accounts) is declared under `infra/terraform/`.

```bash
# 1. Navigate to the Terraform directory
cd infra/terraform

# 2. Authenticate with Google Cloud
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID

# 3. Initialize Terraform provider and modules
terraform init

# 4. Review the execution plan
terraform plan -var="project_id=YOUR_PROJECT_ID" -var="region=asia-southeast1"

# 5. Provision the infrastructure
terraform apply -var="project_id=YOUR_PROJECT_ID" -var="region=asia-southeast1" -auto-approve
```

#### Provisioned Cloud Resources:
* **Google Cloud Run v2 Service (`thailand-regulatory-search-agent`):** Auto-scaling (1–10 instances) container runtime in `asia-southeast1` (Bangkok-adjacent).
* **Google Cloud Secret Manager (`thailand-regulatory-gemini-api-key`):** Enterprise secret store securing the Gemini API key without plaintext exposure.
* **Service Account & IAM Roles (`sa-thailand-regulatory-agent`):** Least-privilege roles for `roles/secretmanager.secretAccessor` and `roles/cloudtrace.agent`.

---

### Option B: Fast Lifecycle & Provisioning via Google Agents CLI (`agents-cli`)

The repository natively supports the **Google Agent Development Kit (ADK) Agents CLI** for rapid validation, local simulation, and containerized deployment.

```bash
# 1. Install the Google Agents CLI using uv
uv tool install google-agents-cli
# Alternatively: pip install google-agents-cli

# 2. Validate agent scaffolding, schemas, and constitution
agents-cli scaffold validate .

# 3. Launch local ADK prototype server for interactive verification
agents-cli run --port 8080

# 4. Provision and deploy directly to Cloud Run
agents-cli deploy cloud-run \
  --project YOUR_PROJECT_ID \
  --region asia-southeast1 \
  --service-name thailand-regulatory-search-agent \
  --source .

# 5. Verify live deployed agent health
curl -f https://thailand-regulatory-search-agent-<hash>-as.a.run.app/healthz
```

---

## 7. Security, Confidentiality & Compliance Guardrails

- **Zero Hardcoded Secrets:** All credentials are dynamically resolved via Google Cloud Secret Manager or environment variables. No secrets are stored in version control.
- **Automated PII Scrubbing:** All input payloads and agent traces undergo automated regex and DLP sanitization to mask 13-digit Thai National Identification numbers, banking accounts, and sensitive payment data.
- **Strict Private Banking Scope:** Automated filters identify and reject government procurement statutes and state-owned bank directives, guiding users exclusively to private commercial banking regulations.
- **Statutory Grounding Mandate:** Enforces 100% citation grounding referencing enacted gazette notifications (`[Grounded: ...]`) and excludes unverified media press releases.
- **Human-in-the-Loop (HITL) Gate:** Intercepts high-stakes actions (such as regulatory breach notifications or policy amendments) and requires explicit officer sign-off before dispatch.

## 8. License
Licensed under the [Apache License, Version 2.0](LICENSE).
