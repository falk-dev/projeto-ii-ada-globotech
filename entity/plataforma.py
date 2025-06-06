class Plataforma:
    
# Construtor
    def __init__(self, nome_plataforma: str, id_plataforma: int = None):
        self.__id_plataforma = id_plataforma
        self.__nome_plataforma = nome_plataforma
        
# Getters e Setters

    @property
    def id_plataforma(self):
        return self.__id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, id_plataforma):
        self.__id_plataforma = id_plataforma
        
    @property
    def nome_plataforma(self):
    # Validação do nome da plataforma
        if not self.__nome_plataforma:
            raise ValueError("O nome da plataforma nao pode estar vazio.")
        return self.__nome_plataforma

    @nome_plataforma.setter
    def nome_plataforma(self, novo_nome: str):
    # Se o novo nome da plataforma for vazio, lança uma exceção.
        if not novo_nome or not isinstance(novo_nome, str):
            raise ValueError("O nome da plataforma nao pode estar vazio.")
        self.__nome_plataforma = novo_nome
    
# Metodos Magicos  
        
    #__str__(self): Retorna o nome da plataforma.
    def __str__(self):
        return self.__nome_plataforma
    
    #__repr__(self): Retorna uma representação como Plataforma(nome='...').
    def __repr__(self):
        return f"Plataforma(nome='{self.__nome_plataforma}')"
    
    #__eq__(self, other): Verifica se duas plataformas sao iguais.
    def __eq__(self, other):
        return self.__nome_plataforma == other.__nome_plataforma
    
    #__hash__(self): Retorna o hash do nome da plataforma.  
    def __hash__(self):
        return hash(self.__nome_plataforma)