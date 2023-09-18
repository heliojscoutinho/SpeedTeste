import speedtest #pip install speedtest-cli
import time
s = speedtest.Speedtest()

print("Carregando servidores...")
s.get_servers() #Alocando os servidores

print("Conectando no melhor servidor disponível...")
bestServer = s.get_best_server() #Escolhendo o melhor servidor disponivel
print(f"Conectando ao seridor {bestServer['host']}, localização: {bestServer['country']} ")
time.sleep(1)

print("Iniciando o teste...")
time.sleep(2)

print("Ping do servidor...")
ping= s.results.ping #Ping do servidor
time.sleep(1)

print("Download...")
download = s.download() #Teste de download
time.sleep(1)

print("Upload...")
upload = s.upload() #Teste de upload
time.sleep(1)


def border_msg(msg): #Caixa de mensagem
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)

print("*************RESULTADO*************")
border_msg(f"Ping: {ping:.2f} ms")
border_msg(f"Download: {download /1024/1024:.2f} Mbit/s")
border_msg(f"Upload: {upload /1024/1024:.2f} Mbit/s")

time.sleep(60)
