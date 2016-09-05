import requests
"""
Converts lat, lng from latAndLong.txt and converts it to county fips in county_fips.txt.
@author
    Shyam Thiagarjan
@requires
    lat and lng are separated by @code DELIMITER
    empty last line in latAndLong.txt
    county_Fips.txt is clear

Input is in the following format for latitude and longitude:
    111.9\t11111
    1212121\t121212
    ...,...
    185673\t14532

Sample Output:
    Fips code, county name, state, state abbreviation

"""
DELIMITER = ','
out = open('county_Fips.txt', 'a')


"""Converts Lat and Lng to County Data and Writes data to file
@param lat
    latitude to process
@param lng
    longitude to process
    """
def processLatAndLng(lat, lng):
    param = str(
        "http://data.fcc.gov/api/block/find?format=json&latitude=" + lat + "&longitude=" + lng + "&showall=true")
    print(param)
    # process JSON
    r = requests.get(param)
    j = r.json()
    try:
        FIPS = str(j['County']['FIPS'])
        county_name = str(j['County']['name'])
        state = str(j['State']['name'])
        abv_state = str(j['State']['code'])
        print(FIPS)
        out.write(county_name + ',' + state + '\n')
    except:  # if not lat,lng found
        out.write("error" + '\n')
        print("WOOPS")


"""Converts lat\tlng to FIPS
@param line
    address line
"""
def convertToDataAndWrite(line):
    if "error" in line:
        out.write("error" + "\n")
    else:
        line = line.split(DELIMITER)
        print(line)
        lat = line[0]
        lng = line[1][:-1]  # remove space and \n
        processLatAndLng(lat, lng)


"""Main Method"""
def main():
    with open("latAndLong.txt", 'r') as f:
        for line in f:
            convertToDataAndWrite(line)


if __name__ == '__main__':
    main()
