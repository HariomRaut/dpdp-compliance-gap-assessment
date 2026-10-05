# DPDP Act 2023 Compliance Gap Assessment (Academic Simulation)

## Project Overview
This project simulates a privacy‑compliance audit for a fictional college‑portal (student‑information system) under India’s Digital Personal Data Protection Act, 2023 (DPDP Act). The goal is to demonstrate how to:

1. Map the personal data lifecycle and produce a **Record of Processing Activities (RoPA)**.
2. Assess the portal against DPDP obligations (notice & consent, purpose limitation, data minimisation, storage limitation, data principal rights).
3. Map identified gaps to **ISO/IEC 27001:2022 Annex A** controls.
4. Produce a remediation checklist that links privacy gaps to actionable technical and organisational measures.

## Directory Structure
```
dpdp-compliance-gap-assessment/
│
├─ README.md                 # This file
├─ docs/
│   ├─ dpdp-act-summary.md   # High‑level summary of DPDP Act 2023 principles
│   └─ iso27001-annex-a.md   # Mapping of Annex A controls to privacy gaps
├─ data/
│   ├─ personal-data-inventory.csv   # Sample inventory of data fields collected
│   └─ ropa-template.csv             # Template for Record of Processing Activities
├─ scripts/
│   ├─ generate_ropa.py          # Python script to convert inventory → RoPA
│   └─ gap-analysis.py           # Simple script to flag gaps based on rules
├─ reports/
│   ├─ gap-assessment-report.md  # Example final report
│   └─ remediation-checklist.md  # Example checklist linked to ISO 27001 controls
└─ references/
    ├─ DPDP-Act-2023.pdf         # (Link to official gazette)
    └─ ISO27001-2022.pdf         # (Link to standard)
```

## How to Reproduce the Work

### Prerequisites
- Python 3.8+
- Required Python packages: `pandas` (install via `pip install pandas`)

### Step‑by‑Step

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your‑username>/dpdp-compliance-gap-assessment.git
   cd dpdp-compliance-gap-assessment
   ```

2. **Prepare the data inventory**
   - Edit `data/personal-data-inventory.csv` to reflect the data fields your system collects.
   - Sample columns: `Data Category, Processing Purpose, Legal Basis, Source (Form/API), Storage Location, Retention Period, Shared With`.

3. **Generate the RoPA**
   ```bash
   python scripts/generate_ropa.py
   ```
   - Output: `data/ropa-generated.csv` (ready for audit).

4. **Run the gap analysis**
   ```bash
   python scripts/gap-analysis.py
   ```
   - The script reads the generated RoPA and flags any rows that violate DPDP principles (e.g., missing consent, excessive retention). Results are printed to console and also saved to `reports/gap-findings.txt`.

5. **Review the example reports**
   - Open `reports/gap-assessment-report.md` for a narrative of findings.
   - Open `reports/remediation-checklist.md` to see how each gap maps to an ISO 27001:2022 control (e.g., A.8.2 Privilege Management, A.9.4.2 Secure Log‑on).

### Extending the Project
- Replace the CSV inventory with data extracted from your actual database or API.
- Integrate the scripts into a CI pipeline that runs on every code change to continuously monitor compliance.
- Expand the gap‑analysis script to incorporate more sophisticated rules (e.g., purpose‑creep detection using data‑lineage metadata).

## Key Learning Outcomes
- Understanding of DPDP Act 2023 principles and how they translate into actionable controls.
- Practical experience drafting a RoPA—a core artefact for any GDPR/DPDP compliance program.
- Ability to map legal requirements to technical safeguards using a recognised standard (ISO 27001).
- Experience producing clear, stakeholder‑friendly compliance reports and remediation plans.

## License
This project is licensed under the MIT License – see the `LICENSE` file for details.

## Acknowledgements
- DPDP Act, 2023 – Ministry of Electronics and Information Technology, Government of India.
- ISO/IEC 27001:2022 – International Organization for Standardization.
- Open source libraries: pandas.
