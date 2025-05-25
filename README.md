# Banco de Dados e API - Projeto Ótica

Este projeto consiste em um banco de dados relacional para gerenciar informações de uma ótica, juntamente com uma API desenvolvida em Flask para interagir com os dados, realizar operações CRUD e renderizar páginas HTML.

## Estrutura do Banco de Dados

O banco de dados contém as seguintes tabelas:

- `projeto_otica_material`: Materiais das armações.
- `projeto_otica_marca`: Marcas disponíveis.
- `projeto_otica_forma`: Formatos de armação.
- `projeto_otica_oculos`: Registro dos óculos.
- `projeto_otica_vendas`: Informações de vendas.

### Relacionamentos

Cada óculos está vinculado a:
- Um material (`ID_Material`)
- Uma marca (`ID_Marca`)
- Uma forma (`ID_Forma`)

As vendas registram:
- O óculos vendido (`ID_Oculos`)
- Informações do comprador e do pagamento

## Tecnologias Utilizadas

- **Banco de Dados**: MySQL via XAMPP
- **Back-end**: Flask (Python)
- **Front-end**: HTML + Jinja2
- **Conexão**: `mysql.connector` para interação com o banco

## API Flask

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/projeto-otica.git
   cd projeto-otica


- Instale as dependências:
pip install -r requirements.txt
- Execute a aplicação:
python app.py
Métodos CRUD da APIA API oferece os seguintes endpoints:- GET /oculos - Retorna todos os óculos cadastrados.
- POST /oculos - Adiciona um novo óculos.
- GET /oculos/<id> - Retorna detalhes de um óculos específico.
- PUT /oculos/<id> - Atualiza informações de um óculos.
- DELETE /oculos/<id> - Remove um óculos.
Renderização de Páginas HTMLAlém da API, o projeto inclui páginas HTML para exibição e gerenciamento de dados usando Jinja2:- GET / - Página inicial.
- GET /oculos - Exibe a lista de óculos disponíveis.
- GET /oculos/<id> - Exibe detalhes de um óculos.

Observação
📌 A API está disponível na branch master deste repositório. Certifique-se de estar nesta branch ao clonar o projeto.

