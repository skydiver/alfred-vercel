#!/usr/bin/python

import os
import datetime
import json

################################################################################
# CHECK IF A CACHE FILE IS EXPIRED
################################################################################
def expired_cache(path, time=3600):
    try:
        f = open(path)
        data = f.read()
        f.close()
        mod_date = os.path.getmtime(path)
        mod_timestamp = datetime.datetime.fromtimestamp(mod_date)
        return (mod_timestamp < datetime.datetime.now() - datetime.timedelta(seconds=time))
    except IOError:
        return True

################################################################################
# SAVE JSON OBJECT TO CACHE FILE
################################################################################
def store_cache(jsonStr, path):
    with open(path, 'w') as outfile:
        json.dump(jsonStr, outfile, indent=2)

################################################################################
# READ JSON OBJECT FROM CACHE FILE
################################################################################
def read_cache(path):
    with open(path) as json_file:
        return json.load(json_file)