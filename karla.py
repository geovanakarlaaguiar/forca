#importa a biblioteca random,que ira gerar um número aléatoria.
import random

#criamos uma variável que vai conter o valor sorteado,com seguinte comando.
palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def recebeuPalavras():
    global palavras
    while True:
        recebeu = input('Qual palavra voce deseja sortear?')
        palavras.append(recebeu)
        if recebeu == '':
            break
    

def principal(): #O def define funções 
    """
    Função Princial do programa
    """
    print('F O R C A') #A função print() é utilizada para o programa exibir mensagens.
    
    recebeuPalavras()

    palavraSecreta = sortearPalavra() #recebe a função do sortear palavras.
    palpite = '' #o comando escolhido pelo jogador.
    desenhaJogo(palavraSecreta,palpite)

    while True: #Repete uma seqüência de comandos enquanto uma dada expressão booleana é avaliada como verdadeira.
        palpite = receberPalpite() #Variável palpite recebe a função receberPalpite.
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!') #A função print() é utilizada para o programa exibir mensagens.
            break #Quebra ou interrupção o fluxo natural do programa.
        if ganhouJogo(palavraSecreta): #IF é o comando condicional.
            print('Voce Ganhou!!!')
            break #Quebra ou interrupção o fluxo natural do programa.         
        
def perdeuJogo(): #definiçãó da função perdeuJogo.
    global FORCAIMG #torna global a variável, para dizer que ela é a mesma usada anterior.
    if len(letrasErradas) == len(FORCAIMG): #A função len retorna um valor tipo inteiro.
        return True #Forma de retornar dados quando a condição for verdadeira.
    else: #É execultado quando a condição if acima for falsa.
        return False #Foma de retornar dados quando a condição é falsa.
    
def ganhouJogo(palavraSecreta): #Aqui está definindo a função ganhouJogo.
    global letrasCertas #dizer que letrasCartas é a mesma que ja foi mensionada anteriormente.
    ganhou = True #para dizer se a o que diz na variável é verdade.
    for letra in palavraSecreta: #FOR gera um loop dentro de uma lista e o indica em qual lista ocorrerá.
        if letra not in letrasCertas: #letra não está dentro da lista letrasCartas.
            ganhou = False #para dizer se o que diz na variável é falso.
    return ganhou #Forma para retornar à variável ganhou.        
        


def receberPalpite(): #Aqui está definindo a função receberPalpite.
    
    palpite = input("Adivinhe uma letra: ") #Pedir para o jogador digitar uma letra.
    palpite = palpite.upper() #colocar palpite em maiúsculo.
    if len(palpite) != 1: #Dizer que se palpite tiver mais de uma letraimprimir na tela que é para digitar amis uma letra.
        print('Coloque um unica letra.') 
    elif palpite in letrasCertas or palpite in letrasErradas: #se a letra já tiver sido digitada,imprimir na tela que o jogador já disse essa letra.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": #se o jogador não digitar letras que estiver entre o A e o Z,pedir para ele digitar apenas letras.
        print('Por favor escolha apenas letras')
    else:
        return palpite #Retornar para variável palpite.
    
    
def desenhaJogo(palavraSecreta,palpite): #definir a função desenhaJogo.
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #imprimir na tela o que está dentro dessa variável.
    
     
    vazio = len(palavraSecreta)*'-' #colocar um _para cada letra da palavra sorteada.
    
    if palpite in palavraSecreta: #se a letra digitada estiver correta adicionar ela na variável letrasCartas.
        letrasCertas += palpite
    else:
        letrasErradas += palpite #se a letra digitada estiver errada adicionar ela na variável letrasErradas.

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) #Imprime na tela as letras que forem certas.
    print('Erros: ',letrasErradas) #Imprime na tela as letra que forem erradas.
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() #Retorna no random com afunção choice e escolhe uma palvra da lista da variável palavra.Upper deixa em maiúscolo.

    
principal()
