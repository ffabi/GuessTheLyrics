import os
from random import randrange

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = SPOTIPY_REDIRECT_URI

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(cache_path = ".cache", scope = scope))

first_results = sp.current_user_saved_tracks(limit = 1, offset = 0)
total = first_results["total"]


def get_random_track():
    hungarian = True
    main_artist = None
    track_name = None

    while hungarian:
        offset = randrange(total)
        results = sp.current_user_saved_tracks(limit = 1, offset = offset)

        main_artist = results['items'][0]["track"]["artists"][0]["name"]
        track_name = results['items'][0]["track"]["name"]

        hungarian = is_hungarian(main_artist, track_name)

    return main_artist, track_name


# todo find an api to determine nationality
def is_hungarian(main_artist, track_name):
    hungarian_characters = ["é", "á", "ó", "ö", "ő", "ú", "ü", "ű", "í"]

    if "Beyoncé" in main_artist:  # we love Beyoncé
        return False

    for char in hungarian_characters:
        if char in main_artist or char in track_name:
            return True

    return False


if __name__ == '__main__':
    # print(get_random_track())

    for i in range(20):
        main_artist, track_name = get_random_track()
        print(main_artist, track_name)
