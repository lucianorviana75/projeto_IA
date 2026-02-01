#Execução principal(main.py)
#Agora IA ganha vida

#main.py
print("MAIN INICIADO")
from core.engine import EngineIA
#from input.user_input import EntradaUsuario

def main():
    ia = EngineIA()
    
    print("IA iniciada ,Digite algo (ou 'sair'):")
    
    while True:
        texto = input(">")
        
        if texto.lower() == "sair":
            print("IA encerrada. ")
            break
        
        
        resposta = ia.processar(texto.lower())
        print("IA:", resposta)
        
if __name__ == "__main__":
    main()    
