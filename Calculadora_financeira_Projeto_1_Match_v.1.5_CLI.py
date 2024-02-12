
# Projeto 1
# Neste projeto, os alunos criarão uma calculadora financeira em Python que ajudará os
# usuários a calcular empréstimos com base em sua renda. A aplicação incluirá as seguintes
# etapas:
# ➔ Validação de Renda:
# ◆ Os usuários inserirão informações sobre sua renda mensal.
# ◆ A aplicação verificará se a renda inserida é válida e está dentro de um limite
# específico.
# ➔ Cálculo de Empréstimo:
# ◆ Após a validação bem-sucedida da renda, os usuários poderão inserir o valor
# do empréstimo desejado e o prazo.
# ◆ A aplicação calculará a taxa de juros apropriada e o valor das prestações
# mensais.
# ➔ Apresentação dos Resultados:
# ◆ A aplicação exibirá os resultados do cálculo, incluindo o valor das prestações
# mensais e o custo total do empréstimo.



# Função para validar a renda do usuário
def validar_renda(renda):
    limite_minimo = 1000  # Defina o limite mínimo de renda desejado

    if renda >= limite_minimo:
        return True
    else:
        return False



# Função para calcular o valor das prestações mensais
def calcular_prestacoes(valor_emprestimo, taxa_juros_mensal, prazo):
    try:
        #Nova forma de cálculo de prestação, usando a fórmula em https://en.wikipedia.org/wiki/Equated_monthly_installment
        #A nova fórmula de cálculo da prestação funciona igual a calculadora do banco central: https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormFinanciamentoPrestacoesFixas.do?method=exibirFormFinanciamentoPrestacoesFixas
        taxa_juros_mensal_decimal = taxa_juros_mensal / 100  # Converte a taxa de porcentagem para decimal
        prestacao = ((valor_emprestimo * taxa_juros_mensal_decimal) * ((1 + taxa_juros_mensal_decimal) ** (prazo)))/(((1 + taxa_juros_mensal_decimal)**(prazo))-1)
        return prestacao
    except ZeroDivisionError:
        print("Divisão por zero")
        main()

# Função principal
def main():
    # Solicita ao usuário a renda mensal
    renda = float(input("Informe sua renda mensal: "))
    if validar_renda(renda):
        # Solicita ao usuário o valor do empréstimo e o prazo.
        valor_emprestimo = float(input("Informe o valor do empréstimo desejado: "))
          

    #Se o empréstimo for 10x maior que a renda, reinicia o programa.
        if valor_emprestimo > renda * 10:
            print("O valor do empréstimo excede 10x a renda!")
            main()
        else: 
            pass

        # Recebe o prazo do investimento em meses
        prazo = int(input("Informe o prazo do empréstimo em meses:"))
        if prazo < 0:
            print("O prazo informado é menor do que zero")
            main()
        else: 
            pass
        
        # Recebe a taxa de juros mensal
        taxa_juros_mensal = float(input("Informe a Taxa de juros mensal desejada:"))

        # Calcula a taxa de juros anual
        taxa_juros_anual = ((1 + taxa_juros_mensal/100)**(12) -1) * 100

        # Calcula o valor das prestações mensais
        prestacao = calcular_prestacoes(valor_emprestimo, taxa_juros_mensal, prazo)

        # Calcula o custo total do empréstimo
        custo_total = (prestacao * prazo)


    
    else:
        print("Desculpe, sua renda não atende aos requisitos mínimos para o empréstimo.")
        main()

        

# Apresenta os resultados
    print("\nResultado do Cálculo:")
    print(f'Renda mensal informada: R$ {renda:.4f}')
    print(f'Valor tomado como empréstimo: R$ {valor_emprestimo:.4f}')
    print(f"Taxa de Juros anual: {taxa_juros_anual:.4f}% ao ano")
    print(f"Taxa de Juros mensal: {taxa_juros_mensal:.4f}% ao mês")
    print(f"Prazo em meses: {prazo} meses")
    print(f"Valor das Prestações Mensais: R$ {prestacao:.4f}")
    print(f"Custo Total do Empréstimo: R$ {custo_total:.4f}")

    

if __name__ == "__main__":
    main()
