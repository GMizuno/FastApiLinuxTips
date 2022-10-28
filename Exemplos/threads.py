import time
import concurrent.futures # Abstracao dos dois principais modelos processamento (Thread e Async)


def consulta_dados(db_name):
    print(f"Consultando dados {db_name}")
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executer:
        future = executer.submit(consulta_dados, 'Clickhouse') # Esperando o Banco de Dados
        dados = future.result()
        executer.submit(processa_dados, dados) # espera / await
        executer.submit(grava_log) # grava nao depende da demais, ou seja, poderia rodas ao mesmo tempo q as outras duas

    end = time.perf_counter()
    print('Fim')
    print(f'Demorou {round(end - start, 3)}')


if __name__ == '__main__':
    main()
