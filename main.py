import RPi.GPIO as io
import time

# CONFIGURACIONES REQUERIDAS POR LA LIBRERIA
io.setmode(io.BOARD)
io.setwarnings(True)

# CONFIGURACIONES DE PERIFERICOS
LED1 = 13
SWITCH = 11

io.setup(LED1, io.OUT)
io.setup(SWITCH, io.IN)

# RUTINA PRINCIPAL

if __name__ == '__main__':
    while True:
        switch_value = io.input(SWITCH)
        if switch_value == 0:
            io.output(LED1, True)
        else:
            io.output(LED1, False)
