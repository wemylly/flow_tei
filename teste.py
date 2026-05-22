print("Salário")
a = int(input('horas trabalhadas'))
b = int(input('valor da hora'))
s_atual = a * b
print(f"Seu salário antes da bonificação é {s_atual}")
salario_novo = ((1+a**1.5) / (b**2.5))*s_atual
print(f"Seu salário pós bonificação é {salario_novo:.2f}")