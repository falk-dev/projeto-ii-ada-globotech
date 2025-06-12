""" 
Métodos:

registrar_interacao(), obter_interacoes_por_tipo().

calcular_tempo_total_consumo_plataforma(), plataformas_mais_frequentes().

"""

class Usuario:
     #Construtor
     def __init__(self, id_usuario: int) -> None:
         self.__id_usuario: int = id_usuario
         self.__interacoes_realizadas: list = [] #lista com objetos Interacao
 
     #Getters e setters
     @property
     def id_usuario(self):
         return self.__id_usuario
     
     @property
     def interacoes_realizadas(self):
         return self.__interacoes_realizadas
     
     # Métodos
     def registrar_interacao(self, interacao: Interacao): 
         pass
 
     def obter_interacoes_por_tipo(self, tipo_desejado: str) -> list: #filtra interacoes_realizadas
         pass
 
     def obter_conteudos_unicos_consumidos(self) -> set: #retorna set de objetos 'conteudo'
         pass
 
     def calcular_tempo_total_consumo_plataforma(self, plataforma: Plataforma) -> int: #retorna tempo para uma plataforma
         pass
 
     def plataformas_mais_frequentes(self, top_n=3) -> list: #retorna as plataformas mais frequentes do usuÃ¡rio
         pass
 
     #Métodos mágicos
         #__str__: representaÃ§Ã£o legÃ­vel do objeto, voltada para usuÃ¡rios finais -> chamado quando se usa str(obj) ou print(obj)
         #__repr__: - representaÃ§Ã£o oficial do objeto -> Ãºtil para depuraÃ§Ã£o 
 
