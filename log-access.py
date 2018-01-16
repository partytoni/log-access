#!/usr/bin/python

import datetime
import os
import subprocess
import time

def cycle():
    config_path = os.path.abspath(os.path.dirname(__file__)) + "/log"
    array = ["cat", "/sys/class/power_supply/BAT0/capacity"]
    percentage = (subprocess.check_output(array)).strip()
    array = ["cat", "/sys/class/power_supply/BAT0/status"]
    datetimex= str(datetime.datetime.now()).split(".")[0]
    status = subprocess.check_output(array)
    log_file = open(config_path+"/logfile.txt","a")
    if "Discharging" in status:
        status = "Discharging"
    else:
        status = "Charging"

    log_file.write(status+",\t"+percentage+"%,\t"+datetimex+"\n")
    log_file.close()

def main():
    config_path = os.path.abspath(os.path.dirname(__file__)) + "/log"
    # print(config_path)
    if not os.path.exists(config_path):  # create log folder
        os.makedirs(config_path)
    while True:
        cycle()
        time.sleep(60)


main()
