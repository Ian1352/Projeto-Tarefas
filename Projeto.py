import json

def mostrarTarefas():
    try:    
        with open("tarefas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

tarefas = mostrarTarefas()

def adicionarTarefas():
    tarefa = input('Digite a tarefa: ')
    tarefas.append({
        "id": len(tarefas) + 1,
        "Titulo": tarefa,
        "Status": False
    })

    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f, indent=2)

def listarTarefas():
    for tarefa in tarefas:
        texto_status = 'Concluúdo' if tarefa["Status"] else 'Pendente'
        print(f'ID - {tarefa["id"]} - {tarefa["Titulo"]} - {texto_status}')

def filtrarTarefas():
    print('Deseja filtrar as tarefas?')
    tarefasfiltro = int(input('1 - Mostrar tudo \n2 - Mostrar pendentes \n3 - Mostrar concluídas \n\nOpção escolhida: '))
    if(tarefasfiltro == 1):
        for tarefa in tarefas:
            status_texto = 'Concluído' if tarefa["Status"] else 'Pendente'      #Percorre todos os itens da lista "tarefas" marcando alternando de True e False para "Concluído" e "Pendente"
            print(f'ID: {tarefa["id"]} - {tarefa["Titulo"]} - {status_texto}')

    elif (tarefasfiltro == 2):
        encontrou = False
        for tarefa in tarefas:
            if (tarefa["Status"] == False):
                encontrou = True
                status_texto = 'Pendente'
                print(f'ID: {tarefa["id"]} - {tarefa["Titulo"]} - {status_texto}')
        if not encontrou:
            print('\nSem tarefas pendentes')

    elif(tarefasfiltro == 3):
        encontrou = False
        for tarefa in tarefas:
            if (tarefa["Status"] == True):
                encontrou = True
                status_texto = 'Concluído'
                print(f'ID - {tarefa["id"]} - {tarefa["Titulo"]} - {status_texto}')
        if not encontrou:
            print('Sem tarefas concluídas')

def salvarTarefa():
    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f, indent= 2)

def concluirTarefa():
    listarTarefas()
    mostrarTarefas()
    print('\n')

    try:
        opcao = int(input('Digite o ID da tarefa que deseja marcar como concluída: '))
        if opcao <= len(tarefas):
            tarefas[opcao - 1]["Status"] = True

            salvarTarefa()
            print('\n')
            print('Tarefa Concluída')

        else:
            print('\n***ID inválido! Tente novamente.***')
    except ValueError:
        print('ID inválido, tente novamente.')
    
def removerTarefa():
    global tarefas
    mostrarTarefas()
    listarTarefas()
    numero = int(input('\nDigite o ID da tarefa que deseja remover (Digite 0 para remover tudo): '))
    if numero == 0:
        certeza = input('Tem certeza que deseja remover tudo? ***Não haverá como recuperar dados apagados*** \n\nDigite "SIM" para confirmar e "NAO" para cancelar: ')

        while certeza != 'SIM' and certeza != 'NAO':
            certeza = input('Por favor, digite exatamente como é mostrado acima: ')
        if certeza == 'SIM':
            tarefas = []
            salvarTarefa()
            print("\nTodas as tarefas foram apagadas")
        if certeza == 'NAO':
            print('\nRetornando...')
    else: 
        if numero <= len(tarefas) and numero > 0:
            tarefas.pop(numero - 1)
            for i, tarefa in enumerate(tarefas):
                tarefa["id"] = i + 1
                salvarTarefa()
            print('Tarefa removida\n')
        else:
            print('\n***ID iválido! Tente novamente.***')

def editarTarefa():
    listarTarefas()
    numero = int(input('Digite o ID da tarefa que deseja editar: '))
    if numero <= len(tarefas):
        edicao = str(input(f'Digite a alteração da tarefa {numero}: '))
        tarefas[numero - 1]["Titulo"] = edicao
        print('\nTarefa editada')
        salvarTarefa()

    else:
        print('\n***ID inválido! Tente novamente.***')

def sair():
    saida = (input('Aperte "Enter" para sair'))

while True:
    while True:
        try:
            usrAcao = int(input('\n1 - Adicionar tarefa\n2 - Listar tarefa\n3 - Concluir Tarefas\n4 - Remover tarefa \n5 - Editar Tarefa \n6 - Sair\n\nDigite a opção de interesse: '))
            break
        except ValueError:
            print('\n----Por favor, insira um valor válido----')
    if usrAcao == 1:
        while True:
            try:
                qtdTarefas = int(input('Quantas tarefas deseja inserir? '))
                break
            except ValueError:
                print('Digite a quantidade de tarefas que deseja inserir: ')
        if qtdTarefas > 0:
            for i in range(qtdTarefas):
                adicionarTarefas()
    elif usrAcao == 2:
        if tarefas == []:
            print('\nSem tarefas\n')
            sair()
        else:
            print('')
            filtrarTarefas()
            print('')
            sair()
    elif usrAcao == 3:
        concluirTarefa()
    elif usrAcao == 4:
        removerTarefa()
    elif usrAcao == 5:
        editarTarefa()
    elif usrAcao == 6:
        print('Finalizado')
        break  
