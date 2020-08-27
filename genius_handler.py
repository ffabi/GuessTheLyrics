import os
import sys

import lyricsgenius
from spotify_handler import get_random_track

from secrets import genius_token

genius = lyricsgenius.Genius(genius_token)

def get_lyrics(author_name, track_name):
    sys.stdout = open(os.devnull, 'w')
    song = None
    while song is None:
        song = genius.search_song(track_name, author_name)
    sys.stdout = sys.__stdout__
    assert "spotify" not in song.artist.lower(), "The word 'spotify' occured in song.artist"
    return song.lyrics

if __name__ == '__main__':
    # print(get_lyrics("Break My Heart", "Dua Lipa"))
    print(get_lyrics("Electricity (with Dua Lipa)", "Silk City"))

    author_name, track_name = get_random_track()
    print(author_name, track_name)
    print(get_lyrics(author_name, track_name))
