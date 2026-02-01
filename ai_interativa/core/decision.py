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