#!/usr/bin/env python3
"""
gap-analysis.py
----------------
Perform a basic gap analysis on the generated RoPA CSV against selected DPDP Act 2023 principles.

Outputs:
- Console summary of potential gaps.
- File: reports/gap-findings.txt (list of findings with row index and description).

Usage:
    python scripts/gap-analysis.py
"""

import pandas as pd
import pathlib

def main():
    base_dir = pathlib.Path(__file__).resolve().parents[1]
    ropa_path = base_dir / "data" / "ropa-generated.csv"
    if not ropa_path.exists():
        raise FileNotFoundError(f"RoPA not found: {ropa_path}. Run generate_ropa.py first.")

    df = pd.read_csv(ropa_path)
    findings = []

    for idx, row in df.iterrows():
        # 1. Notice & Consent: if Legal Basis is Consent but Data Source indicates no form (N/A)
        if row["Legal Basis"] == "Consent" and ("N/A" in str(row["Data Source"]) or pd.isna(row["Data Source"])):
            findings.append((idx, "Notice & Consent",
                f"Data Category '{row['Data Category']}' relies on consent but no explicit data source (form/API) is recorded."))

        # 2. Purpose Limitation: flag if purpose contains multiple conjunctions (simple heuristic)
        purpose = str(row["Processing Purpose"]).lower()
        if (" and " in purpose) or (" & " in purpose) or ("," in purpose and "purpose" not in purpose):
            findings.append((idx, "Purpose Limitation",
                f"Processing Purpose '{row['Processing Purpose']}' may indicate multiple purposes; verify purpose limitation."))

        # 3. Data Minimisation: flag vague categories
        category = str(row["Data Category"]).lower()
        if any(v in category for v in ["other", "misc", "unspecified", "etc."]):
            findings.append((idx, "Data Minimisation",
                f"Data Category '{row['Data Category']}' is vague; consider specifying exact data elements."))

        # 4. Storage Limitation: flag indefinite retention
        retention = str(row["Retention Period"]).lower()
        if "indefinite" in retention or "forever" in retention or ("no limit" in retention):
            findings.append((idx, "Storage Limitation",
                f"Retention Period '{row['Retention Period']}' is indefinite or not defined; define a finite retention schedule."))
        # also flag if numeric > 10 years (simple detection)
        import re
        nums = re.findall(r'\d+', retention)
        if nums:
            try:
                years = int(nums[0])
                if years > 10:
                    findings.append((idx, "Storage Limitation",
                        f"Retention Period '{row['Retention Period']}' exceeds 10 years; verify necessity."))
            except ValueError:
                pass

        # 5. Data Principal Rights: if data is shared with third parties but no note of rights
        shared = str(row["Shared With"]).lower()
        if shared and shared not in ["none", "n/a", ""] and "rights" not in str(row["Remediation Action"]).lower():
            findings.append((idx, "Data Principal Rights",
                f"Data is shared with '{row['Shared With']}' but no explicit mention of data principal rights (access, correction, erasure)."))

    # Output findings
    report_dir = base_dir / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    findings_path = report_dir / "gap-findings.txt"
    with open(findings_path, "w", encoding="utf-8") as f:
        if findings:
            f.write("Potential DPDP Compliance Gaps Identified:\n")
            f.write("="*60 + "\n")
            for idx, area, msg in findings:
                f.write(f"Row {idx} | {area}: {msg}\n")
        else:
            f.write("No potential gaps detected by the basic heuristic checks.\n")

    # Print summary
    print(f"Analysis complete. {len(findings)} potential gap(s) identified.")
    print(f"Details written to: {findings_path}")
    print("\nSample of findings (first 5):")
    for idx, area, msg in findings[:5]:
        print(f" - Row {idx} [{area}]: {msg}")

if __name__ == "__main__":
    main()