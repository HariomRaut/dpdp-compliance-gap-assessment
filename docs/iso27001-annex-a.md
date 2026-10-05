# ISO/IEC 27001:2022 – Annex A Controls Relevant to DPDP Act 2023

Below is a mapping of selected ISO 27001 Annex A controls to the DPDP Act 2023 obligations discussed in `docs/dpdp-act-summary.md`. Use this matrix when drafting your remediation checklist.

| DPDP Obligation | ISO 27001:2022 Annex A Control | Control Objective (brief) | Example Implementation |
|-----------------|--------------------------------|--------------------------|------------------------|
| Notice & Consent | **A.8.2 Privilege Management** | Ensure that privileges are granted based on job‑function and need‑to‑know. | Role‑based access to consent management logs; only privacy team can view consent receipts. |
|  | **A.9.4.2 Secure Log‑on** | Ensure that access to systems is controlled via a secure log‑on procedure. | Multi‑factor authentication for any system that stores or processes consent records. |
| Purpose Limitation | **A.12.6.1 Management of Technical Vulnerabilities** | Obtain timely information about technical vulnerabilities to prevent exploitation. | Regular scanning of forms/applications to ensure no hidden fields that repurpose data. |
|  | **A.18.2.3 Technical Compliance Review** | Regularly review compliance with information security policies and standards. | Quarterly review of data‑flow diagrams to verify that data are used only for declared purposes. |
| Data Minimisation | **A.8.1.1 Inventory of Assets** | Identify and maintain an inventory of assets. | Maintain a data‑asset register that logs each personal data field and its justification. |
|  | **A.13.2.1 Information Transfer Policies and Procedures** | Ensure that policies governing information transfer are in place. | Block outgoing transfers of fields not needed for the declared purpose (DLP rules). |
| Storage Limitation | **A.8.2.3 Management of Removable Media** | Manage removable media securely according to classification. | Encrypted backups with auto‑expire after retention period. |
|  | **A.12.4.1 Event Logging** | Record events and generate logs. | Log retention‑policy enforcement actions (purge jobs). |
| Data Principal Rights | **A.16.1.5 Response to Information Security Incidents** | Respond to information security incidents according to documented procedures. | Procedure to handle erasure requests (right to be forgotten) as a security incident. |
|  | **A.18.2.2 Compliance with Security Policies and Standards** | Ensure that organizational procedures comply with its security policies. | SLA tracking for DSR fulfillment (access, correction, portability). |
| Data Breach Notification | **A.16.1.6 Learning from Information Security Incidents** | Learn from incidents and adjust controls accordingly. | Post‑breach review to improve detection and notification timelines. |
|  | **A.6.1.3 Contact with Authorities** | Maintain appropriate contacts with relevant authorities. | Pre‑established liaison with the Data Protection Board of India. |
| Accountability & Governance | **A.5.1.1 Policies for Information Security** | Define and approve information security policy. | Overarching privacy & security policy referencing DPDP Act. |
|  | **A.5.1.2 Review of the Policies for Information Security** | Review policies at planned intervals or if significant changes occur. | Annual review of DPDP compliance program. |
|  | **A.18.2.1 Compliance with Legal and Contractual Requirements** | Identify and comply with all applicable legal, statutory, regulatory, and contractual requirements. | Maintain a legal register that includes DPDP Act 2023. |

### How to Use This Mapping
1. Identify a DPDP gap from your assessment (e.g., “Consent not recorded for phone numbers”).  
2. Find the corresponding ISO 27001 control(s) (e.g., A.9.4.2, A.8.2).  
3. Implement the control’s objective (e.g., enforce MFA on consent‑management system, maintain privileged access logs).  
4. Document the implementation in your remediation checklist (see `reports/remediation-checklist.md`).

### References
- ISO/IEC 27001:2022 – Information technology — Security techniques — Information security management systems — Requirements (https://www.iso.org/standard/82875.html)
- ISO 27002:2022 – Code of practice for information security controls (https://www.iso.org/standard/82876.html)
