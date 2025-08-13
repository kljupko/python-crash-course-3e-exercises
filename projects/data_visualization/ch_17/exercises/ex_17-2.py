from operator import itemgetter

import requests
import plotly.express as px

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print("Missing Key. Skipping article.")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# Prepare data for chart.
links, comments = [], []
for submission_dict in submission_dicts:
    # Generate link for each article.
    title = submission_dict['title']
    url = submission_dict['hn_link']
    link = f"<a href='{url}'>{title}</a>"
    links.append(link)
    
    comments.append(submission_dict['comments'])

# Visualize data.
title = "Most Active Discussions on HN"
labels = {'x': 'Tile', 'y': 'Comments'}
fig = px.bar(x=links, y=comments, title=title, labels=labels)
fig.show()
