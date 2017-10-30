# !/usr/bin/env python

import requests
from pprint import pprint


def main():
    i = 1100
    myfile = open('outfile3.js', 'w')
    while i < 1115:
        text = 'https://bugzilla.mozilla.org/rest/bug/'
        new = list(text)
        text = text + str(i)
        response = requests.get(text)
        bug = response.json()
        i = i + 1
        myfile.write("%s\n" % bug)
    myfile.close()


if __name__ == '__main__':
    main()

#github