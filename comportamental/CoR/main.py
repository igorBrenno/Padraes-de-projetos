

# 1. Classe Base (Handler Abstrato)
class Handler:
    def __init__(self):
        # O próximo elo na cadeia, inicializado como None (nulo)
        self.proximo: Optional['Handler'] = None

    def adc_proximo(self, proximo: 'Handler') -> 'Handler':
        """
        Define o próximo handler na cadeia e retorna ele para encadeamento fácil.
        """
        # Note: 'self.proximo' recebe o novo objeto
        self.proximo = proximo
        # Retorna o objeto adicionado para permitir chamadas encadeadas
        return proximo

    def trata(self, requisicao: str) -> str:
        """
        Método padrão de tratamento. Se houver um próximo, passa a requisição adiante.
        """
        if self.proximo:
            return self.proximo.trata(requisicao)
        
        # Se for o último e a requisição chegou até aqui, retorna o resultado final
        return requisicao

# 2. Handlers Concretos
class ObjA(Handler):
    """
    Handler concreto que adiciona "ObjA" à requisição.
    """
    def trata(self, requisicao: str) -> str:
        # Adiciona a marcação deste objeto à requisição
        nova_requisicao = requisicao + "ObjA, "
        
        # Chama a implementação do handler base para passar adiante
        return super().trata(nova_requisicao)

class ObjB(Handler):
    """
    Handler concreto que adiciona "ObjB" à requisição.
    """
    def trata(self, requisicao: str) -> str:
        # Adiciona a marcação deste objeto à requisição
        nova_requisicao = requisicao + "ObjB, "
        
        # Chama a implementação do handler base para passar adiante
        return super().trata(nova_requisicao)

# 3. Código Cliente (Montagem e Execução)
print("--- Montando a Cadeia ---")

# Cria o primeiro objeto
objetoA = ObjA()

# Monta a cadeia de forma encadeada (ObjA -> ObjB -> ObjB -> ObjA)
# adc_proximo retorna o objeto recém-adicionado, permitindo a próxima chamada.
objetoA.adc_proximo(ObjB()).adc_proximo(ObjB()).adc_proximo(ObjA())

print("--- Executando a Requisição ---")
requisicao_inicial = "Inicial, "
resultado = objetoA.trata(requisicao_inicial)

print(f"\nRequisição Inicial: '{requisicao_inicial}'")
print(f"Resultado Final da Cadeia: '{resultado}'")