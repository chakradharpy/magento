import os
import pandas as pd

def read_sheet(excel_name, sheet_name, loc, *args):
    # Construct the file path dynamically
    file_path = os.path.join(os.getcwd(), 'exceldata', excel_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found at: {file_path}")

    # Read the sheet
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df[args[0]].iloc[loc]
    except Exception as e:
        raise ValueError(f"Error reading Excel sheet: {e}")
