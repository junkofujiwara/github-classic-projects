#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""list_repo.py"""
import logging
import settings
from util.utility import init, write_file
from util.github_query import list_projects

def main():
    """main"""
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s",
        handlers = [
            logging.FileHandler("projects.log"),
            logging.StreamHandler()
        ])
    github_org, github_repo, github_token, operation = init()
    endpoint = f'{settings.API_ENDPOINT}/repos/{github_org}/{github_repo}'
    if operation.casefold() == settings.OPERATION_LIST:
        logging.info("List repository projects (classic)")
        projects_count = write_file(
            list_projects(endpoint, github_token),
            settings.OUTPUT_FILE_PROJECTS)
        logging.info("Filed %s projects (%s)",
                     projects_count,
                     settings.OUTPUT_FILE_PROJECTS)

if __name__ == "__main__":
    main()
