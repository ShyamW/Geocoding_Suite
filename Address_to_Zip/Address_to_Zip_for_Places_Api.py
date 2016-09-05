"""Python script that converts full line addresses (Google Places style) to zipcodes
@author
    Shyam Thiagarajan
@requires
    empty last line in addresses.txt
    zipcode.txt is clear
@inputs
    addresses from addresses.txt
@outputs
    zipcodes to zipcode.txt
sample input address:
    2115 US-92, Plant City, FL 33563, USA
sample output zipcode:
    33563
"""


"""Finds a fragment containing a zipcode
@param address
    address line that contains zipcode"""
def findZipFromFragment(address):
    try:
        address = address.split(',')
        state_and_zip = str(address[len(address) - 2])
        state_zip_array = state_and_zip.split(' ')
        zip = state_zip_array[2]
    except:
        zip = 'error'
    return zip
    

"""Determines if zipcode is invalid
@param zip
    zipcode to test validity of"""
def zipIsInvalid(zip):
    return len(zip) > 7


"""Updates content in zipfile
@param zipfile
    file to write zipcode to
@param zipcode
    zipcode to write, can be 'error'
@updates zipfile
"""
def updateZipFile(zipfile, zipcode):
    zipfile.write(zipcode + '\n')
    print(zipcode)
    
    
"""Main Method to convert addresses to zipcodes.
@requires
    zipcode_in.txt is empty
@updates
    content in zipcode_in.txt"""
def findZip():
    zipfile = open('zipcode.txt', 'a')
    with open("addresses.txt", 'r') as f:
        for address in f:
            zipcode = findZipFromFragment(address)
            if zipIsInvalid(zipcode):
                zipcode = 'error'
            updateZipFile(zipfile, zipcode)


if __name__ == '__main__':
    findZip()