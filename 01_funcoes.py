# Função que calcual o IMC da pessoa
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 85
# a = 1.72
# imc = calc_imc(p, a)

# print(imc)

print(calc_imc(85, 1.72))