
from datetime import date
def transforma_mes(mes):
    #Função para retornar o numero do mes em inteiro para formatação da data
    ano=["Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun",
    "Jul",
    "Set",
    "Out",
    "Nov"
    "Dez"
    ]
    for i in range(11):
        if ano[i]==mes:
            return i+1

class Hotel: #Criação de um objeto hotel, para facilitar a criação de mais hotéis se preciso
    def __init__(self,nome,classificacao,taxa_semana,taxa_semana_fidelidade,taxa_fds,taxa_fds_fidelidade):
        self.nome =nome
        self.classificacao= classificacao
        self.t_semana = taxa_semana
        self.t_semana_fidelidade = taxa_semana_fidelidade
        self.t_fds= taxa_fds
        self.t_fds_fidelidade=taxa_fds_fidelidade
        self.preco =0
    
    def calcula_preco(self,datas,tipo_cliente): #Metodo que calcula o preço da hospadagem com as datas disponibilizadas
        preco=0
        if tipo_cliente == "Regular":
            for i in datas:
                mes=transforma_mes(i[2:5])
                dia_da_semana=date(int(i[5:9]),mes,int(i[0:2])).weekday()
                if dia_da_semana==5 or dia_da_semana== 6:
                    preco =preco+ self.t_fds
                else:
                    preco =preco+ self.t_semana
        elif tipo_cliente == "Rewards":
            for i in datas:
                mes=transforma_mes(i[2:5])
                dia_da_semana=date(int(i[5:9]),mes,int(i[0:2])).weekday()
                if dia_da_semana==5 or dia_da_semana==6:
                    preco = preco+self.t_fds_fidelidade
                else:
                    preco =preco+ self.t_semana_fidelidade
        return preco