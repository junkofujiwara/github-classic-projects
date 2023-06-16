#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""github_query.py"""
import logging
import requests

def list_projects(endpoint, token):
    """list projects"""
    data = []
    next_page = True
    logging.info("Executing list repository projects (classic) query")
    url = f'{endpoint}/projects?state=all&per_page=100'
    while next_page:
        response = run_get(url, token)
        if response is None:
            return data
        result = response.json()
        for item in result:
            data.append([item["number"],
                item["name"],
                item["body"],
                item["state"]])
        next_page = 'next' in response.links.keys()
        if next_page:
            url = response.links['next']['url']
    return data

def run_get(url, token, throw_exception=False, exist_check=False):
    """run get (REST)"""
    try:
        headers = {"Authorization": f"bearer {token}"}
        request = requests.get(url,
          headers=headers)
        if exist_check and request.status_code == 404:
            return None
        request.raise_for_status()
        return request
    except (requests.exceptions.ConnectionError,
      requests.exceptions.Timeout,
      requests.exceptions.HTTPError) as exception:
        logging.error("Request failed. %s", exception)
        logging.debug("Failed Url: %s", url)
        if throw_exception:
            raise SystemExit(exception) from exception
    return None
