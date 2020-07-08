#!/usr/bin/python3

import logging
import subprocess
import collections

def collect_ssh_login():
    parse_log_ssh = subprocess.Popen("cat /var/log/auth.log | grep ssh2 | awk '{print $11}'", shell=True, stdout=subprocess.PIPE).stdout
    value_log_ssh = parse_log_ssh.read()
    result_text = (value_log_ssh.decode())
    save_text = open("log_ip","w")
    save_text.write(str(result_text))
    save_text.close()
collect_ssh_login()

with open("log_ip") as infile:
    counts = collections.Counter(i.strip() for i in infile)
for line, count in counts.most_common():
    result_list = "Client IP "+ (str(line)) + " Has logged to this server "+str((count)) + " Times"
    print (result_list)
