from pathlib import Path
ticket_number = input("Enter ticket number: ")
ticket_dir = Path(f"tickets/{ticket_number}")
ticket_dir.mkdir(parents=True, exist_ok=True)
(ticket_dir / "evidence").mkdir(exist_ok=True)
(ticket_dir / "configs").mkdir(exist_ok=True)
(ticket_dir / "screenshots").mkdir(exist_ok=True)
template_path = Path ("templates/network-ticket-template.md")
with open(json_file, "r") as file:
    ticket_data = json.load(file)
content = content.replace("{{TICKET_NUMBER}}", ticket_number)
output_file =  ticket_dir / f"{ticket_number}.md"
with open(output_file, "w") as file:
	file.write(content)
print(f"Ticket file created: {output_file}")

