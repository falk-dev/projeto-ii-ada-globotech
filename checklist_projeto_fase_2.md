
# ✅ Projeto Unificado – Fase 2: Análise de Engajamento de Mídias Globo com Orientação a Objetos

## 📌 Objetivo
Aplicar os princípios e técnicas da Programação Orientada a
Objetos na base de código da Fase 1. Assim, o resultado será um sistema mais
robusto, modular, extensível e com maior integridade dos dados

---

## 🔹 1. Modelagem de Classes Centrais

### 🧩 1.1. Classe `Plataforma`

Representa uma plataforma onde o conteúdo é consumido ou a interação ocorre.

- [X] Criar atributos privados:
  - [X] `__id_plataforma` (int) - Identicador único da plataforma (pode ser gerado
internamente pela classe gerenciadora).
  - [X] `__nome_plataforma` (str) - Nome da plataforma (e.g., "Globoplay", "G1").
- [X] Construtor `__init__()`:
  - [X] Recebe nome_plataforma e, opcionalmente, id_plataforma.
  - [X] Valida se o nome não está vazio.
- [X] Criar `@property` e `@*.setter` para acesso e validação dos atributos.
- [X] Métodos mágicos:
  - [X] `__str__(self)`: Retorna o nome da plataforma.
  - [X] `__repr__(self)`: Retorna uma representação como `Plataforma(nome='...')`.
  - [X] `__eq__(self, other)` e ` __hash__(self)`: Para permitir que objeto Plataforma sejam comparados e usados em coleções como sets ou chaves de dicionários (baseado no nome, por exemplo).

### 📦 1.2. Classe `Conteudo` (classe base)
Representa um item de conteúdo consumível.

- [X] Criar atributos protegidos:
  - [X] `_id_conteudo` (int);
  - [X] `_nome_conteudo` (str);
  - [X] `_interacoes` (list): Lista para armazenar objetos Interacao associados a este conteúdo.
- [X] Construtor `__init__()`:
  - [X] Recebe `id_conteudo` e `nome_conteudo`;
  - [X] Inicializa `_interacoes` como uma lista vazia.
- [X] Criar `@property` para `id_conteudo` e `nome_conteudo`.
- [X] Métodos:
  - [X] `adicionar_interacao(self, interacao)`: Adiciona um objeto Interacao à lista `_interacoes`;
  - [X] `calcular_total_interacoes_engajamento(self)`: Calcula o total de 'like', 'share', 'comment';
  - [X] `calcular_contagem_por_tipo_interacao(self)`: Retorna um dicionário com a contagem de cada tipo de interação;
  - [X] `calcular_tempo_total_consumo(self)`:  Soma watch_duration_seconds das interações.
  - [X] `calcular_media_tempo_consumo(self)`: Calcula a média de watch_duration_seconds > 0;
  - [X] `listar_comentarios(self)`: Retorna uma lista dos textos dos comentários.
- [X] Métodos mágicos `__str__(self)` e `__repr__(self)`.

### 📺 1.3. Classes Derivadas de `Conteudo`
#### 🔸 `Video`
- [X] Atributo adicional: `__duracao_total_video_seg` - int, privado
- [X] Construtor (`__init__`): Chama `super().__init__()` e inicializa `__duracao_total_video_seg`.
- [X] Property para `duracao_total_video_seg`.
- [X] Métodos Sobrescritos/Novos:
  - [X] `calcular_percentual_medio_assistido(self)`: Calcula `(tempo médio de consumo / duracao_total_video_seg) * 100`. Retorna `0` se `duracao_total_video_seg` for `0`.

#### 🔸 `Podcast`
- [X] Atributos adicional: `__duracao_total_episodio_seg` (int, privado, opcional para maior detalhe).

#### 🔸 `Artigo`
- [X] Atributos adicional: `__tempo_leitura_estimado_seg` (int, privado).

### 💬 1.4. Classe `Interacao`
Representa uma única interação de um usuário com um conteúdo em uma plataforma.

- [X] Atributos (privados com properties):
  - [X] `__interacao_id` (int, opcional, gerado internamente).;
  - [X] `__conteudo_associado` (`Conteudo`): Referência ao objeto `Conteudo` relacionado;
  - [X] `__id_usuario` (int);
  - [X] `__timestamp_interacao` (datetime);
  - [X] `__plataforma_interacao` (`Plataforma`): Referência ao objeto `Plataforma` onde ocorreu;
  - [X] `__tipo_interacao` (str);
  - [X] `__watch_duration_seconds` (int);
  - [X] `__comment_text` (str).
