# 📊 Relatório de Incidente — Case 001

## 🧾 Resumo Executivo

Um usuário acessou uma URL suspeita e realizou o download de um arquivo executável, resultando em comportamento anômalo no sistema.

## 🔍 Análise Técnica

A URL acessada apresenta características típicas de campanhas de phishing, utilizando termos que simulam legitimidade.

O arquivo baixado (`update_client.exe`) sugere tentativa de engenharia social, induzindo o usuário a executar um falso software de atualização.

Após a execução, foi identificada comunicação com o IP externo `185.234.219.12` na porta 4444, frequentemente associada a atividades de controle remoto (C2).

A análise do IP indica histórico de atividades maliciosas, reforçando a hipótese de comprometimento.

## 🎯 Classificação do Incidente

- Phishing
- Infecção por malware
- Comunicação com Command & Control (C2)

## 🚨 Impacto

- Possível comprometimento da máquina do usuário
- Risco de movimentação lateral na rede

## 🛡️ Recomendações

- Isolamento imediato da máquina afetada
- Remoção do malware
- Verificação de outros dispositivos na rede
- Treinamento de conscientização de segurança para usuários
