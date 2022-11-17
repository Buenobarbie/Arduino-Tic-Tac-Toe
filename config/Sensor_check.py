from pyfirmata import Arduino , util
import time 

uno = Arduino("COM5")

it = util.Iterator(uno)
it.start()


#Preencher
S0_pin = uno.get_pin('d:11:o')
S1_pin = uno.get_pin('d:10:o')
S2_pin = uno.get_pin('d:9:o')
S3_pin = uno.get_pin('d:8:o')
''''SIG_pin = uno.get_pin('a:0:i')'''
SIG_pin = uno.get_pin('d:12:i')   

mix = [S3_pin, S2_pin, S1_pin, S0_pin]

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


''''#úmeros de 0 a 15 em binário'''
bin = [
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,0,1,0],
    [1,0,1,1],
    [1,1,0,0],
    [1,1,0,1],
    [1,1,1,0],
    [1,1,1,1]

]


def update_mux():
    for i in range(9):
        for j in range(4):
            mix[j].write(bin[i][j])
        time.sleep(0.1)
        board[i//3][i%3] = int(SIG_pin.read())

def imprimir_tabuleiro(tab):
    for i in tab:
        for j in i:
            print(j , end=" ")
        print("\n", end = "")

while True:
    print()
    print("Analisando Sensores")
    update_mux()
    imprimir_tabuleiro(board)
    time.sleep(3)




'''while True:
    S0_pin.write(0)
    S1_pin.write(0)
    S2_pin.write(0)
    S3_pin.write(0)

    print("pino 0")
    print(SIG_pin.read())
    print(SIG_pin.read())
    print()

    time.sleep(3)

    S0_pin.write(1)
    S1_pin.write(0)
    S2_pin.write(0)
    S3_pin.write(0)

    print("pino 1")  
    print(SIG_pin.read())  
    print(SIG_pin.read())
    print()

    time.sleep(3)

    S0_pin.write(0)
    S1_pin.write(1)
    S2_pin.write(0)
    S3_pin.write(0)

    print("pino 2")    
    print(SIG_pin.read())
    print(SIG_pin.read())
    print()

    time.sleep(3)

    S0_pin.write(1)
    S1_pin.write(1)
    S2_pin.write(0)
    S3_pin.write(0)

    print("pino 3")    
    print(SIG_pin.read())
    print(SIG_pin.read())
    print()

    time.sleep(3)'''


