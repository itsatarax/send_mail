import csv


def get_csv_data(name):
    filename = open('uploads/' + name, 'r')

    file = csv.DictReader(filename)

    emails = []

    for col in file:
        emails.append(col["Email Address"])

    return emails
