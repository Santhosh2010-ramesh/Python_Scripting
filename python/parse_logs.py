import re
import json

log_file_path = "/tmp/timestamp.log"
output_file_path = "error_logs.json"

error_logs = []

# Regular expression to extract timestamp and error messages
log_pattern = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ERROR - (?P<message>.+)")

with open(log_file_path, "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            error_logs.append({
                "timestamp": match.group("timestamp"),
                "message": match.group("message").strip()
            })

# Write to JSON file
with open(output_file_path, "w") as json_file:
    json.dump(error_logs, json_file, indent=4)

print(f"Extracted {len(error_logs)} error logs and saved to '{output_file_path}'")
