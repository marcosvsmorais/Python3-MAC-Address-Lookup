#!/usr/bin/python3

import requests
import time
 
for addr in ["00:00:00:00:00:00","11:11:11:11:11:11"]:
    vendor = requests.get('https://api.maclookup.app/v2/macs/'+addr+'/company/name')
    time.sleep(0.5)
    print(addr, vendor.text)