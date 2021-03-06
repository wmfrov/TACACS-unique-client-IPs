"""
Imports all system logs found in a directory and tells you how many
clients with unique IP addresses have connected to the server.
Output is to text file in the directory. No input necessary.
"""

import csv
import os
import re

def open_all_logs():
    """
    opens all logs in the current directory that start with the name
    "System" and end with filetype ".CSV" or ".csv"
    """
    all_logs = []
    directory_input = os.getcwd()
    for filename in os.listdir(directory_input):
        if re.search("^System.*csv$", filename, re.I):
            with open(os.path.join(directory_input, filename), 'r') as csv_file:
                content = csv.reader(csv_file, delimiter=",")
                all_logs = [line[4] for line in content if len(line[4]) > 0 \
                    if line[4] != "NAS_IP" if line[4] not in all_logs]
    return all_logs

def main():
    """
    Uses the output of open_all_logs to parse the logs and outputs the number of unique IP
    addresses found in the logs
    and each IP address to a text file in the current directory called "unique_clients.txt"
    """
    csv_log = open_all_logs()
    unique_ip_list = []
    unique_ip_count = 0
    unique_ip_string = ""
    for ip_address in csv_log:
        if ip_address not in unique_ip_list:
            unique_ip_count += 1
            unique_ip_string = unique_ip_string + ip_address + "\n"
            unique_ip_list.append(ip_address)
    unique_ip_string = unique_ip_string[:-1]
    output = str(unique_ip_count) + " Unique IP addresses found in logs " \
         "\n" + "Unique IP addresses:\n" + unique_ip_string
    try:
        with open('unique_clients.txt', 'w') as output_file:
            output_file.write(output)
        print("Writing output file 'unique_clients.txt' to current directory", os.getcwd())
    except PermissionError:
        print("Permission error occurred. Unable to write output file to current directory", os.getcwd())
    return output

print(main())
