import json
import urllib
import urllib.error
import urllib.request

search_url = 'https://api.github.com/search/repositories'
params = urllib.parse.urlencode({
    'q': 'language:python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 3,
})
url = '%s?%s' % (search_url, params)
try:
    response = urllib.request.urlopen(url, timeout=10)
except urllib.error.HTTPError as e:
    print('HTTPError getting Github data: %s' % e)
    print(e.headers)
except urllib.error.URLError as e:
    print('URLError getting Gitub data: %s' % e)
else:
    content = response.read()
    data = json.loads(content)
    for repository in data['items']:
        print('{full_name}: \u2605 {stargazers_count}'.format(**repository))
