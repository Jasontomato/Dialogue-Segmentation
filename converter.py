# converter.py
import csv
import os
import re

def convert_to_csv(input_file, output_file):
    # Check if input file exists and is readable
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.")
    if not os.access(input_file, os.R_OK):
        raise PermissionError(f"The input file '{input_file}' is not readable.")

    # Read and normalize the file content to handle different newline characters
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().replace('\r\n', '\n').replace('\r', '\n')
    except UnicodeDecodeError:
        raise ValueError("The file could not be read due to encoding issues. Ensure it's UTF-8 encoded.")

    # Split the content into dialogue entries
    entries = re.split(r'(?<=\n)(?=\S+\s+\d{2}:\d{2}\s)', content)

    data = []
    for entry in entries:
        lines = entry.strip().split('\n')
        if lines:
            match = re.match(r'(\S+)\s+(\d{2}:\d{2})', lines[0])
            if match:
                name, time = match.groups()
                dialogue = ' '.join(line.strip() for line in lines[1:] if line).strip()
                data.append([name, time, dialogue])

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the output to CSV
    try:
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Time', 'Dialogue'])
            writer.writerows(data)
    except Exception as e:
        raise IOError(f"Failed to write to the output file '{output_file}': {e}")
