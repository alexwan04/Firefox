#!/usr/bin/env python

import requests
from pprint import pprint

def main():
    i = 1100
    myfile = open('outfile2.js', 'w')
    while i < 1181:
        text = 'https://bugzilla.mozilla.org/rest/bug/'
        new = list(text)         
        text = text + str(i)
        response = requests.get(text)
        bug = response.json()
        i = i + 1
        for j, v in bug.items():
            ky = j.encode('ascii','ignore')
            if type(v) is list:
                bug[ky] = [item.encode('ascii') for item in v]
            else:
                bug[ky] = v.encode('ascii','ignore')
        myfile.write("%s\n" % bug)
    myfile.close()
    
if __name__ == '__main__':
    main()