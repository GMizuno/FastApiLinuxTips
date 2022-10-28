import time


def consulta_dados():
    print("Consultando dados")
    time.sleep(2)  # Simulando algum processo no banco de dados
    return "dados"


def processa_dados(dados):  # CPU bound -> Operacaoes aritmeticas
    print("Processando dados ...")
    time.sleep(2)


def grava_log():  # I/O bound -> Operacao de IO
    print("Gravando log...")
    time.sleep(2)


def main():
    start = time.perf_counter()
    print('Inicio')

    dados = consulta_dados()
    processa_dados(dados)
    grava_log()

    end = time.perf_counter()
    print('Fim')
    print(f'Demorou {round(end - start, 3)}')


if __name__ == '__main__':
    main()
