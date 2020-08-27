import re

from contraction_handler import read_contractions


def clean_lyrics(lyrics):
    exp = re.compile("\[(.*?)\]")
    lyrics = exp.sub("", lyrics)
    exp = re.compile("\((.*?)\)")
    lyrics = exp.sub("", lyrics)
    lyrics = lyrics.lower()

    return lyrics

def replace_punctiations(lyrics):
    punctuations = [".", ",", ";", "!", "?", "-"]
    for p in punctuations:
        lyrics = lyrics.replace(p, " " + p)
    return lyrics, punctuations

def replace_contractions(lyrics):
    replacable_contractions, shitty_contractions = read_contractions()

    for key in replacable_contractions.keys():
        lyrics = lyrics.replace(key, replacable_contractions[key])

    return lyrics, shitty_contractions


def split_lyrics(lyrics):
    verses = []
    for verse in lyrics.split("\n\n"):
        new_verse = []
        for line in verse.split("\n"):
            new_verse.append(line.split(" "))
        verses.append(new_verse)



def preprocess_lyrics(lyrics):
    lyrics = clean_lyrics(lyrics)
    lyrics, punctuations = replace_punctiations(lyrics)
    lyrics, shitty_contractions = replace_contractions(lyrics)

    known_words = punctuations
    known_words.extend(shitty_contractions)

    lyrics = split_lyrics(lyrics)

    return lyrics, known_words