from PyInquirer import prompt
import csv
from user import users, involved_users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": users
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    involved_questions = [
        {
            "type":"checkbox",
            "name":"users",
            "message":"New Expense - Involved Users: ",
            "choices": [{'name': user, 'checked': (True if user == infos['spender'] else False)} for user in users],
        },
    ]
    involved_infos = prompt(involved_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([infos['amount'], infos['label'], infos['spender']] + involved_infos['users'])
    print("Expense Added !")
    return True


