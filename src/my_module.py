import re
class Hotel:
    def __init__(self,nome,classificacao,taxa_semana,taxa_semana_fidelidade,taxa_fds,taxa_fds_fidelidade):
        self.nome =nome
        self.classificacao= classificacao
        self.t_semana = taxa_semana
        self.t_semana_fidelidade = taxa_semana_fidelidade
        self.t_fds= taxa_fds
        self.t_fds_fidelidade=taxa_fds_fidelidade
        self.preco =0
    
    def calcula_preco(self,datas,tipo_cliente):
        preco=0
        if tipo_cliente == "Regular":
            for i in datas:
                if i[9:]=="(sat)" or i[9:]=="(sun)":
                    preco =preco+ self.t_fds
                else:
                    preco =preco+ self.t_semana
        elif tipo_cliente == "Reward":
            for i in datas:
                if i[9:]=="(sat)" or i[9:]=="(sun)":
                    preco = preco+self.t_fds_fidelidade
                else:
                    preco =preco+ self.t_semana_fidelidade
        return preco



hotel1=Hotel("Lakewood",3,110,80,90,80)
hotel2=Hotel("Bridgewood",4,160,110,60,50)
hotel3=Hotel("Ridgewood",5,220,100,150,40)
hoteis=[hotel1,hotel2,hotel3]

def get_cheapest_hotel(entrada):   #DO NOT change the function's name
    entrada=entrada.split(': ')
    tipo_cliente=entrada[0]
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

get_cheapest_hotel(input())