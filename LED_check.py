from pyfirmata import Arduino , util
import time 

uno = Arduino("COM5")

it = util.Iterator(uno)
it.start()


led_linha1 = uno.get_pin('d:2:o')
led_linha2 = uno.get_pin('d:3:o')
led_linha3 = uno.get_pin('d:4:o')

led_linhas = [led_linha1, led_linha2, led_linha3]

led_coluna1 = uno.get_pin('d:5:o')
led_coluna2 = uno.get_pin('d:6:o')
led_coluna3 = uno.get_pin('d:7:o')

led_colunas = [led_coluna1, led_coluna2, led_coluna3]


def acender_led(linha , coluna):
    linha-=1
    coluna-=1
    
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


print("Iniciando teste de leds")
time1 = 0.2
for i in range(9):
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
