#!/usr/bin/python

import os
import requests

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

################################################################################
# MAKE API CALLS TO VERCEL
################################################################################
def make_request(url, params=None):
    API_URL = 'https://api.vercel.com/{}'.format(url)
    response = requests.get(API_URL,
        params,
        headers = {
            'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
        },
    )
    return response.json()

################################################################################
# FETCH USER INFORMATION
################################################################################
def get_user():
    response = make_request('www/user')
    return response

################################################################################
# FETCH USER TEAMS
################################################################################
def get_teams():
    response = make_request('v1/teams')
    return response

################################################################################
# FETCH PROJECTS
################################################################################
def get_projects():
    response = make_request('v8/projects', params={'limit': 100})
    return response