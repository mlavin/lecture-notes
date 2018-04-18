import requests

search_url = 'https://api.github.com/search/repositories'
params = {
    'q': 'language:python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 3,
}
try:
    response = requests.get(search_url, params=params, timeout=10)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('HTTPError getting Github data: %s' % e)
except requests.exceptions.ConnectionError as e:
    print('ConnectionError getting Gitub data: %s' % e)
else:
    data = response.json()
    for repository in data['items']:
        print('{full_name}: \u2605 {stargazers_count}'.format(**repository))
