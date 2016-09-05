"""Python script that converts zipcodes to CBSA.
@author
    Shyam Thiagarajan
@requires
    empty last line in zipcode_in.txt
    cbsaout.txt is clear
@reads
    zipcode and CBSA dictionary from ZIPS.txt and CBSA.txt
@inputs
    zipcodes from zipcode_in.txt
@outputs
    CBSA codes to cbsaout.txt

Do not change contents of CBSA.txt and ZIPS.txt; they are dictionaries.
"""


"""Verifies that each zip key has a cbsa value
@param ZIP
    list of zipcodes
@param CBA
    list of cbsa"""
def checkDictionary(ZIP, CBSA):
    if not len(ZIP) == len(CBSA):
        import sys
        sys.exit("SOMETHING IS WRONG WITH ZIP AND CBSA DICTIONARY\n CHECK THESE FILES!")


"""Reads zips from ZIPS.txt
@param ZIP
    list to store zip keys
@updates ZIP"""
def readZips(ZIP):
    with open("../Zip_to_CBSA/ZIPS.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]
            ZIP.append(lines)


"""Reads cbsa from CBSA.txt
@param CBSA
    list of cbsa values
@updates CBSA"""
def readCBSA(CBSA):
    with open("../Zip_to_CBSA/CBSA.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]
            CBSA.append(lines)


"""Reads zips and cbsa into a dictionary
@returns zip_to_CBSA
    zipcodes mapped to cbsa"""
def readZipCBSADictionary():
    ZIP=[]
    readZips(ZIP)
    CBSA = []
    readCBSA(CBSA)
    checkDictionary(ZIP,CBSA)
    zip_to_CBSA = dict(zip(ZIP, CBSA))
    return zip_to_CBSA


"""Reads zipcodes to process from zipcode_in.txt
@return zipcode
    list of zipcodes to process"""
def readZipcodeToProcess():
    zipcode = []
    with open("../Zip_to_CBSA/zipcode_in.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]
            zipcode.append(lines)
    return zipcode


"""Converts zipcodes to cbsa
@oaram zipcode
    list of zipcodes to convert
@param zip_to_CBSA
    dictionary of zipcodes : CBSA
@return cbsa
    list of mapped cbsa
    """
def convertToCbsa(zipcode, zip_to_CBSA):
    cbsa = []
    for zip in zipcode:
        if zip in zip_to_CBSA.keys():
            cbsa.append(zip_to_CBSA[zip])
        else:
            cbsa.append('NONE')
    return cbsa


"""Writes cbsa contents to cbsaout.txt
@oaram cbsa_out
    list of cbsa values to write to file
@updates contents in cbsaout.txt
"""
def writeCBSA(cbsa_out):
    out = open('../Zip_to_CBSA/cbsaout.txt', 'a')
    for cbsa in cbsa_out:
        out.write(cbsa + '\n')
        print(cbsa)


"""Main Method"""
def main():
    zip_to_CBSA = readZipCBSADictionary()
    zipcode = readZipcodeToProcess()
    cbsa_out = convertToCbsa(zipcode, zip_to_CBSA)
    writeCBSA(cbsa_out)


if __name__ == '__main__':
    main()

