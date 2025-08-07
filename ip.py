import os #for Clear
import sys#for Animation
import time#for Time
import requests
import shutil
os.system("pkg update && pkg upgrade -y")
os.system("clear")

#Type With Animation
print("\n\n\n\n\n")
ab="                 \033[33m System Loading..........."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time
print("\n\n\n\n\n")

time.sleep(2)
os.system("pip install requests")
os.system("clear")

ab="                   \033[1;32m Loading Completed"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time
Name=input("     \n\n\n            \033[1;31m Enter Your Name: ")
  
  
ab="            \033[1;31m Hey "+ Name +", Be Ethical...."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

columns = shutil.get_terminal_size().columns

logo_lines = [
    ":::::::::  :::    ::: ::::::::: ",
    ":+:    :+: :+:   :+:  :+:    :+:",
    "+:+    +:+ +:+  +:+   +:+    +:+",
    "+#++:++#:  +#++:++    +#+    +:+",
    "+#+    +#+ +#+  +#+   +#+    +#+",
    "#+#    #+# #+#   #+#  #+#    #+#",
    "###    ### ###    ### #########"
]

print("\033[1;91m")

for line in logo_lines:
    print(line.center(columns))

print("\033[0m")

print("\033[32m" + "=" * columns + "\033[1;96m")
print(" Owner     : RKD TEAM")
print(" Github    : RKD-TEAM")
print(" Facebook  : RKD TEAM")
print(" Tool Name : ip Location")
print("\033[31m This Tool For Educational Purposes Only. So Don't Use For Any Crime")
print("\033[32m" + "=" * columns + "\033[0m")


print("\033[1;91mFor Find Your ip Address :>>>>>\033[35mhttps://ip-api.com\033[1;91<<<<<")

ip=input("\033[1;32mEnter Your ip : ")

req=requests.get("http://ip-api.com/json/"+ip)

txt=req.json()

print(f"\033[1;91m{'Status' :<32}: {txt['status']}\033[0m")
print(f"\033[1;91m{'Country' :<32}: {txt['country']}\033[0m")
print(f"\033[1;91m{'Country Code' :<32}: {txt['countryCode']}\033[0m")
print(f"\033[1;91m{'Region' :<32}: {txt['region']}\033[0m")

print(f"\033[1;96m{'Division Name' :<32}: {txt['regionName']}\033[0m")
print(f"\033[1;96m{'City' :<32}: {txt['city']}\033[0m")
print(f"\033[1;96m{'ZIP Code' :<32}: {txt['zip']}\033[0m")
print(f"\033[1;96m{'Latitude' :<32}: {txt['lat']}\033[0m")

print(f"\033[1;92m{'Longitude' :<32}: {txt['lon']}\033[0m")
print(f"\033[1;92m{'Timezone' :<32}: {txt['timezone']}\033[0m")
print(f"\033[1;92m{'Internet Service Provider (ISP)' :<32}: {txt['isp']}\033[0m")
print(f"\033[1;92m{'Organization' :<32}: {txt['org']}\033[0m")

print(f"\033[1;95m{'Autonomous System (AS)' :<32}: {txt['as']}\033[0m")
print(f"\033[1;95m{'IP Address (Query)' :<32}: {txt['query']}\033[0m")

print("\033[96m         >>>>>>For Live Lacation View<<<<<<")

print(f"\033[1;91mFor Live Location : https://www.google.com/maps/search/?api=1&query={txt['lat']},{txt['lon']}\033[0m")

#{'status': 'success', 'country': 'Canada', 'countryCode': 'CA', 'region': 'QC', 'regionName': 'Quebec', 'city': 'Montreal', 'zip': 'H1K', 'lat': 45.6085, 'lon': -73.5493, 'timezone': 'America/Toronto', 'isp': 'Le Groupe Videotron Ltee', 'org': 'Videotron Ltee', 'as': 'AS5769 Videotron Ltee', 'query': '24.48.0.1'}