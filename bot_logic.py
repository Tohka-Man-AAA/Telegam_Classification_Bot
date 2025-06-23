import random,time
def gen_pass(pass_length):
    elements = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    #a = int(input('Введите нужную длину пароля:'))
    #while a<7:
        #print('Вы указали недостаточную длину, попробуйте еще раз!')
        #a = int(input('Введите нужную длину пароля:'))
        #time.sleep(1)
    password = ''
    while not(('1'in password) or ('2' in password) or ('3'in password) or ('4' in password) or ('5' in password) or ('6' in password) or ('7' in password) or ('8' in password) or ('9' in password) or ('0' in password)) or not(('?' in password) or ('/' in password) or ('#' in password) or ('$' in password) or ('&' in password) or ('!' in password) or ('*' in password) or ('-' in password) or ('+' in password) or ('=' in password) or ('@' in password)):
        password = ''
        for i in range(pass_length):
            password += random.choice(elements)
        time.sleep(1)
    return password
def coin():
    variants=['Орел','Решка']
    attempt=random.choice(variants)
    return attempt