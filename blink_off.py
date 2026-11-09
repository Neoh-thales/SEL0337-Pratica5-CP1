#!/usr/bin/env python3
# SEL0337 - Pratica 5 - Checkpoint 1
# Programa chamado pelo ExecStop do blink.service ao executar
# "sudo systemctl stop blink". A mensagem vai para o journal do servico e pode
# ser vista com "journalctl -u blink".
#
# O systemd roda o ExecStop ANTES de enviar SIGTERM ao blink.py, ou seja, com o
# LED ainda piscando. Por isso quem apaga o LED e o proprio blink.py (no
# finally), e este programa apenas registra a parada.

print("ExecStop: servico blink parado pelo systemctl")
