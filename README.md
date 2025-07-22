![GitHub last commit](https://img.shields.io/github/last-commit/etrusaek/selenium-chatbot-demo)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/etrusaek/selenium-chatbot-demo)

# 🧪 Chatbot Apostas Demo

Este projeto é uma **prova de conceito (PoC)** de um chatbot automatizado que interage com o chat de plataformas de apostas online.
O objetivo principal é enviar mensagens promocionais automaticamente em jogos ao vivo, com login manual feito pelo usuário.

## 🔍 Objetivo

Criar um script em Python usando **Selenium WebDriver** para:
- Acessar plataformas de apostas com o navegador visível.
- Permitir login manual (evitando bloqueios automatizados).
- Localizar o campo de bate-papo durante jogos ao vivo.
- Enviar mensagens automaticamente em intervalos definidos.

## ⚙️ Tecnologias utilizadas

- Python 3.11
- Selenium
- Google Chrome + chromedriver
- WebdriverWait + XPaths / seletores customizados

## 🚫 Limitações encontradas

Durante o desenvolvimento, surgiram obstáculos relacionados à automação em plataformas com jogos da **Evolution Gaming**:
- Campos de input protegidos ou inacessíveis por `Shadow DOM`.
- Elementos dinâmicos ou renderizados fora do DOM visível.
- Restrições anti-bot não burláveis com abordagens simples.
- Falhas de interação mesmo com presença confirmada do elemento.

obs: Plataforma testada: `Betaki` (baseada em jogos da Evolution Gaming, com proteções mais rígidas contra automação)

### 🛠️ Como executar

1. Instale as dependências:
   pip install -r requirements.txt

2. Execute o "main.py"
3. siga as instruções do terminal aberto



