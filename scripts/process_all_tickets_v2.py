import json
from pathlib import Path


def load_ticket(json_file):
    with open(json_file, "r") as file:
        return json.load(file)


def create_workspace(ticket_number):
    ticket_dir = Path(f"tickets/{ticket_number}")

    ticket_dir.mkdir(parents=True, exist_ok=True)
    (ticket_dir / "evidence").mkdir(exist_ok=True)
    (ticket_dir / "configs").mkdir(exist_ok=True)
    (ticket_dir / "screenshots").mkdir(exist_ok=True)

    return ticket_dir


def generate_markdown(ticket_data, ticket_dir):
    template_path = Path("templates/network-ticket-template.md")

    with open(template_path, "r") as file:
        content = file.read()

    content = content.replace("{{TICKET_NUMBER}}", ticket_data["ticket"])
    content = content.replace("{{PRIORITY}}", ticket_data["priority"])
    content = content.replace("{{DEVICE}}", ticket_data["device"])
    content = content.replace("{{REQUESTER}}", ticket_data["requester"])
    content = content.replace("{{DESCRIPTION}}", ticket_data["description"])

    output_file = ticket_dir / f"{ticket_data['ticket']}.md"

    with open(output_file, "w") as file:
        file.write(content)


def main():
    data_dir = Path("data")

    for json_file in data_dir.glob("*.json"):
        print(f"Reading {json_file}")

        ticket_data = load_ticket(json_file)

        ticket_dir = create_workspace(ticket_data["ticket"])

        generate_markdown(ticket_data, ticket_dir)

        print(f"Processed {ticket_data['ticket']}")


if __name__ == "__main__":
    main()