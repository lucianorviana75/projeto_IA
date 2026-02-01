#ROUTER
#----------------------------------------------------------------
class Router:
    
    def route(self, user_input: dict) -> str:
        texto = user_input.get("texto", "").lower()
        
        if any(p in texto for p in ["oi", "olá","ola","bom dia", "boa noite"]):
            return "SAUDACAO"
        
        if any(p in texto for p in ["tchau", "sair", "encerrar"]):
            return "ENCERRAR"
        
        if "?" in texto:
            return "PERGUNTA"
        
        return "PADRAO"
        
        
