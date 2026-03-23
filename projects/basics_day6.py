nome_completo = str(input("Digite seu nome completo por favor: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite dua altua em forma númerica fracional(com ponto, exemplo: 2.32): "))
cidade = str(input("Digite a cidade em que nasceu: "))
sonho_profissional = str(input("Digite seu sonho profissional: "))
salario_esperado = float(input("Qual é o seu salario esperado?: "))


print(f"Seu nome completo é {nome_completo}, você tem {idade}, sua altura é {altura}, a cidade em que você nasceu é {cidade}")
print(f"Seu sonho profissional é: {sonho_profissional}")
if salario_esperado < 5000:
    print("Com esse salario já posso pagar o notebook")
else:
    print("Com esse salario ainda preciso estudar mais")