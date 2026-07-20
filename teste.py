valor_da_parcela = input(f"Digite o valor da parcela: ")
juros_a_pagar = input(f"Digite o valor do juros: ")
gca = input(f"Digite o valor do GCA: ")
iof = input(f"Digite o valor do IOF: ")
comisao_a_aplicar = 0.6
valor_total = 0
valor_total += sum({valor_da_parcela}, {juros_a_pagar}, {gca}, {iof})


print(f"Valor total a ser pago: R$: {valor_total}.")