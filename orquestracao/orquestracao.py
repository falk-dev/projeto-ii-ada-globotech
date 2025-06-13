""" 
Classe de Orquestração: SistemaAnaliseEngajamento
Atributos:

Dicionários para gerenciar objetos (__plataformas_registradas, __conteudos_registrados, __usuarios_registrados).

Métodos Principais:

CRUD de Plataformas: cadastrar_plataforma(), obter_plataforma().

Processamento de CSV:

_carregar_interacoes_csv(): Lê dados brutos.

processar_interacoes_do_csv(): Transforma linhas em objetos, vinculando Interacao → Conteudo → Usuario → Plataforma.

Relatórios:

gerar_relatorio_engajamento_conteudos(): Métricas por conteúdo.

gerar_relatorio_atividade_usuarios(): Top usuários por interações.

identificar_top_conteudos(): Filtro por métricas (tempo, comentários, etc.).
"""
import csv
from datetime import datetime
from entity.plataforma import Plataforma
from entity.usuario import Usuario
from entity.conteudo import Video, Podcast, Artigo
from entity.interacao import Interacao

class SistemaAnaliseEngajamento:

    # Construtor
    def __init__(self):
        # Dicionário de plataformas registradas (nome -> Plataforma)
        self.__plataformas_registradas = {}
        # Dicionário de conteúdos registrados (id -> Conteudo)
        self.__conteudos_registrados = {}
        # Dicionário de usuários registrados (id -> Usuario)
        self.__usuarios_registrados = {}
        # Contador para gerar IDs únicos de plataformas
        self.__proximo_id_plataforma = 1

    # Cadastra uma nova plataforma, se ela ainda não existir
    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        if nome_plataforma in self.__plataformas_registradas:
            return self.__plataformas_registradas[nome_plataforma]
        nova = Plataforma(self.__proximo_id_plataforma, nome_plataforma)
        self.__plataformas_registradas[nome_plataforma] = nova
        self.__proximo_id_plataforma += 1
        return nova

    # Retorna uma plataforma existente ou a cadastra se não existir
    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return self.__plataformas_registradas.get(nome_plataforma) or self.cadastrar_plataforma(nome_plataforma)

    # Retorna a lista de todas as plataformas registradas
    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())

    # Lê o CSV e carrega os dados como dicionários
    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list:
        with open(caminho_arquivo, encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return [linha for linha in leitor]

    # Processa as interações do CSV transformando em objetos
    def processar_interacoes_do_csv(self, caminho_arquivo: str):
        dados = self._carregar_interacoes_csv(caminho_arquivo)
        for linha in dados:
            try:
                # Criação ou recuperação do objeto Conteúdo
                id_conteudo = int(linha["content_id"])
                nome_conteudo = linha["content_name"]
                tipo_conteudo = linha["content_type"].lower()

                if id_conteudo not in self.__conteudos_registrados:
                    if tipo_conteudo == "video":
                        conteudo = Video(id_conteudo, nome_conteudo, int(linha.get("content_total_time", 0)))
                    elif tipo_conteudo == "podcast":
                        conteudo = Podcast(id_conteudo, nome_conteudo)
                    elif tipo_conteudo == "artigo":
                        conteudo = Artigo(id_conteudo, nome_conteudo, int(linha.get("content_total_time", 0)))
                    else:
                        continue  # Conteúdo de tipo desconhecido
                    self.__conteudos_registrados[id_conteudo] = conteudo
                else:
                    conteudo = self.__conteudos_registrados[id_conteudo]

                # Criação ou recuperação do objeto Usuário
                id_usuario = int(linha["user_id"])
                if id_usuario not in self.__usuarios_registrados:
                    usuario = Usuario(id_usuario)
                    self.__usuarios_registrados[id_usuario] = usuario
                else:
                    usuario = self.__usuarios_registrados[id_usuario]

                # Criação ou recuperação da Plataforma
                plataforma = self.obter_plataforma(linha["platform"])

                # Criação do objeto Interação
                interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=linha["timestamp"],
                    plataforma_interacao=plataforma,
                    tipo_interacao=linha["interaction_type"],
                    watch_duration_seconds=linha.get("watch_duration", 0),
                    comment_text=linha.get("comment_text", "")
                )

                # Vincula a interação ao conteúdo e ao usuário
                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except (ValueError, KeyError) as e:
                print(f"Erro ao processar linha: {linha}. Erro: {e}")

    # Gera um relatório de engajamento por conteúdo
    def gerar_relatorio_engajamento_conteudos(self, top_n=None):
        conteudos = list(self.__conteudos_registrados.values())
        conteudos.sort(key=lambda c: c.calcular_total_interacoes_engajamento(), reverse=True)
        for conteudo in (conteudos[:top_n] if top_n else conteudos):
            print(f"{conteudo}: {conteudo.calcular_total_interacoes_engajamento()} interações")

    # Gera um relatório com os usuários mais ativos
    def gerar_relatorio_atividade_usuarios(self, top_n=None):
        usuarios = list(self.__usuarios_registrados.values())
        usuarios.sort(key=lambda u: len(u._Usuario__interacoes_realizadas), reverse=True)
        for usuario in (usuarios[:top_n] if top_n else usuarios):
            print(f"Usuário {usuario.id_usuario}: {len(usuario._Usuario__interacoes_realizadas)} interações")

    # Identifica os top conteúdos com base na métrica especificada
    def identificar_top_conteudos(self, metrica: str, n: int):
        conteudos = list(self.__conteudos_registrados.values())
        if metrica == "tempo_total_consumo":
            conteudos.sort(key=lambda c: c.calcular_tempo_total_consumo(), reverse=True)
        elif metrica == "media_tempo_consumo":
            conteudos.sort(key=lambda c: c.calcular_media_tempo_consumo(), reverse=True)
        else:
            print("Métrica desconhecida.")
            return
        for conteudo in conteudos[:n]:
            print(f"{conteudo}: {getattr(conteudo, f'calcular_{metrica}')()}s")
