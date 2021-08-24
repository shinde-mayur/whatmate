import csv
import pywhatkit


def schedule_message(contact, message, hour, min):
    pywhatkit.sendwhatmsg(contact, message, int(hour), int(min), 10, tab_close=True)


def replace_all(message, keys, values):
    for key in keys:
        message = message.replace(f"[{key}]", values[key])
    return message


message = input("Enter Message to broadcast (Use '[field]' to use as placeholder):-")
time = input("Send message at (Use 24 hr format) eg. 13:23 :-")
hr, mn = time.split(':')

contacts = []

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    head = next(reader)
    for row in reader:
        contacts.append(dict(zip(head, row)))

keys = list(contacts[0].keys())[1:]
for contact in contacts:
    schedule_message(contact['contact'], replace_all(message, keys, contact), hr, mn)
    mn += 1
    if mn >= 60:
        hr, mn = hr+1, 0
    if hr > 24:
        hr = 00
