from PyInquirer import prompt
import csv
from user import users

def bank(*args):
    with open('bank.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in users:
            spamwriter.writerow([i, 0])
    return True