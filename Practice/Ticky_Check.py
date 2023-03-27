#!/usr/bin/env python3
import sys
import re
import operator
import csv

# Dict: Count number of entries for each user
per_user = {}  # Splitting between INFO and ERROR
# Dict: Number of different error messages
errors = {}

# * Read file and create dictionaries
with open('syslog.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        # * Sample Line of log file
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # Populates error dict with ERROR messages from log file
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] += 1
        # Populates per_user dict with users and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        # Populates per_user dict with users logs entry
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['INFO'] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['ERROR'] = 0
            else:
                per_user[user]['ERROR'] += 1


# Sorted by VALUE (Most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

# Sorted by USERNAME
per_user_list = sorted(per_user.items())

file.close()
# Insert at the beginning of the list
with open('user_statistics.csv', 'w', newline='') as user_csv:
    user_csv.write('Username'+','+'INFO'+','+'ERROR'+'\n')
user_csv.close()

with open('error_message.csv', 'w', newline='') as error_csv:
    error_csv.write('ERROR '+','+'Count'+'\n')
error_csv.close()

# * Create CSV file user_statistics
with open('user_statistics.csv', 'a', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' + str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# * Create CSV error_message
with open('error_message.csv', 'a', newline='') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ',' + str(value) + '\n')
