from PyInquirer import prompt
import csv

users = []
with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            users.append(row[0])

involved_users = []
with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            involved_users.append(
                {
                    'name': row[0]
                }
            )

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([infos['name']])
    print("User Created !")
    return True