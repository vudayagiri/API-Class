#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name":"Z Beeble","species":"Betel"},{"name":"author dent","species":"human"},{'name':'Venkat','species':None}]
    
    with open("galaxyguide.json","w") as zfile:
        json.dump(hitchhikers,zfile)
    myfile = json.dumps(hitchhikers)
    print(myfile)
main()
