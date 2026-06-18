# 🏢 Sistema de Controle de Elevadores

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completo-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

*Um sistema inteligente de controle de elevadores com lógica avançada de distribuição* 🚀

[Features](#-features) • [Instalação](#-instalação) • [Como Usar](#-como-usar) • [Arquitetura](#-arquitetura) • [Autor](#-autor)

</div>

---

## 📋 Sobre o Projeto

Um simulador completo de **sistema de controle de elevadores** desenvolvido em Python, implementando lógica inteligente de distribuição de chamadas entre múltiplos elevadores. O projeto foi desenvolvido como atividade prática de **Lógica de Programação** e demonstra conceitos avançados de orientação a objetos e algoritmos otimizados.

### 🎯 Objetivo
Criar um sistema que gerencie automaticamente dois elevadores, distribuindo as chamadas de forma inteligente para otimizar o tempo de espera dos usuários.

---

## ✨ Features

### 🛗 Funcionalidades Principais

✅ **2 Elevadores Independentes**
- Cada elevador com seu próprio estado e controle
- Movimentação independente entre andares
- Monitoramento de ocupação em tempo real

✅ **Estrutura Completa de Andares**
- 4 Andares principais (1, 2, 3, 4)
- 2 Subsolos (-1, -2)
- Térreo como ponto de referência (0)
- Total: 7 níveis de navegação

✅ **Lógica Inteligente de Distribuição**
- Escolhe o elevador **mais próximo** do andar desejado
- Em caso de empate, escolhe o com **menor ocupação**
- Otimização de tempo e eficiência

✅ **Gerenciamento de Capacidade**
- Limite de 8 pessoas por elevador
- Controle de entrada e saída de usuários
- Visualização de ocupação em tempo real com barra de progresso

✅ **Andar Inicial Aleatório**
- Cada elevador começa em um andar aleatório
- Simula cenário real de operação

✅ **Menu Interativo e Intuitivo**
- Interface amigável em linha de comando
- Feedback visual com emojis
- Navegação clara e fácil

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Descrição |
|-----------|-----------|
| ![Python](https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg) | **Python 3.8+** - Linguagem principal |
| 🎨 | **Emojis & Formatação** - Interface visual |
| 📊 | **Algoritmos & Estruturas** - Lógica inteligente |

</div>

---

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior instalado
- Terminal/Prompt de Comando
- Windows, macOS ou Linux

### Passos de Instalação

1. **Clone ou baixe o repositório**
```bash
git clone <seu-repositorio>
cd "LOGICA DE PROGRAMAÇÃO ELEVADOR"
```

2. **Verifique a versão do Python**
```bash
python --version
```

3. **Execute o programa**
```bash
python elevador.py
```

---

## 🚀 Como Usar

### Iniciando o Programa

Ao executar o programa, você verá a tela inicial:

```
============================================================
           🏢 SISTEMA DE CONTROLE DE ELEVADORES 🏢            
============================================================
✓ 2 Elevadores disponíveis
✓ Andares: Subsolo 2, Subsolo 1, Térreo, 1, 2, 3, 4
✓ Capacidade por elevador: 8 pessoas
============================================================
```

### Menu de Opções

```
📋 MENU DE OPÇÕES:
1. Chamar elevador para um andar
2. Entrar no elevador 1
3. Entrar no elevador 2
4. Sair do elevador 1
5. Sair do elevador 2
6. Ver status dos elevadores
7. Sair do programa
```

### 📍 Andares Disponíveis

| Código | Descrição |
|--------|-----------|
| -2 | Subsolo 2 |
| -1 | Subsolo 1 |
| 0 | Térreo |
| 1-4 | Andares 1 a 4 |

### Exemplos de Uso

**Exemplo 1: Chamar um elevador**
```
Escolha uma opção (1-7): 1
Digite o número do andar desejado: 2

📍 Chamando o elevador 1 para o andar 2...
🛗 Elevador 1 movendo para o andar 2...
✓ Elevador 1 chegou ao andar 2!
```

**Exemplo 2: Entrar e sair do elevador**
```
Escolha uma opção (1-7): 2
✓ Uma pessoa entrou no elevador 1.

Escolha uma opção (1-7): 4
✓ Uma pessoa saiu do elevador 1.
```

**Exemplo 3: Visualizar status**
```
Escolha uma opção (1-7): 6

📊 STATUS DO SISTEMA DE ELEVADORES
============================================================
Elevador 1: Andar 2 | Pessoas: 1/8 [█░░░░░░░░]
Elevador 2: Andar Térreo | Pessoas: 0/8 [░░░░░░░░░░]
============================================================
```

---

## 🏗️ Arquitetura

### Diagrama de Classes

```
┌─────────────────────────────────────┐
│           Elevador                  │
├─────────────────────────────────────┤
│ - numero: int                       │
│ - capacidade: int                   │
│ - andar_minimo: int                 │
│ - andar_maximo: int                 │
│ - andar_atual: int                  │
│ - pessoas_no_elevador: int          │
├─────────────────────────────────────┤
│ + entrar()                          │
│ + sair()                            │
│ + subir()                           │
│ + descer()                          │
│ + ir_para_andar(andar_destino)      │
│ + obter_distancia(andar)            │
│ + mostrar_status()                  │
└─────────────────────────────────────┘
         ▲
         │ usa
         │
┌─────────────────────────────────────┐
│       SistemaElevadores             │
├─────────────────────────────────────┤
│ - elevadores: List[Elevador]        │
│ - andar_minimo: int                 │
│ - andar_maximo: int                 │
├─────────────────────────────────────┤
│ + escolher_elevador(andar)          │
│ + chamar_elevador(andar)            │
│ + mostrar_status_sistema()          │
└─────────────────────────────────────┘
```

### Fluxo de Funcionamento

```
Usuario Inicia Programa
        ↓
Menu Interativo Exibido
        ↓
Usuario Escolhe Opcao
        ↓
    ┌───┴───┬─────┬─────┬─────┬─────┬─────┐
    ↓       ↓     ↓     ↓     ↓     ↓     ↓
  Chamar Entrar Sair  Status Ver   Sair  Menu
  Elevador  Elev  Elev  Elev  Todos Prog  Novo
    ↓       ↓     ↓     ↓     ↓     ↓     ↓
  Inteligencia | | | Feedback | Encerra
  Distribuição ↓ ↓ ↓ Atualiza  │
    ↓          OK  │     ↓     │
    └────────────→ └─────┴─────┘
```

### Algoritmo de Seleção Inteligente

```python
def escolher_elevador(andar_destino):
    distancia_elev1 = abs(elev1.andar_atual - andar_destino)
    distancia_elev2 = abs(elev2.andar_atual - andar_destino)
    
    if distancia_elev1 < distancia_elev2:
        return elevador_1
    elif distancia_elev2 < distancia_elev1:
        return elevador_2
    else:
        # Mesma distância - escolhe com menos pessoas
        if elev1.ocupacao <= elev2.ocupacao:
            return elevador_1
        else:
            return elevador_2
```

---

## 📊 Estrutura do Projeto

```
LOGICA DE PROGRAMAÇÃO ELEVADOR/
│
├── elevador.py          # Arquivo principal do sistema
├── README.md            # Este arquivo
└── requirements.txt     # Dependências (apenas Python padrão)
```

---

## 🎓 Conceitos Implementados

### Programação Orientada a Objetos (POO)
- ✅ Classes e Objetos
- ✅ Encapsulamento
- ✅ Métodos e Atributos
- ✅ Instanciação múltipla

### Estruturas de Dados
- ✅ Listas
- ✅ Atributos de instância
- ✅ Métodos de acesso e modificação

### Algoritmos
- ✅ Busca (encontrar elevador mais próximo)
- ✅ Comparação (escolher por ocupação)
- ✅ Iteração (movimento andar por andar)
- ✅ Lógica condicional

### Boas Práticas
- ✅ Nomes descritivos
- ✅ Documentação (docstrings)
- ✅ Tratamento de erros
- ✅ Interface amigável

---

## 🧪 Testando o Sistema

### Teste 1: Distribuição Inteligente
1. Abra dois terminais e visualize o status em tempo real
2. Chame o elevador para andares diferentes
3. Observe qual elevador é escolhido

### Teste 2: Limite de Capacidade
1. Entre 8 vezes no elevador 1
2. Tente entrar pela 9ª vez
3. Veja a mensagem de elevador cheio

### Teste 3: Navegação de Andares
1. Chame o elevador para o subsolo (-2)
2. Chame para o andar 4
3. Observe o movimento progressivo

---

## 💡 Melhorias Futuras

- 🔔 Sistema de chamadas com fila de espera
- 📱 Interface gráfica com tkinter ou Pygame
- 💾 Persistência de dados (salvar histórico)
- 📈 Estatísticas de uso (tempo médio, elevador mais usado)
- 🌐 API REST para integração
- ⚙️ Configuração de capacidade por arquivo

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests
- Compartilhar ideias

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido como atividade de **Lógica de Programação**

### Contato
📧 Email: seu-email@example.com
💼 LinkedIn: [Seu Perfil](https://linkedin.com)
🐙 GitHub: [Seu Perfil](https://github.com)

---

## 📚 Referências e Recursos

- [Documentação Python](https://docs.python.org/3/)
- [PEP 8 - Guia de Estilo Python](https://www.python.org/dev/peps/pep-0008/)
- [Real Python - OOP](https://realpython.com/inheritance-composition-python/)
- [GeeksforGeeks - Python Tutorial](https://www.geeksforgeeks.org/python-tutorial/)

---

<div align="center">

### ⭐ Se este projeto foi útil, deixe uma estrela! ⭐

![Made with ❤️](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by%20Você-blue)

**2026** • Desenvolvido com Python 🐍

</div>
