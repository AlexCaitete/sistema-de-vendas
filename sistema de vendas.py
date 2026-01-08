# MIssão: Desenvolver uma aplicação em Python modularizada que permita Registrar Vendas, Calcula
# Preço Final (com regras de imposto e frete), Listar Vendas e Atualizar
# Status. O foco é a integridade dos dados e a precisão financeira.
# Aluno: Alex Roberto

vendas = []


def registrar_venda():
    print("\n--------------------")
    print("Registro de vendas")
    print("--------------------")

    try:
        id_venda = int(input("ID: "))
    except ValueError:
        print("⚠ ID deve ser um número!")
        return

    produto = input("Produto: ")

    try:
        valor_produto = float(input("Valor: R$ "))
    except ValueError:
        print("⚠ Valor inválido!")
        return

    estado = input("Estado (Sigla, ex: SP): ").upper().strip()

    print("Escolha o frete: [1] Padrão | [2] Express")
    while True:
        opcao = input("Opção de frete: ")
        match opcao:
            case "1":
                tipo_frete = "Padrão"
                break
            case "2":
                tipo_frete = "Express"
                break
            case _:
                print("⚠ Opção inválida. Por favor, digite 1 ou 2.")
                continue

    status = "Aguardando Pagamento"

    venda_nova = {
        'id': id_venda,
        'produto': produto,
        'valor_produto': valor_produto,
        'estado': estado,
        'tipo_frete': tipo_frete,
        'status': status
    }

    vendas.append(venda_nova)
    print("\n---------------------------------")
    print("✅ Venda registrada com sucesso!")
    print(f"Total de vendas cadastradas: {len(vendas)}")
    print("---------------------------------")


# Função do Alex (Ajustada para receber os textos corretos)
def calculo_total(valor_produto, estado, tipo_frete):
    estado_normalizado = estado.upper().strip()

    # Cálculo ICMS
    if estado_normalizado in ['SP', 'RJ']:
        icms = valor_produto * 0.10
    else:
        icms = valor_produto * 0.07

    # Cálculo Frete
    custo_frete = 0
    if valor_produto <= 1000:
        if tipo_frete == "Padrão":  # Ajustado para ler o texto salvo
            custo_frete = 20.00
        elif tipo_frete == "Express":
            custo_frete = 50.00
        else:
            custo_frete = 20.00  # Padrão caso erro

    preco_final = valor_produto + custo_frete + icms
    return round(preco_final, 2)


# Função auxiliar para chamar o cálculo do Alex dentro do menu
def processar_calculo():
    if not vendas:
        print("\n⚠ Nenhuma venda cadastrada para calcular.")
        return

    try:
        id_busca = int(input("\nDigite o ID da venda para calcular o total: "))
        venda_encontrada = None

        for v in vendas:
            if v['id'] == id_busca:
                venda_encontrada = v
                break

        if venda_encontrada:
            total = calculo_total(
                venda_encontrada['valor_produto'],
                venda_encontrada['estado'],
                venda_encontrada['tipo_frete']
            )
            print(f"\n💲 O preço final da venda {id_busca} (com impostos e frete) é: R$ {total:.2f}")
        else:
            print("❌ ID não encontrado.")
    except ValueError:
        print("⚠ Digite um número válido.")


# Função  (Ajustada formatação da tabela)
def exibir_relatorio():
    if len(vendas) == 0:
        print('\n| Sem registros de vendas.')
    else:
        print("\nRELATÓRIO DE VENDAS")
        # Ajustei os espaçamentos (<5, <15) para caberem as colunas
        print(f"| {'ID':<5} | {'PRODUTO':<15} | {'VALOR':<10} | {'ESTADO':<6} | {'FRETE':<10} | {'STATUS'}")
        print("-" * 80)

        for venda in vendas:
            print(
                f"| {venda['id']:<5} | {venda['produto']:<15} | R${venda['valor_produto']:<8} | {venda['estado']:<6} | {venda['tipo_frete']:<10} | {venda['status']}")



def confirmar_pagamento():
    if not vendas:
        print("\n⚠ Nenhuma venda cadastrada.")
        return

    try:
        id_pedido = int(input("\nDigite o ID do pedido para confirmar o pagamento: "))
    except ValueError:
        print("⚠ ID inválido! Digite apenas números.")
        return

    for venda in vendas:
        if venda['id'] == id_pedido:
            if venda['status'] == "Aguardando Pagamento":
                venda['status'] = "Pago/Enviado"
                print(f"✔ Pedido {id_pedido} atualizado para 'Pago/Enviado'.")
            else:
                print(f"⚠ O pedido já está com status: {venda['status']}")
            return

    print("❌ Pedido não encontrado.")



def sair():
    print("\nEncerrando o sistema... 👋")


def menu():
    while True:
        print("\n==== MENU DEVSHOP ====")
        print("1 - Cadastrar venda")
        print("2 - Calcular preço final (Simulação por ID)")
        print("3 - Listar vendas")
        print("4 - Atualizar status")
        print("5 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            registrar_venda()
        elif opc == "2":
            processar_calculo()  # Chamando a nova função intermediária
        elif opc == "3":
            exibir_relatorio()
        elif opc == "4":
            confirmar_pagamento()
        elif opc == "5":
            sair()
            break
        else:
            print("⚠ Opção inválida! Tente novamente.")


# Executar o programa
if __name__ == "__main__":
    menu()