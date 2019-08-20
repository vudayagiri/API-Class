#!/usr/bin/python3

def main():
    while True:
        try:
            name = input("Enter the name of a file: ")
            with open(name,'w') as myfile:
                myfile.write("This Worked")
        except:
            print("Error with THAT file namw... trying again..")
        else:
            break
    print("Thanks for writing the file")

main()