- [X] Atributo de Classe: 
  - [X] `TIPOS_INTERACAO_VALIDOS = {'view_start', 'like', 'share', 'comment'}` (ou outros definidos).
- [X] Construtor (`__init__`):
  - [X] Recebe os dados brutos (e.g., de uma linha do CSV), um objeto `Conteudo` e um objeto `Plataforma`;
  - [X] Valida e atribui os valores:
    - [X] Converte `id_usuario` para int;
    - [X] Converte `timestamp_interacao` para datetime;
    - [X] Valida `tipo_interacao` contra `Interacao.TIPOS_INTERACAO_VALIDOS`. Se inválido, pode definir um padrão ou levantar um `ValueError`;
    - [X] Converte `watch_duration_seconds` para int (padrão 0, não negativo);
    - [X] `comment_text` (`strip`, padrão string vazia).
- [X] **Properties**: Para acesso e validação dos atributos.
- [X] **Métodos Mágicos**: `__str__` e `__repr__`.

### 👤 1.5. Classe `Usuario`
Representa um usuário da plataforma.

- [X] Atributos: 
  - [X] `__id_usuario` (int); 
  - [X] `__interacoes_realizadas` (list): Lista de objetos `Interacao`.
- [X] Construtor (`__init__`): Recebe `id_usuario`.
- [X] Properties: Para acesso aos atributos.
- [X] Métodos:
  - [X] `registrar_interacao(self, interacao: Interacao)`: Adiciona à lista `__interacoes_realizadas`.
  - [X] `obter_interacoes_por_tipo(self, tipo_desejado: str) -> list`: Filtra `__interacoes_realizadas`.
  - [X] `obter_conteudos_unicos_consumidos(self) -> set`: Retorna um set de objetos `Conteudo` (ou seus IDs).
  - [X] `calcular_tempo_total_consumo_plataforma(self, plataforma: Plataforma) -> int`: Calcula o tempo total de consumo para uma plataforma específica
  - [X] `plataformas_mais_frequentes(self, top_n=3) -> list`: Retorna as N plataformas mais utilizadas pelo usuário.
- [X] Métodos Mágicos: `__str__`, `__repr__`.

---

## 🔹 2. Sistema de Orquestração e Análise `SistemaAnaliseEngajamento`

- [X] Atributos (privados):
  - [X] `__plataformas_registradas`: Dicionário mapeando `nome_plataforma` (str) para objetos `Plataforma`. Usado para o "CRUD" em memória. 
  - [X] `__conteudos_registrados`: Dicionário mapeando `id_conteudo` (int) para objetos `Conteudo` (ou suas subclasses).
  - [X] `__usuarios_registrados`: Dicionário mapeando `id_usuario` (int) para objetos `Usuario`.
  - [X] `__proximo_id_plataforma` (int): Para gerar IDs para novas plataformas.
- [x] Construtor (`__init__`): Inicializa os dicionários e o contador de ID.
- [X] Métodos de Gerenciamento de Plataforma ("CRUD" em memória): 
  - [X] `cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma`: Cria e adiciona uma nova plataforma se não existir. Retorna o objeto `Plataforma`.
  - [X] `obter_plataforma(self, nome_plataforma: str) -> Plataforma`: Retorna uma plataforma pelo nome. Se não existir, pode cadastrá-la.
  - [X] `listar_plataformas(self) -> list`: Retorna uma lista de todas as plataformas cadastradas.
- [X] Métodos de Carga e Processamento:
  - [X] `_carregar_interacoes_csv(self, caminho_arquivo: str) -> list`: Carrega dados brutos do CSV.
  - [X] `processar_interacoes_do_csv(self, caminho_arquivo: str)`:
    - [X] Chama `_carregar_interacoes_csv`.
    - [X] Ao invés de gerar um dicionario com os dados brutos, será adaptado para armazenar os dados como objetos da classe adequada:
      - [X] Obtém/Cria o objeto `Plataforma`.
      - [X] Obtém/Cria o objeto `Conteudo`.
      - [X] Obtém/Cria o objeto `Usuario`.
      - [X] Tenta instanciar `Interacao`, lidando com `ValueError` para validações.
      - [X] Se `Interacao` válida, registra-a nos objetos `Conteudo` e `Usuario`.
- [X] Métodos de Análise e Relatório:
  - [X] `gerar_relatorio_engajamento_conteudos(self, top_n: int = None)`: Itera por `__conteudos_registrados`, usa os métodos de cada objeto `Conteudo` para calcular métricas e as exibe.
  - [X] `gerar_relatorio_atividade_usuarios(self, top_n: int = None)`: Similar, para usuários.
  - [X] `identificar_top_conteudos(self, metrica: str, n: int)`: (e.g., `metrica='tempo_total_consumo'`).
