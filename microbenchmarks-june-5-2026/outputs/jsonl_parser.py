import pandas as pd

def convert_jsonl_to_csv_pandas(input_filepath, output_filepath):
    # read_json with lines=True handles the JSONL format natively
    # It automatically finds all unique keys and creates columns for them
    df = pd.read_json(input_filepath, lines=True)
    
    # Export to CSV, ignoring the index column
    df.to_csv(output_filepath, index=False)
    
    print(f"Successfully converted {input_filepath} to {output_filepath}")
    print(f"Total rows: {len(df)}, Total columns: {len(df.columns)}")

# Example usage
input_file = 'metrics_report.jsonl'
output_file = 'tpu_v6e_benchmarks.csv'
convert_jsonl_to_csv_pandas(input_file, output_file)
