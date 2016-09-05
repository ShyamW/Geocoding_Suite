"""Python script that converts FIPS to CBSA
@author
    Shyam Thiagarajan
@requires
    empty last line in fips_in.txt
    cbsa_out.txt is clear
@reads
    CBSA and FIP dictionary from CBSA.txt and FIPS.txt
@inputs
    FIPS from fips_in.txt
@outputs
    CBSA codes to cbsaout.txt

Do not change contents of CBSA.txt and FIPS.txt; they are dictionaries.
Use 5 Leading Zeros in Excel, will prepend zero to four digit zipcodes outputted by program. Ensure 1 blank line follows
input fips in fips_in.txt
"""


"""Collects CBSA from CBSA.txt
@param CBSA
    list to append CBSA
@updates CBSA
"""
def getCBSA(CBSA):
    with open("CBSA.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]  # remove \n
            CBSA.append(lines)


"""Collects FIPS from FIPS.txt
@param FIPS
    list to append FIPS
@updates FIPS"""
def getFips(FIPS):
    with open("FIPS.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]  # remove \n
            FIPS.append(lines)


"""Reads Fips to be processed
@param fips_in
    list to process fips
@updates fips_in"""
def getFipsIn(fips_in):
    with open("fips_in.txt", 'r') as f:
        for lines in f:
            lines = lines[:-1]  # remove \n
            fips_in.append(lines)


"""Converts fips to cbsa codes and writes result to file
@param fips_in
    list of fips to be converted
@param FIPS
    constant list of fips to match to CBSA
@param CBSA
    constant list of CBSA to match to FIPS"""
def convertToCBSA(fips_in, fips_to_cbsa):
    for fips in fips_in:
        cbsa_out = open('cbsa_out.txt', 'a')
        print(fips)
        if 'error' in fips:
            cbsa_out.write('nonefound' + '\n')
        elif fips in fips_to_cbsa.keys():
            cbsa = fips_to_cbsa[fips]
            cbsa_out.write(cbsa + '\n')
        else:
            cbsa_out.write('none' + '\n')


"""Ensures Dictionary is correct
@param CBSA
    list of CBSA in dictionary
@param FIPs
    list of FIPS in dictionary"""
def checkDictionary(CBSA, FIPS):
    if not len(CBSA) == len(FIPS):
        import sys
        sys.exit("SOMETHING IS WRONG WITH FIPS AND CBSA DICTIONARY\n CHECK THESE FILES!")


"""Main Method"""
def main():
    CBSA = []
    getCBSA(CBSA)
    FIPS = []
    getFips(FIPS)
    fips_in = []
    getFipsIn(fips_in)
    print(fips_in)
    checkDictionary(CBSA, FIPS)
    fips_to_cbsa = dict(zip(FIPS, CBSA))
    print(fips_to_cbsa)
    convertToCBSA(fips_in, fips_to_cbsa)
    print('!DONE!')


if __name__ == '__main__':
    main()