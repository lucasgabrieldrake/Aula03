#Pedir um número da compra, aplicar desconto, exibir valor com o desconto 16%, caso contrario exibir valor original sem desconto(caso não ultrapasse 250)

valor = float(input('Informe o valor: '))

if valor > 250:
   desconto = valor * 0.16
   total = valor - desconto
   print(f'Valor com desconto de 16% R${total}')

else:
   print(f'Valor sem desconto: R$ {valor}')
