import os
import requests


class APIKeyMissingError(Exception):
    pass

class GBooks():

    def __init__(self):
        self.GBOOKS_API_KEY = os.environ.get('GBOOKS_API_KEY', None)
        if self.GBOOKS_API_KEY is None:
            raise APIKeyMissingError(
                "All methods require an API key. See "
                "https://developers.google.com/books/docs/v1/using#auth "
                "for how to retrieve an authentication token from "
                "the Google Books API"
            )

        self.url_base = 'https://www.googleapis.com/books/v1/'
        self.api_mapping = {
            'author': 'inauthor',
            'title': 'intitle',
            'isbn': 'isbn',
        }

    def get_book(self, endpoint='volumes', **kwargs):
        self.url = self.url_base + endpoint
        query = '?q='
        for k,v in kwargs.items():
            if k in self.api_mapping.keys():
                query += '{}:{}+'.format(self.api_mapping[k], v)
        print(query)

        session = requests.Session()
        session.params = {}
        session.params['key'] = self.GBOOKS_API_KEY
        session.params['q'] = query
        print(session.params)
        return session
        
        # response = session.get(self.url)
        # return response.json()
