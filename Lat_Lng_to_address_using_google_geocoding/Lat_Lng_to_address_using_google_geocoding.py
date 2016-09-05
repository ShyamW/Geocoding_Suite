"""Converts Lat and Lng to addresses using Google Geocoding API (FAST)
@author
    Shyam Thiagarajan
@requires
    empty last line in latAndLong.txt
    addresses.txt is clear
@inputs
    lat,lng from latAndLong.txt
@outputs
    addresses to txt file 'addresses.txt'.

Input is in the following format for latitude and longitude:
    111.9,11111
    1212121,121212
    ...,...
    185673,14532

API KEY:
AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ

"""
import requests

KEY = 'AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ'
out = open('addresses.txt', 'a')


"""Reads Lat and Lng coordinates from latAndLong.txt
@return data
    list of lat and lng"""
def getCoordinates():
    data = []
    with open("latAndLong.txt", 'r') as f:
        for line in f:
            line = line[:-1]  # strip \n
            print(line)
            data.append(line)
    return data


"""Prints address and progress to file and console
@param address
    address to be printed
@param current
    amount of addresses recorded so far
@param total
    total amount of addresses that will be recorded
@updates
    content in addresses.txt"""
def recordData(address, current, total):
    out.write(address + '\n')
    print(address)
    print(str(current) + " of " + str(total))


"""Finds address if available and records result
@param Coordinates
    list of lat and lng"""
def findAddress(coordinates):
    total = len(coordinates)
    progress = 1
    for lat_lng in coordinates:
        param = str("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat_lng + "&key=" + KEY)
        print(param)
        json = requests.get(param).json()
        try:
            address = str(json['results'][1]['formatted_address'])
        except:  # if no lat,lng found
            address = "No Address Returned"
        recordData(address, progress, total)
        progress += 1


"""Main Method"""
def main():
    coordinates = getCoordinates()
    findAddress(coordinates)


if __name__ == '__main__':
    main()
