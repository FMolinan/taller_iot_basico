import RPi.GPIO as io
import time

# CONFIGURACIONES REQUERIDAS POR LA LIBRERIA
io.setmode(io.BOARD)
io.setwarnings(True)

# CONFIGURACIONES DE PERIFERICOS
LED1 = 13

io.setup(LED1, io.OUT)

# RUTINA PRINCIPAL

if __name__ == '__main__':
    while True:
        io.output(LED1, True)
        time.sleep(0.5)
        io.output(LED1, False)
        time.sleep(0.5)
