import json
from typing import List, Union

from bs4 import BeautifulSoup
from requests import request

from search_songs.song import Song
from search_songs.vars import BASE_URL, SONGS_URL, SEARCH_URL


sep = '/'


def _parse(response_text: str) -> List[Union[Song, None]]:
    """
    Parse response text to list of songs

    :param response_text: response text from web
    :return: List of founded songs
    """
    soup = BeautifulSoup(response_text, 'html.parser')
    script = soup.find('body').find('script', id="__NEXT_DATA__")
    script_dict = json.loads(script.text)
    results = script_dict['props']['initialMobxState']['searchStore']['exercises']
    songs = []
    for result in results:
        songs.append(Song(result['artist'], result['title']))
    return songs


def search(
        text: str,
        *args,
        **kwargs
) -> List[Union[Song, None]]:
    """
    Searching songs by a name or an artist

    :param text: Song name or artist name
    :return: List of founded songs or empty list
    """
    response = request('GET', sep.join((BASE_URL, SONGS_URL, SEARCH_URL, text)))
    response.raise_for_status()
    song_list = _parse(response.text)
    return sorted(song_list)


