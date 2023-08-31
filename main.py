import csv
import time
from afd import Estado, Transicao

# Mensagens

SELECAO_COMIDAS = 'Seleção de comidas.'
PAGAMENTO = 'Escolha do método de pagamento.'
APROVADO = 'Pagamento aprovado.'
RECUSADO = 'Pagamento recusado.'

def mensagem_carrinho(item):
    return f'Adiciona {item} ao carrinho.'

# Autômato

ESTADOS = [
    Estado(
        'q0',
        [Transicao('a', 'q1', 'Aplicativo aberto com sucesso.')]
    ),
    Estado(
        'q1',
        [
            Transicao('x', 'q2', 'Restaurante X selecionado.'),
            Transicao('y', 'q3', 'Restaurante Y selecionado.'),
            Transicao('z', 'q4', 'Restaurante Z selecionado.')
        ]
    ),
    Estado(
        'q2',
        [Transicao('m', 'q5', SELECAO_COMIDAS)]
    ),
    Estado(
        'q3',
        [Transicao('m', 'q5', SELECAO_COMIDAS)]
    ),
    Estado(
        'q4',
        [
            Transicao('m', 'q5', SELECAO_COMIDAS),
            Transicao('k', 'q6', 'Brinde do restaurante Z aceito.')
        ]
    ),
    Estado(
        'q5',
        [
            Transicao('p', 'q7', mensagem_carrinho('pizza')),
            Transicao('b', 'q7', mensagem_carrinho('batata frita')),
            Transicao('h', 'q7', mensagem_carrinho('hambúrguer'))
        ]
    ),
    Estado(
        'q6',
        [Transicao('m', 'q5', SELECAO_COMIDAS)]
    ),
    Estado(
        'q7',
        [
            Transicao('p', 'q7', mensagem_carrinho('pizza')),
            Transicao('b', 'q7', mensagem_carrinho('batata frita')),
            Transicao('h', 'q7', mensagem_carrinho('hambúrguer')),
            Transicao('?', 'q8', 'Seleção de bebidas.')
        ]
    ),
    Estado(
        'q8',
        [
            Transicao('r', 'q8', mensagem_carrinho('refrigerante')),
            Transicao('g', 'q8', mensagem_carrinho('água')),
            Transicao('c', 'q8', mensagem_carrinho('cerveja')),
            Transicao('e', 'q9', 'Informa endereço.')
        ]
    ),
    Estado(
        'q9',
        [
            Transicao('u', 'q10', 'Informa cupom de desconto.'),
            Transicao('$', 'q11', PAGAMENTO)
        ]
    ),
    Estado(
        'q10',
        [Transicao('$', 'q11', PAGAMENTO)]
    ),
    Estado(
        'q11',
        [
            Transicao('t', 'q12', 'Pagamento no PIX.'),
            Transicao('d', 'q13', 'Pagamento em dinheiro.'),
            Transicao('i', 'q14', 'Pagamento no cartão.')
        ],
        
    ),
    Estado(
        'q12',
        [
            Transicao('s', 'q15', APROVADO),
            Transicao('n', 'q16', RECUSADO)
        ]
    ),
    Estado(
        'q13',
        [
            Transicao('s', 'q15', APROVADO),
            Transicao('n', 'q16', RECUSADO)
        ]
    ),
    Estado(
        'q14',
        [
            Transicao('s', 'q15', APROVADO),
            Transicao('n', 'q16', RECUSADO)
        ]
    ),
    Estado(
        'q15',
        [
            Transicao('#', 'q18', 'Pedido finalizado.'),
            Transicao('@', 'q17', 'Pedido cancelado.')
        ]
    ),
    Estado('q16', []),
    Estado('q17', []),
    Estado('q18', [])
]

ESTADO_INICIAL = 0
ESTADO_FINAL = len(ESTADOS) - 1

# Funções

def processa_entrada_interativa():
    estado_atual = ESTADO_INICIAL
    palavra = ''
    while True:
        char = input('Insira a operação (letra): ')
        if char == '':
            break

        palavra = palavra + char

        estado = ESTADOS[estado_atual]
        transicao = Transicao.escolhe_transicao(char, estado.transicoes)

        if transicao:
            estado_atual = int(transicao.proximo.replace('q', ''))
            print(transicao.mensagem, '\n')
        else:
            print('Transição não encontrada. Parada por indeterminação.\n')
            break
        
        if estado_atual == ESTADO_FINAL:
            break
    
    if estado_atual == ESTADO_FINAL:
        print(f'Palavra {palavra} reconhecida.')
    else:
        print('Palavra terminou em um estado não final. Palavra rejeitada.')

def processa_entrada_inteira(entrada):

    try:
        palavra = ''.join(entrada)
    except:
        palavra = entrada

    estado_atual = ESTADO_INICIAL
    for char in entrada:
        time.sleep(650 / 1000)
        estado = ESTADOS[estado_atual]

        transicao = Transicao.escolhe_transicao(char, estado.transicoes)
        if transicao:
            estado_atual = int(transicao.proximo.replace('q', ''))
            print(char)
            print(transicao.mensagem, '\n')
        else:
            print(char)
            print('Transição não encontrada. Parada por indeterminação.\n')
            break

    time.sleep(650 / 1000)
    if estado_atual == ESTADO_FINAL:
        print(f'Palavra {palavra} reconhecida.')
    else:
        print('Palavra terminou em um estado não final. Palavra rejeitada.')

def palavra_csv(nome):
    with open(f'{nome}.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            entrada = row
    return entrada


# Execução

print('===================================================')
print("""             _ ______              _ 
            (_)  ____|            | |
             _| |__ ___   ___   __| |
            | |  __/ _ \ / _ \ / _` |
            | | | | (_) | (_) | (_| |
            |_|_|  \___/ \___/ \__,_|          
""")
print('===================================================')
print('Trabalho Final - Linguagens Formais E Autômatos N')
print('Alunos:')
print('    - André Vitor Gabriel')
print('    - Emerson do Nascimento Rodrigues')
print('    - João Raphael Fontoura Dorneles')
print('===================================================\n')

while True:
    print('\nModos de execução')
    print('1 - Interação real')
    print('2 - Interação automática (arquivo csv)')
    print('3 - Interação automática (teclado)')
    print('4 - Encerrar\n')
    modo_execucao = input('Escolha o modo de execução: ')

    print()
    match modo_execucao:
        case '1':
            processa_entrada_interativa()
        case '2':
            nome_arquivo = input('Insira o nome do arquivo (sem a extensão): ')

            try:
                entrada = palavra_csv(nome_arquivo)
            except:
                print(f'Arquivo {nome_arquivo}.csv não encontrado.')
                continue

            palavra = ''.join(entrada)
            print(f'\nPalavra lida do arquivo: {palavra}\n')
            processa_entrada_inteira(entrada)
        case '3':
            entrada = input('Insira a sequência de operações (palavra): ')
            print()
            processa_entrada_inteira(entrada)
        case '4':
            print('Encerrando.\n')
            break
        case _:
            print(f'Modo de execução \'{modo_execucao}\' inválido.')
            continue
