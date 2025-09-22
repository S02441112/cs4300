import requests

def get_status_code(url):
    """Request and Return HTTP status of a url"""
    req = requests.get(url)
    return req.status_code

