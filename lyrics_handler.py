import re
import copy
from contraction_handler import read_contractions
from lyrics_api_handler import get_lyrics


def clean_lyrics(lyrics):
    exp = re.compile("\[(.*?)\]")
    lyrics = exp.sub("", lyrics)
    exp = re.compile("\((.*?)\)")
    lyrics = exp.sub("", lyrics)
    # lyrics = lyrics.lower()

    return lyrics


def replace_punctiations(lyrics):
    punctuations = [".", ",", ";", "!", "?", "-", '"']
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
    for verse in lyrics.split("\n\n\n"):
        new_verse = []
        for line in verse.split("\n"):
            if line == "\n" or line == "":
                continue
            words = line.replace("\n", "").split(" ")
            new_verse.append([word for word in words if word != ""])
        verses.append(new_verse)

    return verses


def valid_lyrics(lyrics):
    if not 50 < len(lyrics) < 3000:
        return False
    return True


def preprocess_lyrics(lyrics):
    lyrics = clean_lyrics(lyrics)
    lyrics, punctuations = replace_punctiations(lyrics)
    lyrics, shitty_contractions = replace_contractions(lyrics)
    # lyrics = lyrics.replace("'", " " + "'" + " ") # ain't
    known_words = punctuations
    known_words.extend(shitty_contractions)
    known_words.extend(["'"])

    verses = split_lyrics(lyrics)

    return verses, known_words


def replace_unknown(verses: list, known_words: list):
    replaced = False
    hidden_verses = copy.deepcopy(verses)
    for i in range(len(verses)):
        for j in range(len(verses[i])):
            for k in range(len(verses[i][j])):
                word = hidden_verses[i][j][k]
                if word.lower() not in known_words:
                    hidden_verses[i][j][k] = "_" * len(word)
                    replaced = True

    return hidden_verses, replaced


def show_lyrics(verses):
    for verse in verses:
        for line in verse:
            print(" ".join(line))
        print()


if __name__ == '__main__':
    lyrics = get_lyrics("Dua Lipa", "Break My Heart")
    verses, known_words = preprocess_lyrics(lyrics)
    show_lyrics(verses)
