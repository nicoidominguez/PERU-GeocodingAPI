# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:58 2016
Last modified on June 2018

@author: ndominguez
"""

#For RENAMU (city-halls) directions
import requests

f = open("renamu_dir.txt", 'r')
addresses = f.readlines()
direc = []
for address in addresses[0:len(addresses) - 1]:
    direc.append(address[0:len(address) - 1])
direc.append(addresses[-1])
f.close()

lat = []
lon = []
for direccion in direc:
    address2 = ""
    for i, char in enumerate(direccion):

        if char == " ":
            address2 += "+"
        else:
            address2 += char

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address2
    response = requests.get(url)

    resp_json_payload = response.json()

    if resp_json_payload['status'] == "OK":
        a = resp_json_payload['results'][0]['geometry']['location']
        lat.append(a["lat"])
        lon.append(a["lng"])
    else:
        lat.append(999)
        lon.append(999)

    print('Direcciones calculadas: {}'.format(len(lat) + 1))

f = open("renamu-coords.txt", 'w')
f.write("address\tlat\tlon\n")

for i, address in enumerate(addresses):
    towrite = address + "\t" + str(lat[i]) + "\t" + str(lon[i]) + "\n"
    f.write(towrite)

f.close()

