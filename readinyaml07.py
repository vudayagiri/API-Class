#!/usr/bin/python3

import yaml

def main():

    with open ("myyaml.yaml","r") as myyaml:
        myyamlfile = yaml.load(myyaml)

    print(type(myyamlfile))
    print(myyamlfile)

main()

