def make_album(artist_name, album_title, music_number=None):
    """Cria um dicionário com informações de um álbum."""
    album = {'artist_name': artist_name, 'album_title': album_title}
    if music_number:
        album['music_number']= music_number
    return album

music_album = make_album('michael jackson', 'thriller')
print(music_album)

music_album = make_album('pink floyd', 'the dark side of the moon')
print(music_album)

music_album = make_album('ac/dc', 'back in black')
print(music_album)

music_album = make_album('nirvana', 'nevermind', 12)
print(music_album)