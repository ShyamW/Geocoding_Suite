"""
Python script that converts lat,lng to an address using Geopy API (Slow)
@author
    Shyam Thiagarajan
@requires
    empty last line in latAndLong.txt
    addresses.txt is clear
@inputs
    lat,lng from latAndLong.txt
@outputs
    addresses to 'addresses.txt'.

Input is in the following format for latitude and longitude:
    111.9\t11111
    1212121\t121212
    ...\t...
    185673\t14532

"""
from geopy.geocoders import Nominatim
import time


DELIMITER = '\t'
geolocator = Nominatim()
file_out = open('addresses.txt', 'a')


"""Converts Coord to address and writes to file.
@param lat_lng
    lat and long seperated by !
@updates file_out
"""
def convertCoordToAddress(lat_lng):
    location = geolocator.reverse(lat_lng)
    try:
        file_out.write(str(location.address) + "\n")
        # pause to avoid bandwidth limitation
        time.sleep(4)
        print(location.address)
    except:
        print("omitted" + 'due to encoding error')
        file_out.write('omitted due to encoding error' + "\n")


"""Reads Coordinates from latAndLong.txt
@return data
    list of lat and lng separated by ', ' """
def readCoordinates():
    with open("latAndLong.txt", 'r') as f:
        data = []
        # read all data from file into list
        for line in f:
            lat_long = (line.split(DELIMITER))
            print(lat_long)
            lat = lat_long[0]
            long = lat_long[1]
            # convert data to parameter format
            param = (lat+", " + long)
            data.append(param)
    return data


"""Main Method"""
def main():
    data = readCoordinates()
    progress = 1
    for lat_lng in data:
        convertCoordToAddress(lat_lng)
        print(str(progress) + ' of ' + str(len(data)))
        progress += 1


if __name__ == '__main__':
    main()