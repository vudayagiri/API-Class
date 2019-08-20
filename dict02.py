#!/usr/bin/python3
def main():
    webster = {"f1":"guest-wifi",'f2':"Solera","f3":"Sound physicians"}
    print(webster.get("f2"))
    print(webster['f2'])

    zlist =['westlake','southlake']
    webster['f4']= zlist
    print (webster['f4'][1])
main()
