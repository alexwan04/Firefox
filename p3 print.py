#!/usr/bin/env python

import requests
from pprint import pprint

def main():
        response = requests.get('https://bugzilla.mozilla.org/rest/bug/1125')
        bug = response.json()
        pprint(bug)
    
if __name__ == '__main__':
    main()
