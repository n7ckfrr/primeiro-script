import random
secret_number = random.randint(1,10)

while True:
    palpite = int(input('Chuta um número de 1 a 10:'
    ''))

    if palpite == secret_number:
     print('correto')
     break
    else: 
     print('erro kk')