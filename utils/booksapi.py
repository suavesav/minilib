import os
import requests

from urllib.parse import quote_plus


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
        self.KEYWORDS = 'keywords'

    def _make_query(self, **kwargs):
        # account for keywords
        query = '?q='
        if self.KEYWORDS in kwargs.keys():
            query += quote_plus(kwargs[self.KEYWORDS])

        for k,v in kwargs.items():
            if k in self.api_mapping.keys():
                query += '+{}:{}'.format(
                    self.api_mapping[k],
                    quote_plus(v)
                )
        return query

    def get_book(self, endpoint='volumes', **kwargs):
        self.url = self.url_base + endpoint
        query = self._make_query(**kwargs)

        params = {}
        params['key'] = self.GBOOKS_API_KEY
        params['q'] = query

        response = requests.get(self.url, params=params)
        return response.json()
