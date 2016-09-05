"""Python script that converts full line addresses to [city or county], [state].
@author
    Shyam Thiagarajan
@requires
    city_state.txt and addresses.txt are open.
    city_state.txt is clear
    addresses.txt has an empty last line
@inputs 
    addresses from addresses.txt
@outputs 
    city, state or county name, state to city_state.txt
sample input address:
    United States House of Representatives,..., Washington, District of Columbia, 20540, United States of America
sample output city, state:
    Washington, District of Columbia
"""


"""Finds city and state from an address
@param address
    address to parse
@return city_state
    city, state or county, state"""
def findCityStateFromFragment(address):
    try:
        address_array = address.split(',')
        city = str(address_array[len(address_array) - 4]).rstrip().lstrip()
        state = str(address_array[len(address_array) - 3]).rstrip()
        city_state = city + ', ' + state
    except:
        city_state = 'error'
    print(city_state)
    return city_state


"""Writes city_state to city_state_file
@param city_state_file
    file to write city,state
@pararm city_state
    city, state or county, state extracted from address"""
def updateCityStateFile(city_state_file, city_state):
    city_state_file.write(city_state + '\n')


"""Parses city, state or county, state from address
@updates
    city_state_file"""
def geopyParseCityState():
    city_state_file = open('city_state.txt', 'a')
    with open("addresses.txt", 'r') as f:
        for address in f:
            try:
                city_state = findCityStateFromFragment(address)
            except:
                print("ERROR")
                city_state = address[:-1]
            updateCityStateFile(city_state_file, city_state)


if __name__ == '__main__':
    geopyParseCityState()