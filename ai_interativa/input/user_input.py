class EntradaUsuario:
    def __init__(self, texto):
        self.texto = texto.strip().lower()
        
    def get_texto(self):
        return self.texto
