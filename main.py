from contraction_handler import read_contractions
import re
from genius_handler import get_lyrics
from spotify_handler import get_random_track

def replace_unknown(lyrics_words: list, known_words: list):
    hidden_lyrics_words = lyrics_words.copy()
    for i in range(len(lyrics_words)):
        word = hidden_lyrics_words[i]
        if word not in known_words:
            hidden_lyrics_words[i] = "_" * len(word)

    return hidden_lyrics_words

def clean_lyrics(lyrics):
    exp = re.compile("\[(.*?)\]")
    lyrics = exp.sub("", lyrics)
    exp = re.compile("\((.*?)\)")
    lyrics = exp.sub("", lyrics)
    lyrics = lyrics.lower()

    lyrics = lyrics.replace("\n", " ")

    return lyrics

def play():
    author_name, track_name = get_random_track()
    # print(author_name, " - ", track_name)
    lyrics = get_lyrics(author_name, track_name)
    # lyrics = get_lyrics("Dua Lipa", "Break My Heart")
    # lyrics = get_lyrics("Queen", "We Will Rock You")
    lyrics = clean_lyrics(lyrics)

    punctuations = [".", ",", ";", "!", "?", "-", '"']
    for p in punctuations:
        lyrics = lyrics.replace(p, " " + p + " ")

    replacable_contractions, shitty_contractions = read_contractions()

    for key in replacable_contractions.keys():
        lyrics = lyrics.replace(key.lower(), replacable_contractions[key].lower())

    lyrics.replace("'", "")
    lyrics_words = lyrics.split(" ")
    known_words = punctuations
    known_words.extend(shitty_contractions)

    hidden_lyrics_words = "_"

    try:
        while "_" in hidden_lyrics_words:
            new_input = input("Guess a word: ")
            if new_input == "give up":
                break
            for word in new_input.split(" "):
                known_words.append(word)
            hidden_lyrics_words = " ".join(replace_unknown(lyrics_words, known_words))
            print(hidden_lyrics_words)
    finally:
        print(lyrics)
        print(author_name, track_name)


if __name__ == '__main__':
    play()
