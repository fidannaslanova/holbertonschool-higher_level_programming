#!/usr/bin/python3
"""Module for generating personalized invitation files from a template"""


def generate_invitations(template, attendees):
    """Generates invitation files from template and attendees list"""
    if not isinstance(template, str):
        print("Error: template is not a string")
        return
    if not isinstance(attendees, list) or not all(
            isinstance(a, dict) for a in attendees):
        print("Error: attendees is not a list of dictionaries")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        with open("output_{}.txt".format(i), 'w') as f:
            f.write(content)
