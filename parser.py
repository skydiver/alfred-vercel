#!/usr/bin/python

from cache import expired_cache, read_cache, store_cache
from vercel import get_user, get_teams, get_projects

################################################################################
# FETCH USER INFORMATION
################################################################################
def user_info():
    CACHE_FILE = 'tmp/_user.json'
    EXPIRED = expired_cache(CACHE_FILE)

    if (EXPIRED):
        data = read_cache(CACHE_FILE)
    else:
        data = get_user()
        store_cache(data, CACHE_FILE)

    return data['user']

################################################################################
# FETCH PROJECTS
################################################################################
def projects_list():
    CACHE_FILE = 'tmp/_projects.json'
    EXPIRED = expired_cache(CACHE_FILE)

    if (EXPIRED):
        data = read_cache(CACHE_FILE)
    else:
        data = get_projects()
        store_cache(data, CACHE_FILE)

    return data['projects']

################################################################################
# RETURN PROJECTS ALFRED OBJECT
################################################################################
def projects():
    user = user_info()
    projects = projects_list()

    result = []

    for project in projects:
        url = 'https://vercel.com/{}/{}'.format(user['username'], project['name'])
        result.append({
            'title': project['name'],
            'subtitle': url,
            'arg': url,
            'icon': {
                'path': 'icon.png'
            }
        })

    return result