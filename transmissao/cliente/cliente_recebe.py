import socket

recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recebe.bind(('127.0.0.1', 44444))
recebe.listen(10)

try:
    while True:
        sc, address = recebe.accept()
        
        arquivof = open("database/cliente/jogada_ai.txt",'wb')
        fim =0
        while (fim==0):       
        
            ler_bfferl = sc.recv(1024)
            
            while (ler_bfferl):
                    
                    arquivof.write(ler_bfferl)
                    ler_bfferl = sc.recv(1024)
                    
                    fim=1
                    
        arquivof.close()

        sc.close()
        
except:
    recebe.close()