#CORE
#---------------------------------------------------------------------------
#contest.py

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

#-----------------------------------------------------------------------
#decicsion.py
#Motor de Decisão(decision.py)
#Aqui nasce a inteligencia

#Ele decide o que responder , não como pesquisar.

#core/decision.py

def decidir_responda(texto,contexto,intencao):
    if intencao == "SALDACAO":
        return "Olá ! Estou aqi para conversar com você."
    
    if intencao == "IDENTIDADE":
        return "Ainda não tenho nome, mas sou uma IA em construção."
    
    if intencao == "BEM_ESTADO":
        return "Estou funcionando perfeitamente, e você?"
    
    if len(contexto) >= 2:
        return f"Entendi. Você disse antes: '{contexto[-2]}'"
    
    return "Não entendi totalmente , mas quero continuar aprendendo com você "

#---------------------------------------------------------------------------
#engine.py
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
#---------------------------------------------------------------------------
#intent.py
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
























