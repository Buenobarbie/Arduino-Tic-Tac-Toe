import socket

def envia_jogada_ai(x, y):

    envia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    envia.connect(("127.0.0.1", 44444))

    arquivo = open("database/servidor/jogada_ai.txt",'w')
    arquivo.write(f"{x} {y}\n")
    arquivo.close()

    arquivo = open ("database/servidor/jogada_ai.txt", "rb")
    ler_buffer = arquivo.read(1024)

    while (ler_buffer):
        envia.send(ler_buffer)
        ler_buffer = arquivo.read(1024)

    envia.close()
    