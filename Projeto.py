tarefas = []

def adicionarTarefas():
    tarefa = input('Digite a tarefa: ')
    tarefas.append({
        "id": len(tarefas) + 1,
        "Titulo": tarefa,
        "Status": False
    }) 
    with open('Tarefas.txt', 'w') as f: # Fazer a numeração dos arquivos
        f.write(f"{tarefa}\n")

def listarTarefas():
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'Tarefa {i}: {tarefa["id"]} {tarefa["Titulo"]} - {tarefa["Status"]}')

def concluirTarefa():
    listarTarefas()
    print('\n')

    try:
        numero = int(input('Digite o ID da tarefa que deseja concluir: '))
        if numero <= len(tarefas):
            tarefas[numero - 1]["Status"] = True
            print('\n')
            print('Tarefa Concluída')
        else:
            print('\n***ID inválido! Tente novamente.***')
    except ValueError:
        print('ID inválido, amigo.')
    
def removerTarefa():
    listarTarefas()
    numero = int(input('Digite o ID da tarefa que deseja remover: '))
    if numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print('\n')
    else:
        print('\n***ID iválido! Tente novamente.***')

def editarTarefa():
    listarTarefas()
    numero = int(input('Digite o ID da tarefa que deseja editar: '))
    if numero <= len(tarefas):
        edicao = str(input(f'Digite a alteração da tarefa {numero}'))
        tarefas[numero - 1]["Titulo"] = edicao
    else:
        print('\n***ID inválido! Tente novamente.***')

def sair():
    saida = (input('Aperte "Enter" para sair'))

while True:
    usrAcao = int(input(('\n1 - Adicionar tarefa\n2 - Listar tarefa\n3 - Concluir Tarefas\n4 - Remover tarefa \n5 - Sair\n\nDigite a opção de interesse: ')))
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
        concluirTarefa()
    elif usrAcao == 4:
        removerTarefa()
    elif usrAcao == 10:
        editarTarefa()
    elif usrAcao == 5:
        print('Finalizado')
        break  
