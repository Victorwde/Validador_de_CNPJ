def d1(x):
    s = int(x[11])*2 + int(x[10])*3 + int(x[9])*4 + int(x[8])*5 + int(x[7])*6 + int(x[6])*7 + int(x[5])*8 + int(x[4])*9 + int(x[3])*2 + int(x[2])*3 + int(x[1])*4 + int(x[0])*5
    if s%11==0 or s%11==1:
        return 0
    else:
        return 11-(s%11)

def d2(x):
    s = int(x[12])*2 + int(x[11])*3 + int(x[10])*4 + int(x[9])*5 + int(x[8])*6 + int(x[7])*7 + int(x[6])*8 + int(x[5])*9 + int(x[4])*2 + int(x[3])*3 + int(x[2])*4 + int(x[1])*5 + int(x[0])*6
    if s%11==0 or s%11==1:
        return 0
    else:
        return 11-(s%11)

def VCNPJ(x):
    if d1(x) == int(x[12]):
        if d2(x) == int(x[13]):
            return 'Válido'
        else:
            return 'ùltimo inválido'
    else:
        return 'penúltimo inválido'



cnpj = input('Digite seu CNPJ: ')
print(VCNPJ(cnpj))
#cnpj = 59541264000103 teste