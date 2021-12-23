from random import uniform
import csv
import random
import time

namafile = 'data3D.csv'

header1 = "altitude"
header2 = "latitude"
header3 = "longitude"

altitude = 0
latitude = uniform(27.10,27.50)
longitude = uniform(48.25,48.35)

fieldnames = [header1, header2, header3]


with open(namafile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open(namafile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            header1: altitude,
            header2: latitude,
            header3: longitude
        }

        csv_writer.writerow(info)
        print(altitude, latitude,longitude)

        altitude += 1
        latitude = uniform(27.10,27.50)
        longitude = uniform(48.25,48.35)

    time.sleep(1)