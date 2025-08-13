import os

from dotenv import load_dotenv
import requests
import plotly.express as px

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:c+sort:stars+stars:>10000"

headers = {"Authorization": f"token {token}"} if token else {}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Get the data.
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualize.
title = "Most Starred C Repos on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=names, y=stars, title=title, labels=labels)
fig.show()
