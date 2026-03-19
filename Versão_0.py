tarefas = []

def adicionarTarefas():
    tarefa = input('Digite a tarefa: ')
    tarefas.append(tarefa)
    with open('Tarefas.txt', 'a') as f:
        f.write(f"{tarefas}\n")

def listarTarefas():
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'Tarefa {i}: {tarefa}')

def sair():
    saida = (input('Aperte "Enter" para sair'))

while True:
    usrAcao = int(input(('\n1 - Adicionar tarefa\n2 - Listar tarefa\n3 - Sair\n\nDigite a opção de interesse: ')))
    if usrAcao == 1:
        qtdTarefas = int(input('Quantas tarefas deseja inserir? '))
        if qtdTarefas > 0:
            for i in range(qtdTarefas):
                adicionarTarefas()
    elif usrAcao == 2:
        if tarefas == []:
            print('')
            print('Sem tarefas\n')
            sair()
        else:
            print('')
            listarTarefas()
            print('')
            sair()
    elif usrAcao == 3:
        print('Finalizado')
        break  
