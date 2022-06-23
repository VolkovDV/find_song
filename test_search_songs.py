import pytest

from search_songs.search import search

@pytest.mark.parametrize(
    'request_text, expected_count', [('Deva Deo', 14), ('days', 13)]
)
def test_search_song(request_text, expected_count):
    song_list = search(request_text)

    assert len(song_list) == expected_count

@pytest.mark.parametrize(
    'request_text', [' ', 'FORJOSEPHHAYDNJOSEPHJOSEPHHAYDNJOSEPHJOSEPHHAYDNJOSEPHJOSEPHHAYDNJOSEPHJOSEPHHAYDNJOSEPH']
)
def test_search_song_empty(request_text):
    song_list = search(request_text)

    assert len(song_list) == 0


def test_search_song_no_arg():
    with pytest.raises(TypeError):
        search()
