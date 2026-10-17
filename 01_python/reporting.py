
from pathlib import Path
import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "02_Data"


def export_report(data, filename, index=False):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_path = DATA_DIR / filename
    data.to_csv(output_path, index=index)

    print(f"Report saved successfully: {output_path.name}")
    return output_path


def export_text_report(content, filename):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = DATA_DIR / filename

    output_path.write_text(content, encoding="utf-8")

    print(f"Text report saved successfully: {output_path.name}")
    return output_path 
