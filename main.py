import os
import csv
from netmiko import ConnectHandler
from getpass import getpass



def clear():
    os.system('clear')

clear()
os.system('rm -rf output')

mm_ip = input("What's the IP Address of the primary MCr?\n")
clear()
mm_un = input("What's the username to login to the MCr?\n")
clear()
password = getpass()
clear()


device = {
        "device_type":"aruba_os",
        "host":mm_ip,
        "username":mm_un,
        "password":password,
        }
clear()
net_connect = ConnectHandler(**device)

ap_db = (net_connect.send_command('show ap database long',  use_textfsm=True))
os.system('mkdir output')

keys = ap_db[0].keys()

with open('./output/ap_database.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(ap_db)
