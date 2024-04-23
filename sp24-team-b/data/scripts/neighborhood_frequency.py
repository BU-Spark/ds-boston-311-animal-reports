import pandas as pd
from collections import defaultdict, Counter

zipcode_complaints = defaultdict(Counter)
zipcode_report_counts = Counter()

for year in range(2013, 2024):
    file_name = f'filtered_{year}.csv'  # Updated path to match uploaded files
    try:
        df = pd.read_csv(file_name)
        
        if 'location_zipcode' in df.columns and 'case_title' in df.columns:
            valid_rows = df.dropna(subset=['location_zipcode', 'case_title'])
            valid_rows = valid_rows[(valid_rows['location_zipcode'].astype(str).str.strip() != "") & (valid_rows['case_title'].str.strip() != "")]
            
            for _, row in valid_rows.iterrows():
                # format the zipcode to remove '.0' and prepend '0'
                zipcode = "0" + str(int(row['location_zipcode'])).strip()  # convert zipcode to integer then to string and prepend '0'
                complaint = row['case_title'].strip()
                zipcode_report_counts[zipcode] += 1
                zipcode_complaints[zipcode][complaint] += 1
        else:
            missing_columns = []
            if 'location_zipcode' not in df.columns:
                missing_columns.append("'location_zipcode'")
            if 'case_title' not in df.columns:
                missing_columns.append("'case_title'")
            print(f"{missing_columns} column(s) not found in {file_name}")
    except FileNotFoundError:
        print(f"{file_name} not found.")

sorted_zipcodes = sorted(zipcode_report_counts, key=zipcode_report_counts.get, reverse=True)

for zipcode in sorted_zipcodes:
    num_reports = zipcode_report_counts[zipcode]
    most_common_complaint, count = zipcode_complaints[zipcode].most_common(1)[0]
    print(f"{zipcode}: {num_reports} reports | Most Common Complaint: '{most_common_complaint}' with {count} complaints.")


