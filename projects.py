#!/usr/bin/python3

import sys
import os
import json

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', None)

if ACCESS_TOKEN is None or len(ACCESS_TOKEN) == 0:
    data = [{
        'title': 'Access Token not found!',
        'subtitle': 'You need to get a Vercel API token. Please, read workflow instructions.',
        'arg': 'github.com/skydiver/alfred-vercel',
        'icon': {
            'path': 'icon-warning.png'
        }
    }]
else:
    # GET PROJECTS LIST
    from parser import projects
    SEARCH = sys.argv[1] if len(sys.argv) >= 2 else None
    data = projects(search=SEARCH)

# RETURN ALFRED OBJECT
data = json.dumps({ "items": data }, indent=2)
print(data)
