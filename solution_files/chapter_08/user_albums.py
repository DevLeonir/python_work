def make_album(artist_name, album_title):
    """Cria um dicionário com informações de um álbum."""
    album = {'artist_name': artist_name, 'album_title': album_title}
    return album

while True:
    print("\nDigite o nome do artista e o nome do album:")

    print("Digite 'q'para finalizar o programa.")
    name = input("Nome do artista: ")
    if name == 'q':
        print("\nPrograma finalizado!")
        break

    print("\nDigite 'q' para finalizar o programa.")
    title = input("Nome do album: ")
    if name == 'q':
        print("\nPrograma finalizado!")
        break

    music_album = make_album(name, title)
    print(music_album)
