# EXERCÍCIO: Playlist com Métodos Especiais
# Objetivo: Aprender __str__, __len__, __add__

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []  # Lista vazia para as músicas

    def adicionar_musica(self, musica):
        """Adiciona uma música na playlist"""
        self.musicas.append(musica)
        print(f"✓ '{musica}' adicionada!")
    
    # __str__ define o que aparece ao fazer print(objeto)
    # Sem isso, print mostra algo feio como: <__main__.Playlist object at 0x...>
    def __str__(self):
        # join() junta a lista com quebra de linha
        lista_musicas = "\n".join(self.musicas)
        return f"🎵 Playlist: {self.nome}\n{lista_musicas}"
    
    # __len__ define o que len(objeto) retorna
    # Sem isso, len() não funcionaria em objetos
    def __len__(self):
        return len(self.musicas)
    
    # __add__ define o que acontece com o operador +
    # Permite somar duas playlists
    def __add__(self, other):
        nova = Playlist(f"{self.nome} + {other.nome}")
        nova.musicas = self.musicas + other.musicas
        return nova

# PASSO 2: Criar playlists e testar
print("═══ Criando Playlists ═══\n")
playlist1 = Playlist("Rock Legends")
playlist1.adicionar_musica("Bohemian Rhapsody - Queen")
playlist1.adicionar_musica("Stairway to Heaven - Led Zeppelin")
playlist1.adicionar_musica("Hotel California - Eagles")

print()
playlist2 = Playlist("Pop Hits")
playlist2.adicionar_musica("Shape of You - Ed Sheeran")
playlist2.adicionar_musica("Blinding Lights - The Weeknd")

# PASSO 3: Testar os métodos especiais
print("\n═══ Playlist 1 ═══")
print(playlist1)  # Chama __str__

print(f"\nNúmero de músicas: {len(playlist1)}")  # Chama __len__

print("\n═══ Somando Playlists ═══")
soma = playlist1 + playlist2  # Chama __add__
print(soma)

# COMO FUNCIONA:
# __str__: print(playlist) → mostra texto bonito
# __len__: len(playlist) → retorna quantidade de músicas
# __add__: playlist1 + playlist2 → cria playlist nova com tudo junto
