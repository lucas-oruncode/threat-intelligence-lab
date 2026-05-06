# Case 002 — Brute Force + Root Compromise + C2

## 🧪 Cenário

O SOC detectou múltiplas tentativas de login via SSH seguidas de autenticação bem-sucedida e execução de comandos suspeitos.

## 🎯 Objetivo

Investigar possível comprometimento de servidor e identificar ações pós-exploração.

## 🔍 IOCs Identificados

- IP atacante: 45.77.12.90
- URL: http://malicious-dropper.net/shell.sh
- Arquivo: shell.sh
- Hash (SHA256): a3f5c2e7b9d4e1f6a7b8c9d0e1f2a3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9
- IP C2: 185.199.110.153
- Porta: 4444

## 🧠 Resultado

O incidente foi classificado como:

- Brute Force (SSH)
- Comprometimento de conta root
- Execução de malware
- Comunicação com servidor C2