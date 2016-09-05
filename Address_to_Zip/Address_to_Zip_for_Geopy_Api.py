"""Python script that converts full line addresses (Geopy Style) to zipcodes
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
    United States House of Representatives, Washington, District of Columbia, 20540, United States of America
sample zipcode output:
    20540

"""


"""Finds a fragment containing a zipcode
@param line
    address line that contains zipcode
@return zip
    zipcode in address"""
def findZipFromFragment(address):
    line = address.split(',')
    zip = str(line[len(line) - 2]).lstrip().rstrip()
    return zip


"""Determines if zipcode is invalid
@param zip
    zipcode to test validity of
@return boolean
    Whether zip is longer than 7 characters"""
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
def geopyFindZipFromAddress():
    zipfile = open('zipcode.txt', 'a')
    with open("addresses.txt", 'r') as f:
        for address in f:
            zipcode = findZipFromFragment(address)
            if zipIsInvalid(zipcode):
                zipcode = 'error'
            updateZipFile(zipfile, zipcode)


if __name__ == '__main__':
    geopyFindZipFromAddress()