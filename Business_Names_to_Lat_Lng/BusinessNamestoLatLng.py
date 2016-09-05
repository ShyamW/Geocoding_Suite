"""Python script that converts Business names to lat,lng coordinates using google places API
@author
    Shyam Thiagarajan
@requires
    output.txt is empty
    empty last line in companies.txt
@inputs
    Business names from companies.txt
@outputs
    lat and lng to output.txt

API KEY CHOICES:

    AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ
"""
import requests


"""Gets companies from companies.txt.
@param companies
    list of companies to geolocate
@updates companies"""
def getCompanies(companies):
    with open('companies.txt') as f:
        names = (f.readlines())
        for words in names:
            try:
                words = words.split('(', 1)[0]
                words = words.split('-', 1)[0]
                print(words)
                companies.append(words)
            except:
                companies.append(words)


"""Writes lat and lng to console and file.
@param lat_lng
    coordinates to output
@param out
    file to write to"""
def writeLatLng(lat_lng, out):
    out.write(lat_lng + '\n')
    print(lat_lng)



"""Finds Lat and Lng of Company.
@param comp
    company to geolocate
@param count
    index of list (for counting)
@param total
    total number of names to geocode
"""
def findLatLng(comp, count, total):
    name = str(comp)
    name = name.replace(" ", "+")
    print(name)
    param = str(
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + name + "&administrative_level_2=" +
        "&components=|country:US" + "&key=" + API_KEY)
    print(param)
    # process JSON
    r = requests.get(param)
    j = r.json()
    try:
        lat = str(j['results'][0]['geometry']['location']['lat'])
        lng = str(j['results'][0]['geometry']['location']['lng'])
        lat_lng = lat + ',' + lng
    except:
        lat_lng = 'error'
    print(str(count) + ' of ' + str(total))
    return lat_lng


"""Determines lat and lng of company.
@updates output.txt
"""
def main():
    companies = []
    getCompanies(companies)
    out = open('output.txt', 'a')
    count = 1
    total = len(companies)
    for comp in companies:
        lat_lng = findLatLng(comp, count, total)
        writeLatLng(lat_lng, out)
        count += 1


if __name__ == '__main__':
    API_KEY = 'AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ'
    main()
    print('DONE')
