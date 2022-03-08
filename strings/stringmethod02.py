#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

defmain():
    """ Run-time code"""
    #create a small string
    lil string = "Alta3 Research offers classes on python coding"
    newlist = lilstring.split(" ") # this resturns a list
    print(newlist)

    #create a list of strings
    myiplist = ["192", "168", "0", "12"]
    #set singleip as the result of joining the list myiplist around the "."
    singleip = ".".join(myiplist) 
    # display singleip
    print(singleip) 

# call our main function 
main() 


