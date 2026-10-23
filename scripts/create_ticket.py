from pathlib import Path
ticket_number = input("Enter ticket number: ")
template_path = Path ("templates/network-ticket-template.md")
with open(template_path, "r") as file:
	content= file.read()
content = content.replace("{{TICKET_NUMBER}}", ticket_number)
output_dir = Path ("docs/tickets")
output_dir.mkdir(parents=True,exist_ok=True)
output_file= output_dir / f"{ticket_number}.md"
with open(output_file, "w") as file:
	file.write(content)
print(f"Ticket file created: {output_file}")

