#!/usr/bin/python3

import uuid

ticket = uuid.uuid1()

try:
    print("Type the name of the config file to load onto the switch" ")
    configfile = input("Filename: ")
    with open(configfile, 'r') as configfileobj:
    switchconfig = configfileobj.read()
except Exception as err:
    x = f"There was an issue opening the file: {err}"
else: 
    x = f"The file {configfile} was succesffult loaded"
finally:
    with open ("try12.log,'w') as log:
        print(Writing results to log file")
        print(f"{ticket} - {x}", file=log)

    
