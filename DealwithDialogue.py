import csv
import re

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content into dialogue entries
    entries = re.split(r'\n(?=\S+\s+\d{2}:\d{2})', content)

    data = []
    for entry in entries:
        lines = entry.strip().split('\n')
        if lines:
            # Extract name and time from the first line
            match = re.match(r'(\S+)\s+(\d{2}:\d{2})', lines[0])
            if match:
                name, time = match.groups()
                # Join the rest of the lines as dialogue
                dialogue = ' '.join(lines[1:]).strip()
                data.append([name, time, dialogue])

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Time', 'Dialogue'])
        writer.writerows(data)

