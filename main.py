import sys
import json

import requests

# Use Like python githubber.py JASchilz
# my github name TinaBrownfield

if __name__ == "__main__":

    username = sys.argv[1]
    #username = 'TinaBrownfield'

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    #events = json.loads(response.content)
    #print(events[0]['created_at'])
    
    try:
        events = response.json()[0]
        print('Latest update from {}: '.format(username) + events['created_at'])
    except TypeError:
        print('No User by that name')
    


