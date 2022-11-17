from pyfirmata import Arduino , util
import time 
from transmissao.cliente.cliente_envia import envia_jogada_humano

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


led_linha1 = uno.get_pin('d:2:o')
led_linha2 = uno.get_pin('d:3:o')
led_linha3 = uno.get_pin('d:4:o')

led_linhas = [led_linha1, led_linha2, led_linha3]

led_coluna1 = uno.get_pin('d:5:o')
led_coluna2 = uno.get_pin('d:6:o')
led_coluna3 = uno.get_pin('d:7:o')

led_colunas = [led_coluna1, led_coluna2, led_coluna3]

def acender_led(linha , coluna):
    
    for i in range(3):
        if i == linha:
            led_linhas[i].write(1)
        else:
            led_linhas[i].write(0)
        
        if i == coluna:
            led_colunas[i].write(0)
        else:
            led_colunas[i].write(1)
        
def apagar_leds():
    for i in range(3):
        led_linhas[i].write(0)
        led_colunas[i].write(0)

temp_board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def detecta_jogada():
    detect = False
    while not detect:
        update_mux()
        print("\nDetectanto jogada Player\n")
        imprimir_tabuleiro(board)
        for i in range(3):
            for j in range(3):
                if temp_board[i][j] != board[i][j] and board[i][j] == 1:
                    temp_board[i][j] = 1
                    detect = True
                    return i, j


def detectar_jogada_ia(x,y):
    time.sleep(2)
    acender_led(x,y)
    detect = False
    while not detect:
        print("\nDetectanto jogada IA\n")
        imprimir_tabuleiro(board)
        update_mux()
        for i in range(3):
            for j in range(3):
                if temp_board[i][j] != board[i][j] and board[i][j] == 1:
                    temp_board[i][j] = 1
                    detect = True
                    apagar_leds()
                    return i, j

for i in range(4):
    print(f"Jogada {i + 1}\n")
    x_p, y_p = detecta_jogada()

    acender_led(x_p, y_p)
    time.sleep(2)
    apagar_leds()

    envia_jogada_humano(x_p, y_p)
    time.sleep(1)

    with open('database/cliente/jogada_ai.txt', 'r') as file:
        x_ia, y_ia = map(int, file.read().rstrip().split())
    
    detectar_jogada_ia(x_ia, y_ia)


time1 = 0.2
for i in range(5):
    acender_led(1,1)
    time.sleep(time1)
    acender_led(1,2)
    time.sleep(time1)
    acender_led(1,3)
    time.sleep(time1)
    acender_led(2,1)
    time.sleep(time1)
    acender_led(2,2)
    time.sleep(time1)
    acender_led(2,3)
    time.sleep(time1)
    acender_led(3,1)
    time.sleep(time1)
    acender_led(3,2)
    time.sleep(time1)
    acender_led(3,3)
    time.sleep(time1)
    apagar_leds()
