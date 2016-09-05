"""Python script that converts Business names and states to lat,lng coordinates using google places API
@author
    Shyam Thiagarajan
@requires
    output.txt is clear
    companies.txt and states.txt have equal number of lines
    companies.txt and states.txt have an empty last line
@inputs
    Business names from companies.txt
@inputs
    states of Business names from states.txt
@outputs
    lat and lng to output.txt

API KEY CHOICES:

    AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ
"""
import requests


"""Gets companies from companies.txt
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


"""Gets states from states.txt
@updates states
"""
def getStates(states):
    with open('states.txt') as g:
        for line in g:
            line = line[:-1]
            states.append(line)


"""Writes lat and lng to console and file
@param lat_lng
    coordinates to output
@param out
    file to write to"""
def writeLatLng(lat_lng, out):
    out.write(lat_lng + '\n')
    print(lat_lng)



"""Finds Lat and Lng of Company
@param comp
    company to geolocate
@param count
    index of list (for counting and matching arrays)
@param states
    list of states"""
def findLatLng(comp, count, states):
    name = str(comp)
    name = name.replace(" ", "+")
    # match state and name
    state = states[count]
    print(name)
    param = str(
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + name + "&administrative_level_2=" +
        state + "&components=|country:US" + "&key=" + API_KEY)
    print(param)
    # process JSON
    j = requests.get(param).json()
    try:
        lat = str(j['results'][0]['geometry']['location']['lat'])
        lng = str(j['results'][0]['geometry']['location']['lng'])
        lat_lng = lat + ',' + lng
    except:
        lat_lng = 'error'
    print(str(count) + ' of ' + str(len(states)))
    return lat_lng


"""Determines lat and lng of company and state
@updates output.txt
"""
def main():
    companies = []
    states = []
    getCompanies(companies)
    getStates(states)
    out = open('output.txt', 'a')
    count = 1
    for comp in companies:
        lat_lng = findLatLng(comp, count, states)
        writeLatLng(lat_lng, out)
        count += 1



if __name__ == '__main__':
    API_KEY = 'AIzaSyCFfJiEeUo_nXV6nc1TcOJZIS5RCTJAAHQ'
    main()
    print('DONE')
