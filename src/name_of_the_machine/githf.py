# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import sys
from os import environ, path
from github import Github, UnknownObjectException
from urllib3 import disable_warnings
import yaml

# The useless urllib3 warning is too maddening for an ordinary human being.
disable_warnings()


def connect_to_repo(github_token,
                   organization=None,
                   repository_name=None,
                   private=False):
    """
    Establish a connection with a GitHub repository.
    """

    gh = Github(github_token, verify=False)
    if organization:
        org = gh.get_organization(organization)
        try:
            repo = org.get_repo(f'{repository_name}')
        except UnknownObjectException:
            # print('Can not connect YOU to this repo in this organization')
            repo = None
        return repo
    else:
        user = gh.get_user()
        try:
            repo = user.get_repo(repository_name)
        except UnknownObjectException:
            # print('Can not connect YOU to this repo')
            repo = None
        return repo


def read_file(repository,
              file_path):
    """
    Read the contents of a file in a GitHub repository.
    """
    try:
        # Get the file if it exists
        ingested_file = repository.get_contents(file_path)
        content = ingested_file.decoded_content.decode("utf-8")

    except UnknownObjectException:
        # The file doesn't exist
        # print('The file does not exist')
        content = ''

    return content


def fetch_instructions(config):
    """Retrieve the system prompt from a private GitHub repo.
    Falls back to the local machina.yaml if GitHub is unreachable.
    Returns the 'name' of the Machine in dashed format.
    Returns the 'description' field from the YAML as the system prompt string.
    """
    try:
        repo = connect_to_repo(
            github_token=config.github_token,
            organization=config.machine_organization_name,
            repository_name=config.private_repo_with_text,
            private=True
        )
        raw_yaml = read_file(
            repository=repo,
            file_path=config.system_prompt_file
        )
    except Exception as e:
        print(f"Warning: could not fetch prompt from GitHub: {e}",
              file=sys.stderr)
        local_path = path.join(path.dirname(__file__), 'machina.yaml')
        with open(local_path, 'r') as f:
            raw_yaml = f.read()

    # Parse whatever you've gotten.
    parsed = yaml.safe_load(raw_yaml)
    name = parsed.get('name')
    config.name = name
    instructions = parsed.get('description', 'You are a helpful assistant.')
    config.instructions = instructions
    return name, instructions
