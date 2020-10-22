from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render   # Added for this step
from GerenciamentoApp.models import Agendamento, Pessoa, PessoaAgendamento

def index(request):
    resultado = ''

    if request.method=='POST':
        if 'adicionar_btn' in request.POST:
            csv = open('AdicionarAgendamento.csv', 'r')

            num_pessoas = 0
            id_pessoas = []
            for i, line in enumerate(csv):
                if i == 0:
                    num_pessoas = int(line)
                elif i == 1:
                    id_pessoas = line.split(',')
                    if len(id_pessoas) != num_pessoas:
                        resultado = 'ERRO: a quantidade de IDs não corresponde ao número de pessoas no arquivo AdicionarAgendamento.csv'
                else:
                    datas = line.split(',')

            # TODO: Verificar no banco de dados e inserir o resultado do conflito na variavel conflita
            # SELECT * FROM agendamento JOIN pessoaagendamento ON agendamento.id = pessoaagendamento.agendamentoid WHERE datainicio = '2020-06-30 12:00:00' AND datafim = '2020-06-30 22:00:00' AND pessoaid in (1,5,8)
            # SELECT * FROM agendamento JOIN pessoaagendamento ON agendamento.id = pessoaagendamento.agendamentoid WHERE datainicio = datas[0] AND datafim = datas[1] AND pessoaid in (id_pessoas)

            conflita = True
            if conflita:
                resultado = 'Não é possível adicionar um novo agendamento, pois existe outro agendamento para o mesmo horário.'
            else:
                resultado = ""
                for id in id_pessoas:
                    resultado += "UPDATE agendamento SET datainicio = '{}' AND datafim = '{}' WHERE (SELECT pessoaid FROM pessoaagendamento WHERE agendamentoid = agendamento.id) = {}".format(datas[0], datas[1], id)
                
        elif 'atualizar_btn' in request.POST:
           csv = open('AtualizarAgendamento.csv', 'r')

           num_pessoas = 0
           for i, line in enumerate(csv):
               if i == 0:
                   id_agendamento = int(line)
               else:
                   datas = line.split(',')

            # TODO: Verificar no banco de dados e inserir o resultado do conflito na variavel conflita
            # SELECT * FROM agendamento WHERE datainicio = '2020-05-30 08:00:00' AND datafim = '2020-05-30 12:00:00'
            # SELECT * FROM agendamento WHERE datainicio = datas[0] AND datafim = datas[1]

           conflita = True
           if conflita:
               resultado = 'Não é possível atualizar o agendamento, pois existe outro agendamento para o mesmo horário.'
           else:
               resultado = "UPDATE agendamento SET datainicio = '{}' AND datafim = '{}' WHERE id = {}".format(datas[0], datas[1], id_agendamento)

        elif 'consultar_btn' in request.POST:
            mes = request.POST['mes']
            ano = request.POST['ano']
            # TODO: Consultar banco e imprimir resultado
            
            resultado = "SELECT local, datainicio, datafim FROM agendamento WHERE '{}' BETWEEN strftime('%m', datainicio) AND strftime('%m', datafim)AND '{}' BETWEEN strftime('%Y', datainicio) AND strftime('%Y', datafim)".format(mes, ano)

    return render(
        request,
        "GerenciamentoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {'resultado': resultado}
    )