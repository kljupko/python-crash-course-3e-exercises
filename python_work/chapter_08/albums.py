def make_album(artist, title, n_songs=None):
    """
    Create a dictionary containing album information.

    Args:
        artist (str): The name of the artist.
        title (str): The title of the album.
        n_songs (int, optional): The number of songs on the album.

    Returns:
        dict: A dictionary with album details.
    """
    album = {"artist": artist.title(), "title": title.title()}
    if n_songs:
        album["number of songs"] = n_songs
    return album

album_1 = make_album("michael jackson", "thriller")
album_2 = make_album("judas priest", "firepower")
album_3 = make_album("mgla", "exercises in futility")

print(album_1)
print(album_2)
print(album_3)

album_4 = make_album("porcupine tree", "deadwing", 9)

print(album_4)
