from analise import SistemaAnaliseEngajamento

sistema_analise = SistemaAnaliseEngajamento()

# Passando para o método público o arquivo csv a ser lido
sistema_analise.carregar_interacoes("interacoes_globo.csv")
