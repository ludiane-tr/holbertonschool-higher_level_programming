import os

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: The attendees list must be a list of dictionaries.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Error: The template is empty, no files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("Error: No attendees provided, no files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace missing values with "N/A"
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Generate the output file
        filename = f"output_{i}.txt"
        with open(filename, "w") as file:
            file.write(invitation)

        print(f"Invitation generated: {filename}")
