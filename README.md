# 🛒 DevShop - Sistema de Gestão de Vendas

Sistema de back-office para gerenciamento de vendas, desenvolvido em **Python**. O projeto simula o fluxo de registro, precificação e atualização de status de pedidos de um e-commerce via terminal (CLI).

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades práticas do curso de **Análise e Desenvolvimento de Sistemas**, focando na aplicação de estruturas de dados e modularização de código.

O sistema permite cadastrar vendas e, crucialmente, aplica regras de negócios automáticas para definição do preço final, considerando o estado de destino (tributação) e regras de frete.

## 🚀 Funcionalidades

* **Registro de Vendas:** Cadastro detalhado com ID, produto, valor e destino.
* **Lógica de Precificação (Business Logic):**
    * Cálculo automático de **ICMS** baseado no estado (SP/RJ vs Outros).
    * Regras de **Frete**: Gratuito para compras acima de R$ 1.000,00 ou tabelado por tipo (Padrão/Express).
* **Gestão de Status:** Atualização do fluxo de "Aguardando Pagamento" para "Pago/Enviado".
* **Relatórios:** Visualização tabular de todas as vendas registradas.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Conceitos:**
    * Manipulação de Listas e Dicionários.
    * Estruturas Condicionais (`match/case`, `if/else`).
    * Tratamento de Exceções (`try/except`).
    * Funções e Modularização.

## 💻 Como executar

Certifique-se de ter o Python instalado.

1. Clone o repositório:
```bash
git clone [https://github.com/AlexCaitete/devshop-sales-manager.git](https://github.com/AlexCaitete/devshop-sales-manager.git)
