"""Python script that converts full line addresses to city, state, or county name
@author
    Shyam Thiagarajan
@requires
    city_state.txt and addresses.txt are open.
    city_state.txt is clear
    addresses.txt has en empty last line
@inputs
    addresses from addresses.txt
@outputs
    city, state or county name, state to city_state.txt
sample input address:
    2115 US-92, Plant City, FL 33563, USA
sample output city, state:
    Plant City, FL

"""


"""Finds city and state from an address
@param address
    address to parse
@return city_state
    city, state or county, state"""
def parseCityState(address):
    try:
        line = address.split(',')
        city = str(line[len(line) - 3]).rstrip().lstrip()
        statefrag = str(line[len(line) - 2]).rstrip()
        state_array = statefrag.split(" ")
        state = str(state_array[1]).rstrip()
        city_state = city + ', ' + state
    except:
        city_state = 'error'
    print(city_state)
    return city_state


"""Writes city_state to city_state_file
@param city_state_file
    file to write city,state
@pararm city_state
    city, state or county, state extracted from address
"""
def updateCityStateFile(city_state_file, city_state):
    city_state_file.write(city_state + '\n')



"""Main Method, Parses city, state or county, state from address.
@updates
    city_state_file
"""
def findCityState():
    city_state_file = open('city_state.txt', 'a')
    with open("addresses.txt", 'r') as f:
        for address in f:
            try:
                city_state = parseCityState(address)
            except:
                city_state = 'ERROR'
                print("!!!!")
            updateCityStateFile(city_state_file, city_state)


if __name__ == '__main__':
    findCityState()