# 🧠 Investigação

## 1. Análise de logs

Foram identificadas múltiplas tentativas de login via SSH seguidas de sucesso:

- Tentativas consecutivas em curto intervalo
- Acesso bem-sucedido à conta root

Indício forte de ataque de força bruta.

---

## 2. Ações pós-comprometimento

Após login:

- Execução de `whoami` (confirmação de privilégio)
- Download de script remoto via `wget`
- Alteração de permissão (`chmod +x`)
- Execução do script (`./shell.sh`)

Indica execução de payload malicioso.

---

## 3. Análise de rede

Conexões de saída detectadas:

- 185.199.110.153:4444 → possível C2
- 103.21.244.0:80 → possível infraestrutura intermediária (proxy)

---

## 4. Análise do domínio

Domínio utilizado para download:

- `malicious-dropper.net`

Sem detecção direta em ferramentas, porém:

- comportamento suspeito
- uso direto em execução de script

---

## 5. Conclusão técnica

Evidências indicam comprometimento completo do sistema com execução de código remoto e comunicação externa.