#!/usr/bin/env python
# encoding: utf-8

'''
SDK for KKBOX's Open/Partner API. https://docs.kkbox.codes
'''

from fetcher import *
from territory import *

class KKBOXAlbumFetcher(Fetcher):
    '''
    Get metadata and tracks of an album.
    
    See `https://docs.kkbox.codes/docs/albums`. 
    '''
    @property
    def access_token(self):
        return self.http.access_token

    def __init__(self, access_token):
        self.http = KKBOXHTTP(access_token)

    @assert_access_token
    def fetch_album(self, album_id, terr=KKBOXTerritory.TAIWAN):
        '''
        Fetches an album by given ID.

        :param album_id: the album ID.
        :type album_id: str
        :param terr: the current territory.
        :return: API response.
        :rtype: dict

        See `https://docs.kkbox.codes/docs/albums`.
        '''
        url = 'https://api.kkbox.com/v1.1/albums/%s' % album_id
        url += '?' + url_parse.urlencode({'territory': terr})
        return self.http._post_data(url, None, self.http._headers_with_access_token())

    @assert_access_token
    def fetch_tracks_in_album(self, album_id, terr=KKBOXTerritory.TAIWAN):
        '''
        Fetches tracks in an album by given ID.

        :param album_id: the album ID.
        :type album_id: str
        :param terr: the current territory.
        :return: API response.
        :rtype: dict

        See `https://docs.kkbox.codes/docs/albums-tracks`.
        '''
        url = 'https://api.kkbox.com/v1.1/albums/%s/tracks' % album_id
        url += '?' + url_parse.urlencode({'territory': terr})
        return self.http._post_data(url, None, self.http._headers_with_access_token())