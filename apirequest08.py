#!/usr/bin/python3

import requests
from pprint import pprint


def main():

    r = requests.get("https://anapioficeandfire.com/api")
    pprint(r.json())


    house = requests.get("https://anapioficeandfire.com/api/houses")
    #pprint(house.json())
    sworn = (house.json())
    for i in sworn:
        print(i["swornMembers"])

main()
