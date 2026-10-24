import json
from pathlib import Path
print("Script started")
# Load ticket data from JSON
try:
    with open(json_file, "r") as file:
        ticket_data = json.load(file)
except json.JSONDecodeError:
    print(f"Invalid or empty JSON file: {json_file}")
    continue
``
ticket_number = ticket_data["ticket"]

# Create ticket workspace
ticket_dir = Path(f"tickets/{ticket_number}")
ticket_dir.mkdir(parents=True, exist_ok=True)

(ticket_dir / "evidence").mkdir(exist_ok=True)
(ticket_dir / "configs").mkdir(exist_ok=True)
(ticket_dir / "screenshots").mkdir(exist_ok=True)

# Load template
template_path = Path("templates/network-ticket-template.md")

with open(template_path, "r") as file:
    content = file.read()

# Replace placeholders
content = content.replace("{{TICKET_NUMBER}}", ticket_data["ticket"])
content = content.replace("{{PRIORITY}}", ticket_data["priority"])
content = content.replace("{{DEVICE}}", ticket_data["device"])
content = content.replace("{{REQUESTER}}", ticket_data["requester"])
content = content.replace("{{DESCRIPTION}}", ticket_data["description"])

# Create markdown file
output_file = ticket_dir / f"{ticket_number}.md"

with open(output_file, "w") as file:
    file.write(content)

print(f"Ticket created: {output_file}")