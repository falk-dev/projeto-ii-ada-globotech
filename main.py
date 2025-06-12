from analise import SistemaAnaliseEngajamento

sistema_analise = SistemaAnaliseEngajamento()

# Caminho do .csv
arquivo = "interacoes_globo.csv"

# Passando para o método de processamento de interações o arquivo csv.
sistema_analise.processar_interacoes_do_csv(arquivo)

while True:
    print("\nMenu de opções:\n")
    print("1. Listar plataformas cadastradas")
    print("2. Listar conteúdos cadastradas")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        plataformas = sistema_analise.listar_plataformas()

        for p in plataformas:
            print(p)

    elif opcao == "2":
        conteudos = sistema_analise.listar_conteudos()

        for c in conteudos:
            print(c)
