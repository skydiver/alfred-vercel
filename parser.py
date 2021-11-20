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
        data = get_user()
        store_cache(data, CACHE_FILE)
    else:
        data = read_cache(CACHE_FILE)

    return data['user']

################################################################################
# FETCH USER TEAMS
################################################################################
def user_teams():
    CACHE_FILE = 'tmp/_teams.json'
    EXPIRED = expired_cache(CACHE_FILE)

    if (EXPIRED):
        data = get_teams()
        store_cache(data, CACHE_FILE)
    else:
        data = read_cache(CACHE_FILE)

    return data['teams']

################################################################################
# FETCH PROJECTS
################################################################################
def projects_list():
    CACHE_FILE = 'tmp/_projects.json'
    EXPIRED = expired_cache(CACHE_FILE)

    if (EXPIRED):
        user = user_info()
        teams = user_teams()
        user_projects = get_projects()

        data = []

        for project in user_projects['projects']:
            data.append({
                'name': project['name'],
                'type': 'Personal Account',
                'team': user['username'],
                'url': 'https://vercel.com/{}/{}'.format(user['username'], project['name'])
            })

        for team in teams:
            team_projects = get_projects(team['id'])

            for project in team_projects['projects']:
                data.append({
                    'name': project['name'],
                    'type': 'Team',
                    'team': team['name'],
                    'url': 'https://vercel.com/{}/{}'.format(user['username'], project['name'])
                })

        store_cache(data, CACHE_FILE)

    else:
        data = read_cache(CACHE_FILE)

    return data

################################################################################
# RETURN PROJECTS ALFRED OBJECT
################################################################################
def projects():
    projects = projects_list()

    result = []

    for project in projects:
        result.append({
            'title': project['name'],
            'subtitle': 'Team: {}'.format(project['team']),
            'arg': project['url'],
            'icon': {
                'path': 'icon.png'
            }
        })

    return result