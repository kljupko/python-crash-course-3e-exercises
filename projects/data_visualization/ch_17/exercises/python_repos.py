import os

from dotenv import load_dotenv
import requests

def get_github_token():
    """Returns the GitHub token to access the API."""
    load_dotenv()
    return os.getenv("GITHUB_TOKEN")

def make_request(token):
    """Make an API call and return the response."""
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Authorization": f"token {token}"} if token else {}

    return requests.get(url, headers=headers)

def response_to_dict(response):
    """Return the response object as a dictionary."""
    return response.json()

def explore_response(response_dict):
    """Explore information about the repositories."""
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")

token = get_github_token()
response = make_request(token)
response_dict = response_to_dict(response)
explore_response(response_dict)
