import json
from pathlib import Path

data_dir = Path("data")
template_path = Path("templates/network-ticket-template.md")

for json_file in data_dir.glob("*.json"):
    print(f"Reading {json_file}")

    with open(json_file, "r") as file:
        ticket_data = json.load(file)

    ticket_number = ticket_data["ticket"]

    ticket_dir = Path(f"tickets/{ticket_number}")

    ticket_dir.mkdir(parents=True, exist_ok=True)
    (ticket_dir / "evidence").mkdir(exist_ok=True)
    (ticket_dir / "configs").mkdir(exist_ok=True)
    (ticket_dir / "screenshots").mkdir(exist_ok=True)

    with open(template_path, "r") as file:
        content = file.read()

    content = content.replace("{{TICKET_NUMBER}}", ticket_data["ticket"])
    content = content.replace("{{PRIORITY}}", ticket_data["priority"])
    content = content.replace("{{DEVICE}}", ticket_data["device"])
    content = content.replace("{{REQUESTER}}", ticket_data["requester"])
    content = content.replace("{{DESCRIPTION}}", ticket_data["description"])

    output_file = ticket_dir / f"{ticket_number}.md"

    with open(output_file, "w") as file:
        file.write(content)

    print(f"Processed {ticket_number}")