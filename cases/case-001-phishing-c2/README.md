# Case 001 — Phishing + Malware + C2

## 🧪 Cenário

Um usuário relatou comportamento anômalo após acessar uma URL suspeita e baixar um arquivo.

## 🎯 Objetivo

Investigar possível comprometimento utilizando análise de indicadores de comprometimento (IOCs).

## 🔍 IOCs Identificados

- URL: http://secure-update-check.net/update
- Arquivo: update_client.exe
- Hash (MD5): 5d41402abc4b2a76b9719d911017c592
- IP: 185.234.219.12
- Porta: 4444

## 🧠 Resultado

O incidente foi classificado como:
- Phishing
- Infecção por malware
- Comunicação com servidor C2
