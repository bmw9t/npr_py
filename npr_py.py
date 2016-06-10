import requests

URL = 'http://api.npr.org/query?'

PARAM = {
    'apiKey': 'MDI0NjkyODAwMDE0NjU1NzEzNTBjNzhkNw000',
    'id': '3002',
    'output': 'JSON',
    'fields': 'teaser'
}


def get_results(url=URL, params=PARAM):
    res = requests.get(url, params=PARAM)
    return res.json()['list']['story']


def add_or_update_params(key, value):
    """take a key and value and add them to the API call."""
    PARAM[key] = value


def delete_params(key):
    """delete the given param from the API call"""
    del(PARAM[key])


def main():
    res = get_results()
    for result in res:
        print('======')
        print(result)

    print(PARAM)
    add_or_update_params('test', 'a thing')
    print(PARAM)
    delete_params('test')
    print(PARAM)


if __name__ == '__main__':
    main()
