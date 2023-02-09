
class Processo:
    def __init__(self, pid, tempo_chegada, tempo_exec):
        self.pid = pid
        self.tempo_chegada = tempo_chegada
        self.tempo_exec = tempo_exec


def Escalonamento_FCFS(lista_processos):
    lista_processos = sorted(lista_processos, key=lambda x: x.tempo_chegada)
    for processo in lista_processos:
        print(
            f"Processo {processo.pid}"
            f" com tempo de chegada "
            f"{processo.tempo_chegada} e "
            f"executou por {processo.tempo_exec}s")


def Escalonamento_SJF(lista_processos):
    lista_processos = sorted(lista_processos, key=lambda x: x.tempo_exec)

    for processo in lista_processos:
        print(
            f"Processo {processo.pid} com tempo de chegada {processo.tempo_chegada}s e tempo de execução {processo.tempo_exec}s")


def Escalonamento_RR(lista_processos, quantum):
    while lista_processos:
        processo = lista_processos.pop(0)
        if processo.tempo_exec > quantum:
            processo.tempo_exec = processo.tempo_exec - quantum
            print(
                f"Processo {processo.pid}"
                f" com tempo de chegada "
                f"{processo.tempo_chegada}s e "
                f"tempo de execução {quantum}s")
            lista_processos.append(processo)
        else:
            print(f"Processo {processo.pid} "
                  f"com tempo de chegada {processo.tempo_chegada}s"
                  f"e tempo de execução {processo.tempo_exec}s")


num_processos = int(input("Digite o número de processos: "))
quantum = int(input("Digite o quantum: "))


lista_processos = []
for i in range(num_processos):
    tempo_chegada = int(input(f"Digite o tempo de chegada para o processo {i + 1}: "))
    tempo_exec = int(input(f"Digite o tempo de execução para o processo {i + 1}: "))
    lista_processos.append(Processo(i + 1, tempo_chegada, tempo_exec))


print('*' * 25 + '----FCFS----' + '*' * 25)
Escalonamento_FCFS(lista_processos)
print('*' * 25 + '-----SJF-----' + '*' * 25)
Escalonamento_SJF(lista_processos)
print('*' * 25 + '-----RR------' + '*' * 25)
Escalonamento_RR(lista_processos, quantum)
print('*' * 50)
