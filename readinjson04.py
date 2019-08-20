#!/usr/bin/python3
import json

def main():


     with open("datacenter.json","r") as dc:
         dcshort = json.load(dc)

     print(dcshort["row1"])
main()
