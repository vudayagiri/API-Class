#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name":"Z Beeble","species":"Betel"},{"name":"author dent","species":"human"},{'name':'Venkat','species':None}]
    

    mystr = yaml.dump(hitchhikers)
    print (mystr)
main()
