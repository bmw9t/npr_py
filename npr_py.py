import requests
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords

URL = 'http://api.npr.org/query?'

PARAM = {
    'apiKey': 'MDI0NjkyODAwMDE0NjU1NzEzNTBjNzhkNw000',
    'id': '1105',
    'output': 'JSON',
    'fields': 'text'
}

# Functions for interacting with the API


def get_results(url=URL, params=PARAM):
    res = requests.get(url, params=PARAM)
    try:
        return res.json()['list']['story']
    except:
        print('problem with api query. none returned')
        print(res.url)


def add_or_update_params(key, value):
    """take a key and value and add them to the API call."""
    PARAM[key] = value


def delete_params(key):
    """delete the given param from the API call"""
    del(PARAM[key])


# Analysis functions


def get_text(results):
    """takes some API results and returns a big
    string of all the text in it."""
    api_text_results = []
    for result in results:
        try:
            paragraphs = result['text']['paragraph']
        except:
            print(result)
        for paragraph in paragraphs:
            try:
                if '$text' in paragraph:
                    api_text_results.append(paragraph['$text'])
            except:
                print('==========')
                print(paragraph)
                print(paragraph['num'])
    return ' '.join(api_text_results)


def tokenize(text):
    """take the test lump and tokenize it."""
    punctuation = [',', '-', '.', '!', "\"", '\'' ':', ';', '?', '...',
                   '\'\'', '``', ']', '[', '—', ':']
    stopwords_list = stopwords.words('english') + punctuation
    return list(w.lower() for w in word_tokenize(text) if
                w.lower() not in stopwords_list)


def the_whole_thing():
    res = get_results()
    text = get_text(res)
    fd = FreqDist(tokenize(text))
    return fd.most_common(50)


def main():
    res = get_results()
    print(the_whole_thing())


if __name__ == '__main__':
    main()
