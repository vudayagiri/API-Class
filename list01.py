#!/usr/bin/python3

def main():
    mylist = ['bert',55,'juniper','cisco',['bigip','meraki','dell']]
    print(f'My primary network provider are {mylist[2]} {mylist[3]}.')
    print(mylist[4][1])



if __name__ == "__main__":
    main()
