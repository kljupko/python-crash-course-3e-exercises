def make_album(artist, title, n_songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if n_songs:
        album["number of songs"] = n_songs
    return album

while True:
    prompt = "(enter 'q' to cancel)"
    prompt += "\nArtist name: "
    artist = input(prompt)

    if artist.lower() == "q":
        break

    title = input("Album title: ")

    if title.lower() == "q":
        break

    album = make_album(artist, title)
    print(album)
    print()
