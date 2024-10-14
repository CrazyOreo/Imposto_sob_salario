# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valor_salario = float(input("insira o valor de seu salario:\n"))

if valor_salario <= 900:
    print ("Você esta isento de descontos")

elif valor_salario > 900 and valor_salario < 1500:
    valor_desc = valor_salario
    valor_desc = valor_desc * 0.05
    valor_desc = valor_salario - valor_desc

    valor_desc_sala_IR = valor_desc * 0.05 #O 0.05 é a quantidade do desconto, que no caso é 5%, então fiz o valor incicial de desconto
    valor_desconto_IR = valor_desc - valor_desc_sala_IR #sabendo o valor do desconto de 5% tirei do valor salario total o desconto de 5%
    valor_somentedesc_IR = valor_desc - valor_desconto_IR #Aqui eu somente fiz o valor total menos o valor já com o desconto, apenas para ficar como o exercicio esta pedindo

    valor_desc_sala_INSS = valor_desc * 0.10 #Aqui se repete novamente, porem com os 10%, encontrando o valor do INSS que pede 10% do "VALOR TOTAL", então retirei apenas do valor total
    valor_desconto_INSS = valor_desconto_IR - valor_desc_sala_INSS #Aqui pego apenas o valor do INSS aplicado desconto e diminuo com o valor final que esta inserido no valor desconto IR pois o do IR era o valor total menos o valor IR.
    valor_somentedesc_INSS = valor_desconto_IR - valor_desconto_INSS #Aqui pego apenas o valor do desconto, que é o valor dos 10% (valor_desc_sala_INSS = valor_salario * 0.10)

    valor_desc_sala_FGTS = valor_desc * 0.11 #Daqui em diante, apenas se repete
    valor_desconto_FGTS = valor_desconto_INSS - valor_desc_sala_FGTS
    valor_somentedesc_FGTS = valor_desconto_INSS - valor_desconto_FGTS

    valor_totaldesc = valor_desc - valor_desconto_FGTS

    #Area grafica para apresentação do codigo
    print(f"Seu salario com desconto de 5%:{valor_desc}\n")
    print(f"(-) IR (5%): -{valor_somentedesc_IR}\n")
    print(f"(-) INSS ( 10%): -{valor_somentedesc_INSS}\n")
    print(f"FGTS (11%) : {valor_somentedesc_FGTS}\n")
    print(f"total de descontos: {valor_totaldesc}\n")
    print(f"salario liquido: {valor_desconto_INSS}\n")

elif valor_salario >= 1500 and valor_salario < 2500:
    valor_desc = valor_salario
    valor_desc = valor_desc * 0.10
    valor_desc = valor_salario - valor_desc

    valor_desc_sala_IR = valor_desc * 0.05 
    valor_desconto_IR = valor_desc - valor_desc_sala_IR 
    valor_somentedesc_IR = valor_desc - valor_desconto_IR 

    valor_desc_sala_INSS = valor_desc * 0.10 
    valor_desconto_INSS = valor_desconto_IR - valor_desc_sala_INSS 
    valor_somentedesc_INSS = valor_desconto_IR - valor_desconto_INSS 

    valor_desc_sala_FGTS = valor_desc * 0.11 
    valor_desconto_FGTS = valor_desconto_INSS - valor_desc_sala_FGTS
    valor_somentedesc_FGTS = valor_desconto_INSS - valor_desconto_FGTS

    valor_totaldesc = valor_desc - valor_desconto_FGTS

    #Area grafica para apresentação do codigo
    print(f"Seu salario com desconto de 5%:{valor_desc}\n")
    print(f"(-) IR (5%): -{valor_somentedesc_IR}\n")
    print(f"(-) INSS ( 10%): -{valor_somentedesc_INSS}\n")
    print(f"FGTS (11%) : {valor_somentedesc_FGTS}\n")
    print(f"total de descontos: {valor_totaldesc}\n")
    print(f"salario liquido: {valor_desconto_INSS}\n")

elif valor_salario > 2500:
    valor_desc = valor_salario
    valor_desc = valor_desc * 0.20
    valor_desc = valor_salario - valor_desc

    valor_desc_sala_IR = valor_desc * 0.05 
    valor_desconto_IR = valor_desc - valor_desc_sala_IR 
    valor_somentedesc_IR = valor_desc - valor_desconto_IR 

    valor_desc_sala_INSS = valor_desc * 0.10 
    valor_desconto_INSS = valor_desconto_IR - valor_desc_sala_INSS 
    valor_somentedesc_INSS = valor_desconto_IR - valor_desconto_INSS 

    valor_desc_sala_FGTS = valor_desc * 0.11 
    valor_desconto_FGTS = valor_desconto_INSS - valor_desc_sala_FGTS
    valor_somentedesc_FGTS = valor_desconto_INSS - valor_desconto_FGTS

    valor_totaldesc = valor_desc - valor_desconto_FGTS

    #Area grafica para apresentação do codigo
    print(f"Seu salario com desconto de 5%:{valor_desc}\n")
    print(f"(-) IR (5%): -{valor_somentedesc_IR}\n")
    print(f"(-) INSS ( 10%): -{valor_somentedesc_INSS}\n")
    print(f"FGTS (11%) : {valor_somentedesc_FGTS}\n")
    print(f"total de descontos: {valor_totaldesc}\n")
    print(f"salario liquido: {valor_desconto_INSS}\n")

#Ass:Crazy Oreo/Pedro Macegosa