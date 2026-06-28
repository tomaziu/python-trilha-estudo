frases = ["  Olá Mundo  ", "Python é legal", "  code  "]

sem_espaço = [frase.strip() for frase in frases]
print(sem_espaço)

filtro_10caracteres = [frase for frase in sem_espaço if len(frase) > 10]
print(filtro_10caracteres)