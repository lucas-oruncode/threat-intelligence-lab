# 📊 Relatório de Incidente — Case 002

## 🧾 Resumo Executivo

Foi identificado um ataque de força bruta bem-sucedido contra um servidor SSH, resultando em acesso root e execução de código malicioso.

---

## 🔍 Análise Técnica

Um ator malicioso realizou múltiplas tentativas de autenticação via SSH, obtendo acesso à conta root após sucesso em brute force.

Após o acesso, o invasor executou comandos de reconhecimento e realizou o download de um script remoto (`shell.sh`), que foi executado no sistema.

A execução do script resultou em conexões externas, incluindo comunicação com o IP `185.199.110.153` na porta 4444, indicando possível interação com servidor de Command & Control (C2).

---

## 🔗 Cadeia do Ataque

1. Brute force via SSH  
2. Acesso root  
3. Reconhecimento (`whoami`)  
4. Download de payload  
5. Execução do script  
6. Comunicação com C2  

---

## 🎯 Classificação do Incidente

- Brute Force (SSH)
- Comprometimento de conta privilegiada
- Execução de malware
- Comunicação com C2

---

## 🚨 Impacto

- Comprometimento total do servidor
- Possível persistência do atacante
- Risco de movimentação lateral

---

## 🛡️ Recomendações

- Isolamento imediato do servidor
- Coleta de evidências (logs, memória)
- Análise do script `shell.sh`
- Rotação de credenciais (especialmente root)
- Desabilitar login root via SSH
- Implementar autenticação por chave (SSH key)
- Monitoramento de rede e endpoints
- Verificação de outros sistemas na rede

---

## 🧾 Conclusão

O incidente apresenta características claras de comprometimento completo, com acesso privilegiado, execução de código remoto e comunicação com infraestrutura de controle, exigindo resposta imediata.