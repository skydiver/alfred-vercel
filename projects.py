#!/usr/bin/python3

import os
import json

from parser import projects

# RETURN ALFRED OBJECT
data = json.dumps({ "items": projects() }, indent=2)
print(data)
