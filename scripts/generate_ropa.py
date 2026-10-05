#!/usr/bin/env python3
"""
generate_ropa.py
----------------
Convert a personal‑data inventory CSV into a Record of Processing Activities (RoPA)
template suitable for DPDP Act 2023 compliance audits.

Usage:
    python scripts/generate_ropa.py
    # Outputs data/ropa-generated.csv
"""

import pandas as pd
import pathlib

def main():
    # Paths
    base_dir = pathlib.Path(__file__).resolve().parents[1]
    inventory_path = base_dir / "data" / "personal-data-inventory.csv"
    ropa_path = base_dir / "data" / "ropa-generated.csv"
    template_path = base_dir / "data" / "ropa-template.csv"

    # Load inventory
    df_inv = pd.read_csv(inventory_path)

    # Ensure required columns exist
    required_cols = [
        "Data Category",
        "Processing Purpose",
        "Legal Basis",
        "Source (Form/API)",
        "Storage Location",
        "Retention Period",
        "Shared With"
    ]
    missing = [c for c in required_cols if c not in df_inv.columns]
    if missing:
        raise ValueError(f"Missing columns in inventory: {missing}")

    # Build RoPA: add extra columns for controls, risks, remediation (initially empty)
    ropa_cols = [
        "Data Category",
        "Processing Purpose",
        "Legal Basis",
        "Data Source",
        "Storage Location",
        "Retention Period",
        "Shared With",
        "Security Measures",          # to be filled based on ISO 27001 mapping
        "Risks Identified",
        "Remediation Action"
    ]

    # Map inventory columns to RoPA columns
    df_ropa = pd.DataFrame()
    df_ropa["Data Category"] = df_inv["Data Category"]
    df_ropa["Processing Purpose"] = df_inv["Processing Purpose"]
    df_ropa["Legal Basis"] = df_inv["Legal Basis"]
    df_ropa["Data Source"] = df_inv["Source (Form/API)"]
    df_ropa["Storage Location"] = df_inv["Storage Location"]
    df_ropa["Retention Period"] = df_inv["Retention Period"]
    df_ropa["Shared With"] = df_inv["Shared With"]
    df_ropa["Security Measures"] = ""
    df_ropa["Risks Identified"] = ""
    df_ropa["Remediation Action"] = ""

    # Reorder columns
    df_ropa = df_ropa[ropa_cols]

    # Save
    ropa_path.parent.mkdir(parents=True, exist_ok=True)
    df_ropa.to_csv(ropa_path, index=False)
    print(f"RoPA generated: {ropa_path}")
    print("Next steps: fill in Security Measures, Risks Identified, and Remediation Action "
          "using the ISO 27001 mapping (docs/iso27001-annex-a.md).")

if __name__ == "__main__":
    main()