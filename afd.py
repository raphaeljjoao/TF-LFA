class Estado():
    def __init__(self, nome, transicoes):
        self.nome = nome
        self.transicoes = transicoes

class Transicao():
    def __init__(self, char, proximo, mensagem):
        self.char = char
        self.proximo = proximo
        self.mensagem = mensagem
    
    def escolhe_transicao(char, transicoes):
        for transicao in transicoes:
            if transicao.char == char:
                return transicao
        
        return None

