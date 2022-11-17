import socket

def envia_jogada_humano(x, y):

    envia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    envia.connect(("127.0.0.1",55555))

    arquivo = open("database/cliente/jogada_humano.txt",'w')
    arquivo.write(f"{3*x + y + 1}\n")
    arquivo.close()

    arquivo = open ("database/cliente/jogada_humano.txt", "rb")
    ler_buffer = arquivo.read(1024)

    while (ler_buffer):
        envia.send(ler_buffer)
        ler_buffer = arquivo.read(1024)

    envia.close()
