# This file will generate the user list from the given CSV file

import csv
userList = [] # list of students to check if their parents have the right schools attached
file = 'users.csv';
rowCount = 0;
# Count how many rows are in the CSV file
def row_count(file):
    with open(file) as in_file:
        return sum(1 for _ in in_file)


# Feeds the CSV file into userlist
def populateUserList():

    rowCount = row_count(file)

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            print(row)
            userList.append(row)
            if count > rowCount:  # break loop at end of file
                break
            count += 1