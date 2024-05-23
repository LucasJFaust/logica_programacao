"""
Exercício:
Peça o usuario para digitar seu nome
Peça o usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios"
"""
nome:str = input('Digite o seu nome: ')
idade:int = input('Digite a sua idade: ')

# Lembrando que strings vazias são avaliadas como falsy. Logo se o usuário não digitar nada a condição do if não será atendida
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')