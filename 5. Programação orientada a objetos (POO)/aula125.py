# Mantendo estados (True ou False) dentro da classe (203)

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            return f'{self.nome} já está filmando.'

        self.filmando = True
        return f'{self.nome} está filmando ...'

    def parar_filmar(self):
        if not self.filmando:
            return f'{self.nome} não está mais filmando.'

        self.filmando = False
        return f'{self.nome} está parando de filmar ...'

    def tirar_foto(self):
        if self.filmando:
            return f'{self.nome} não pode tirar foto, pois está filmando.'

        return f'{self.nome} tirou uma foto.'

primeira = Camera('Sony')

print(primeira.filmar())
print(primeira.parar_filmar())
print(primeira.tirar_foto())
