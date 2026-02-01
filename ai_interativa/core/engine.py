#Engine da IA (engine.py)
#Este e o cerebro central.

#core/engine.py


from core.context import Contexto
from core.decision import decidir_responda
from router.router import Router
from core.intent import Intencao


class EngineIA:
    
    def __init__(self):
        self.contexto = Contexto()
        self.router = Router()
        self.intencao = Intencao()
        
    def _entrada_tecnica(self, texto):
        return (
        "python.exe" in texto
        or ".py" in texto
        or texto.startswith("c:/")
        or texto.startswith("C:/")
    )    
    def processar(self, texto_usuario):
        #guarda no contexto
        
        self.contexto.adicionar(texto_usuario)
        Contexto_atual = self.contexto.obter_contexto()
        
        
        # router decide o caminho
        rota = self.router.route({"texto": texto_usuario})
        
        if  rota == "SAUDACAO":
            return "Olá ! Como posso te ajudar ?"
        
        if rota == "ENCERRAR":
            return "Até mais! Encerrando a conversa." 
        
        intencao = self.intencao.identificar(texto_usuario)
        
        
        # reta PADRAO OU PERGUNTA
        resposta =  decidir_responda(texto_usuario,Contexto_atual,intencao)
        return resposta
          