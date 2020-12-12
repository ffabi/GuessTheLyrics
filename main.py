from lyrics_api_handler import get_lyrics
from lyrics_handler import replace_unknown, preprocess_lyrics, show_lyrics, valid_lyrics
from spotify_api_handler import get_random_track


def play():
    verses, author_name, track_name = None, None, None
    try:

        fail = True
        valid = False
        lyrics, author_name, track_name = "", "", ""
        while fail or not valid:
            author_name, track_name = get_random_track()
            # author_name, track_name = "Nuages", "Dreams"
            # author_name, track_name = "Dua Lipa", "Break My Heart"

            lyrics, fail = get_lyrics(author_name, track_name)
            valid = valid_lyrics(lyrics)

            if fail or not valid:
                print(author_name, track_name, " was not valid", len(lyrics))

        # print(author_name, " - ", track_name)

        verses, known_words = preprocess_lyrics(lyrics)

        replaced = True
        while replaced:
            new_input = input("Guess a word: ")
            if new_input == "give up":
                break
            if new_input == ":q":
                break
            for word in new_input.split(" "):
                word = word.lower()
                known_words.append(word)
                known_words.append(word + "s")
                known_words.append(word + "ing")
            hidden_verses, replaced = replace_unknown(verses, known_words)
            show_lyrics(hidden_verses)
    finally:
        show_lyrics(verses)
        print()
        print()
        print(author_name, track_name)


if __name__ == '__main__':
    play()
