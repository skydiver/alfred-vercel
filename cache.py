#!/usr/bin/python

import os
import datetime
import json

CACHE_PATH = './_cache/'

################################################################################
# CHECK IF A CACHE FILE IS EXPIRED
################################################################################
def expired_cache(path, time=3600):
    try:
        f = open(CACHE_PATH + path)
        data = f.read()
        f.close()
        mod_date = os.path.getmtime(CACHE_PATH + path)
        mod_timestamp = datetime.datetime.fromtimestamp(mod_date)
        return (mod_timestamp < datetime.datetime.now() - datetime.timedelta(seconds=time))
    except IOError:
        return True

################################################################################
# SAVE JSON OBJECT TO CACHE FILE
################################################################################
def store_cache(jsonStr, path):
    with open(CACHE_PATH + path, 'w') as outfile:
        json.dump(jsonStr, outfile, indent=2)

################################################################################
# READ JSON OBJECT FROM CACHE FILE
################################################################################
def read_cache(path):
    with open(CACHE_PATH + path) as json_file:
        return json.load(json_file)

################################################################################
# WIPE CACHE
################################################################################
def wipe_cache():
    files = os.listdir(CACHE_PATH)
    for f in files:
        if f.find('.json') > 0:
            os.remove(CACHE_PATH + f)
