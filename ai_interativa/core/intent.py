class Intencao:
    def identificar(self, texto):
        texto = texto.lower()

        if any(p in texto for p in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            return "SAUDACAO"

        if any(p in texto for p in [
            "seu nome",
            "meu nome",
            "quero saber meu nome",
            "qual é seu nome",
            "quem é você"
        ]):
            return "IDENTIDADE"

        if any(p in texto for p in ["tudo bem", "como você está", "como vai"]):
            return "BEM_ESTADO"

        return "DESCONHECIDA"
