print('Primeira vez tentando fazer um estoque')

def linha():
    print('-'*50)

linha()
item1 = input('qual seu item?')
quantidade1 = int(input('quantas unidades?'))
linha()
item2= input('qual seu item?')
quantidade2 = int(input('quantas unidades?'))
linha()
item3 = input('qual seu item?')
quantidade3 = int(input('quantas unidades?'))
linha()
item4 = input('qual seu item?')
quantidade4 = int(input('quantas unidades?'))
linha()
item5 = input('qual seu item?')
quantidade5 =int(input('quantas unidades?'))
linha()

def allitens():
    print('seu estoque é:')
    print(item1, quantidade1)
    print(item2, quantidade2)
    print(item3, quantidade3)
    print(item4, quantidade4)
    print(item5, quantidade5)

allitens()