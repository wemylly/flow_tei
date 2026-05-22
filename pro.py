print("*"*30)
print('Taxa Metabolica Basal')
print("*"*30)
W = float(input('Qual seu peso (em Kg)?'))
H = float(input('Qual seu altura (em m)?'))
A = float(input('Qual seu idade?'))

BMR = 10 * W + 6.25 * H - 5 * A + 5

print(f'Sua Taxa Metabolica Basal é: {BMR:.1f}')

