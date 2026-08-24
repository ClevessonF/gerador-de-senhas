# 🔐 Gerador de Senhas

Um gerador de senhas aleatórias e seguras, feito em Python. Tem duas versões: uma simples (por linha de comando) e uma interativa (com menu no terminal).

## 📋 O que o projeto faz

Gera senhas aleatórias combinando letras minúsculas, maiúsculas, números e símbolos, para ajudar você a criar senhas mais seguras.

## 🚀 Como usar

### Versão interativa (recomendada)

Rode o comando abaixo e siga o menu:

bash
python gerador_senhas_interativo.py


Você escolhe o tamanho da senha (8, 12, 16 ou outro número) e, depois de gerar, pode:

- **R** → gerar uma nova senha
- **T** → trocar o tamanho da senha
- **Q** → sair do programa

### Versão simples (linha de comando)

bash
python gerador_senhas.py


Opções disponíveis:

| Comando | O que faz |
|---|---|
| `-t 16` | Define o tamanho da senha (padrão: 12) |
| `-q 5` | Gera várias senhas de uma vez (padrão: 1) |
| `--sem-maiusculas` | Remove letras maiúsculas |
| `--sem-numeros` | Remove números |
| `--sem-simbolos` | Remove símbolos |

Exemplo:

bash
python gerador_senhas.py -t 16 -q 5


## 🛠️ Requisitos

- Python 3 instalado no computador

## 📄 Licença

Sinta-se à vontade para usar, copiar e modificar este projeto como quiser.
