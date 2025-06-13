from analise import SistemaAnaliseEngajamento
from entidades import Conteudo

sistema_analise = SistemaAnaliseEngajamento()

# Caminho do .csv
arquivo = "interacoes_globo.csv"

# Passando para o método de processamento de interações o arquivo csv.
sistema_analise.processar_interacoes_do_csv(arquivo)

while True:
    print("\nMenu de opções:\n")
    print("1. Listar plataformas cadastradas")
    print("2. Listar conteúdos cadastradas")
    print("3. Visualizar métricas de interação por tipo de todos os conteúdos")
    print("4. Visualizar métricas de tempo de visualização por conteúdo")
    print("5. Visualizar métricas de média de tempo de visualização por conteúdo")
    print("6. Visualizar comentários por conteúdo")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        print(f"\n➡️  Plataformas cadastradas:\n")
        plataformas = sistema_analise.listar_plataformas()

        for p in plataformas:
            print(p)

    elif opcao == "2":
        print(f"\n📺  Conteúdos cadastrados:\n")
        conteudos = sistema_analise.listar_conteudos()

        for c in conteudos:
            print(c)

    elif opcao == "3":
        print("\n📊 Métricas de interações por conteúdo: \n")

        todos_os_conteudos = sistema_analise.listar_conteudos()

        if not todos_os_conteudos:
            print("Nenhum conteúdo cadastrado para gerar relatório.")
        else:
            for conteudo in todos_os_conteudos:
                relatorio = conteudo.calcular_total_interacoes_engajamento()
                print(relatorio)

    elif opcao == "4":
        print("\n⏱️  Tempo total de visualização por conteúdo: \n")

        todos_os_conteudos = sistema_analise.listar_conteudos()

        if not todos_os_conteudos:
            print("Nenhum conteúdo cadastrado para gerar relatório.")
        else:
            for conteudo in todos_os_conteudos:
                relatorio = conteudo.calcular_tempo_total_consumo()
                print(relatorio)

    elif opcao == "5":
        print("\n⏱️  Média de tempo de visualização por conteúdo: \n")

        todos_os_conteudos = sistema_analise.listar_conteudos()

        if not todos_os_conteudos:
            print("Nenhum conteúdo cadastrado para gerar relatório.")
        else:
            for conteudo in todos_os_conteudos:
                relatorio = conteudo.calcular_media_tempo_consumo()
                print(relatorio)

    elif opcao == "6":
        print("\n💬  Comentários por conteúdo: \n")

        todos_os_conteudos = sistema_analise.listar_conteudos()

        if not todos_os_conteudos:
            print("Nenhum conteúdo cadastrado para gerar relatório.")
        else:
            for conteudo in todos_os_conteudos:
                relatorio = conteudo.listar_comentarios()
                print(relatorio)
