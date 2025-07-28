def make_album(artist, title, n_songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if n_songs:
        album["number of songs"] = n_songs
    return album
