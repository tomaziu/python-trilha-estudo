class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
    
    def __str__(self):
        return f"Playlist: {self.nome}\nMúsicas:\n{'\n'.join(self.musicas)}"
    
    def __len__(self):
        return len(self.musicas)
    
    def __add__(self, other):
        nova = Playlist(f"{self.nome} + {other.nome}")
        nova.musicas = self.musicas + other.musicas
        return nova

playlist1 = Playlist("Minha Playlist")
playlist1.adicionar_musica("Duvet - Bôa")
playlist1.adicionar_musica("Creep - Radiohead")

playlist2 = Playlist("Outra Playlist")
playlist2.adicionar_musica("Smells Like Teen Spirit - Nirvana")
playlist2.adicionar_musica("Wonderwall - Oasis")

print(playlist1)
print(f"Número de músicas na playlist: {len(playlist1)}")

soma_playlists = playlist1 + playlist2
print(soma_playlists)