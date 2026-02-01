#Memoria de curto prazo(context.py)
#core/context.py
class Contexto:
    def __init__(self, limite= 5):
        self.limite = limite
        self.historico = []
        
    def adicionar(self, mensagem):
        self.historico.append(mensagem)
        
        
        if len(self.historico) > self.limite:
            self.historico.pop(0) 
            
            
    def obter_contexto(self):
        return self.historico
    
    
    def limpar(self):
        self.historico = []           