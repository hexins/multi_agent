import pandas as pd

# Extract Lead Data
def extract_lead_data(file_path):
    leads = []
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        lead = {
            "name": row["Name"],
            "email": row["Email"],
            "company": row["Company"],
            "job_title": row["Job Title"],
            "industry": row["Industry"]
        }
        leads.append(lead)
    return leads
