import time
import asyncio


async def consulta_dados():
    print("Consultando dados")
    await asyncio.sleep(2) # time.sleep(2)  # Simulando algum processo no banco de dados
    return "dados"


# Deveria tratar essa funcao de forma sincrona (quando fazer um conseulta async no banco tenho q usar uma lib async, o mesmo para numpy, pandas, ...)
async def processa_dados(dados):  # CPU bound -> Operacaoes aritmeticas
    print("Processando dados ...")
    await asyncio.sleep(2) # time.sleep(2)


async def grava_log():  # I/O bound -> Operacao de IO
    print("Gravando log...")
    await asyncio.sleep(2) # time.sleep(2)


async def main():
    start = time.perf_counter()
    print('Inicio')

    # dados = consulta_dados() # dados eh um corrotina
    # await processa_dados(await dados)
    # await grava_log() # Vai esperar a execucao


    dados = asyncio.create_task(consulta_dados())
    # print(dados) => interessante, olhar final do print
    asyncio.create_task(processa_dados(await dados))
    await grava_log()


    end = time.perf_counter()
    print('Fim')
    print(f'Demorou {round(end - start, 3)}')


if __name__ == '__main__':
    asyncio.run(main()) # Eventloop
    print("Fim do programa!!!!!!!!!!!")

# Nao ficou mais rapido :(, com a qtd de de await estou "esperando" da mesma forma q sync
# time.sleep tbm eh um problema, dentro de funcao assincrona tenho q usar outras funcoes assincornas
