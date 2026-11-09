#!/usr/bin/env python3
# SEL0337 - Pratica 5 - Checkpoint 1
# Aplicacao: blink de um LED na GPIO 18, iniciado automaticamente no boot da
# Raspberry Pi pelo systemd (ver blink.service). Roda em loop infinito ate o
# servico ser parado com "sudo systemctl stop blink".

import signal
import sys
import time

import RPi.GPIO as GPIO

PINO_LED = 18    # numeracao BCM (pino fisico 12)
PERIODO_S = 0.2  # tempo em cada nivel logico


def ao_receber_sigterm(signum, frame):
    # O systemd encerra o servico com SIGTERM. Sem este tratamento o Python
    # morreria na hora, sem passar pelo finally, e o LED poderia ficar aceso.
    sys.exit(0)


signal.signal(signal.SIGTERM, ao_receber_sigterm)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINO_LED, GPIO.OUT)

try:
    print(f"Piscando LED na GPIO {PINO_LED}")
    while True:
        GPIO.output(PINO_LED, GPIO.HIGH)
        time.sleep(PERIODO_S)
        GPIO.output(PINO_LED, GPIO.LOW)
        time.sleep(PERIODO_S)
except KeyboardInterrupt:
    print("\nEncerrando o programa.")
finally:
    GPIO.cleanup()  # devolve o pino como entrada, apagando o LED
