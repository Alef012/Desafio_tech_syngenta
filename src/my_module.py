
from  src.classe_hotel import Hotel
hotel1=Hotel("Lakewood",3,110,80,90,80)
hotel2=Hotel("Bridgewood",4,160,110,60,50)  #criação dos objetos 
hotel3=Hotel("Ridgewood",5,220,100,150,40)
hoteis=[hotel1,hotel2,hotel3] #lista dos 3 hoteis pra ser percorrida no for

def get_cheapest_hotel(entrada):   #DO NOT change the function's name
    entrada=entrada.split(': ')
    tipo_cliente=entrada[0]    #separação da string entrada
    datas=entrada[1].split(', ')
    menor=hotel1
    for i in hoteis:
        i.preco=i.calcula_preco(datas,tipo_cliente)
        if i.preco< menor.preco:
            menor=i
        elif i.preco == menor.preco:
            if i.classificacao > menor.classificacao:
                menor =i
    
    return menor.nome

print(get_cheapest_hotel("Rewards: 10Mai2022, 11Mai2022, 12Mai2022, 13Mai2022, 14Mai2022, 15Mai2022"))
#resposta certa deve ser Ridgewood
print(get_cheapest_hotel("Regular: 10Mai2022, 11Mai2022, 12Mai2022, 13Mai2022, 14Mai2022, 15Mai2022"))
#resposta certa deve ser Lakewood