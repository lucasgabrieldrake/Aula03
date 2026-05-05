# Classificação por Pontos
     
pontos = int(input('Informe os pontos: '))

if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Agora você têm {total} pontos')

elif pontos >= 50:
    total = pontos + 5
    print(f'Bom desempenho. Você têm {total} pontos') 

elif pontos >= 30:
    total = pontos + 2
    print(f'Dá para o gasto. Você tem {total} pontos')        

else: 
    print(f'Treine mais. Pontuação {pontos} pontos')

print('Fim!')