- [X] Atributo de Classe/Método de Classe (opcional):
  - [X] `SistemaAnaliseEngajamento.VERSAO_ANALISE = "2.0"`
  
---

## 🔹 3. Estrutura de Diretórios
O projeto deve ser organizado com estrutura de módulos como aprendido ao longo do módulo

```
projeto_engajamento_fase2/
├── __init__.py
├── entidades/ (Sub-pacote)
│   ├── __init__.py
│   ├── plataforma.py (Classe Plataforma)
│   ├── conteudo.py (Classes Conteudo, Video, Podcast, Artigo)
│   ├── interacao.py (Classe Interacao)
│   └── usuario.py (Classe Usuario)
├── analise/ (Sub-pacote)
│   ├── __init__.py
│   └── sistema.py (Classe SistemaAnaliseEngajamento)
├── main.py (Script principal)
└── interacoes_globo.csv (Arquivo de dados)
```

---

## 🎯 4. Apresentação Final
- [X] Demonstrar o funcionamento do sistema.
- [X] Explicar decisões de design OO, como as classes se relacionam, e como os
princípios da POO foram aplicados.
- [X] Discutir desafios e aprendizados.


---

Cada tarefa pode ser marcada com:
- ✅ Concluído
- ⏳ Em andamento
- 🚫 Bloqueado

| Etapa | Tarefa | Responsável | Realizado em | Status |
|-------|--------|-------------|--------|--------|
| 1.1 | Criar atributos privados | Will | 11/06/2025 | ✅ |
| 1.1 | Construtor `__init__()` | Will | 11/06/2025 | ✅ |
| 1.1 | Criar `@property` e `@setter` para atributos | Will | 11/06/2025 | ✅ |
| 1.1 | Métodos mágicos | Will | 11/06/2025 | ✅ |
| 1.2 | Criar atributos protegidos | Mychelle | 09/06/2025 | ✅ |
| 1.2 | Construtor `__init__()` | Mychelle | 09/06/2025 | ✅ |
| 1.2 | Criar `@property` | Mychelle | 09/06/2025 | ✅ |
| 1.2 | Métodos | Mychelle | 13/06/2025 | ✅ |
| 1.2 | Métodos mágicos | Mychelle | 12/06/2025 | ✅ |
| 1.3 | Classe `Video` | Gabi | 12/06/2025 | ✅ |
| 1.3 | Classe `Podcast` | Gabi | 12/06/2025 | ✅ |
| 1.3 | Classe `Artigo` | Gabi | 12/06/2025 | ✅ |
| 1.4 | Atributos (privados com properties) | Rafa | 11/06/2025 | ✅ |
| 1.4 | Atributo de Classe | Rafa | 11/06/2025 | ✅ |
| 1.4 | Construtor (`__init__`) | Rafa | 11/06/2025 | ✅ |
| 1.4 | Properties | Rafa | 11/06/2025 | ✅ |
| 1.4 | Métodos Mágicos | Rafa | 11/06/2025 | ✅ |
| 1.5 | Atributos | Isabela | 12/06/2025 | ✅ |
| 1.5 | Construtor (`__init__`) | Isabela | 12/06/2025 | ✅ |
| 1.5 | Properties | Isabela | 12/06/2025 | ✅ |
| 1.5 | Métodos | Isabela | 12/06/2025 | ✅ |
| 1.5 | Métodos Mágicos | Isabela | 12/06/2025 | ✅ |
| 2 | Atributos (privados) | Mychelle | 10/06/2025 | ✅ |
| 2 | Construtor (`__init__`) | Mychelle | 10/06/2025 | ✅ |
| 2 | Métodos de Gerenciamento de Plataforma (CRUD) | Mychelle | 12/06/2025 | ✅ |
| 2 | Métodos de Carga e Processamento | Mychelle | 12/06/2025 | ✅ |
| 2 | Métodos de Análise e Relatório | Alice  | 13/06/2025 | ✅ |
| 2 | Atributo de Classe/Método de Classe | Mychelle | 10/06/2025 | ✅ |
| 3 | Criar estrutura de diretórios e arquivos | Will | 04/06/2025 | ✅ |
| 4 | Preparar apresentação, slides, explicações | Todos | 12/06/2025 | ✅ |


*Checklist baseado no documento oficial da Fase 2.*
