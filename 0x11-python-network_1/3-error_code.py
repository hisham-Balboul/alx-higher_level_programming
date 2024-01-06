#!/usr/bin/python3
"""send a web req with error handling"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
