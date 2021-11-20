#!/usr/bin/python3

import sys
import os
import json

from parser import projects

# GET PROJECTS LIST
SEARCH = sys.argv[1] if len(sys.argv) >= 2 else None
projects = projects(search=SEARCH)

# RETURN ALFRED OBJECT
data = json.dumps({ "items": projects }, indent=2)
print(data)
