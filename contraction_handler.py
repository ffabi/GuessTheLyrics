import csv


def read_contractions():
    with open("shitty_contractions.csv") as file:
        shitty_contractions = file.read().splitlines()

    with open("replacable_contractions.csv") as file:
        reader = csv.reader(file)
        replacable_contractions = { rows[0]: rows[1] for rows in reader }

    return replacable_contractions, shitty_contractions


def replace_contractions(lyrics):
    replacable_contractions, shitty_contractions = read_contractions()

    for key in replacable_contractions.keys():
        lyrics = lyrics.replace(key, replacable_contractions[key])

    return lyrics, shitty_contractions

if __name__ == '__main__':
    read_contractions()