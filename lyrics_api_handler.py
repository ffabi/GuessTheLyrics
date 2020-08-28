import os
import re
import sys

import lyricsgenius
from spotify_api_handler import get_random_track

from secrets import genius_token

genius = lyricsgenius.Genius(genius_token)


def get_lyrics(main_artist, track_name, max_try = 10):
    exp = re.compile("\((.*?)\)")
    main_artist = exp.sub("", main_artist)
    track_name = track_name.replace("Radio Edit", "")

    sys.stdout = open(os.devnull, 'w')
    song = None
    tries = 0
    fail = False
    while song is None:
        song = genius.search_song(track_name, main_artist)
        if tries == max_try:
            fail = True
            print("No lyrics for {} - {}".format(main_artist, track_name))
        tries = tries + 1
    sys.stdout = sys.__stdout__
    assert "spotify" not in song.artist.lower(), "The word 'spotify' occured in song.artist: {}".format(song.artist)
    return song.lyrics, fail


if __name__ == '__main__':
    # print(get_lyrics("Break My Heart", "Dua Lipa"))
    print(get_lyrics("Electricity", "Silk City"))

    # author_name, track_name = get_random_track()
    # print(author_name, track_name)
    # print(get_lyrics(author_name, track_name))
