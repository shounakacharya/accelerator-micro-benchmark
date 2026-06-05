import pandas as pd
import json

def process_nested_tpu_logs(input_filepath, output_filepath):
    """
    Reads a nested JSONL file and flattens it into a tabular CSV.
    """
    records = []
    
    # Secure the perimeter and gather the evidence line by line
    with open(input_filepath, 'r') as file:
        for line in file:
            if line.strip():
                records.append(json.loads(line))
                
    # Dispatch json_normalize to flatten the nested dictionaries
    df = pd.json_normalize(records)
    
    # Lock it up in a CSV
    df.to_csv(output_filepath, index=False)
    
    print(f"Case closed! Processed {len(df)} records.")
    print(f"Evidence secured in: {output_filepath}")

# Execute the protocol
input_file = 'metrics_report.jsonl'
output_file = 'tpu_benchmarks_v6e_flattened.csv'
process_nested_tpu_logs(input_file, output_file)
