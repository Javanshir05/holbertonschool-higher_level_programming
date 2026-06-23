#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not template:
        print('Error: Template is empty, no output files generated.')
        return

    if not attendees:
        print('Error: No data provided, no output files generated.')
        return

    if not isinstance(template, str):
        print('Error: Invalid input')
        return

    if (not isinstance(attendees, list) or
            not all(isinstance(item, dict) for item in attendees)):
        print('Error: Invalid input')
        return

    for index, attendee in enumerate(attendees, start=1):
        template_schema = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = '{' + f'{key}' + '}'
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
        if not os.path.exists(f'output_{index}.txt'):
            with open(f'output_{index}.txt', 'w') as file:
                file.write(template_schema)
        else:
            print('Error: file already exists')
