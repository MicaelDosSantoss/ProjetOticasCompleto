
```markdown
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

- **Banco de Dados**: MySQL ou PostgreSQL (compatível com SQL padrão)
- **Back-end**: Flask (Python)
- **Front-end**: HTML + Jinja2
- **ORM**: SQLAlchemy

## API Flask

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/projeto-otica.git
   cd projeto-otica
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```sh
   python app.py
   ```

### Métodos CRUD da API

A API oferece os seguintes endpoints:

- `GET /oculos` - Retorna todos os óculos cadastrados.
- `POST /oculos` - Adiciona um novo óculos.
- `GET /oculos/<id>` - Retorna detalhes de um óculos específico.
- `PUT /oculos/<id>` - Atualiza informações de um óculos.
- `DELETE /oculos/<id>` - Remove um óculos.

Exemplo de implementação do endpoint `GET /oculos`:

```python
@app.route('/oculos', methods=['GET'])
def get_oculos():
    oculos = Oculos.query.all()
    return jsonify([oculo.to_dict() for oculo in oculos])
```

### Conexão com o Banco de Dados

A API utiliza SQLAlchemy para interagir com o banco de dados:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:senha@localhost/projeto_otica'
db = SQLAlchemy(app)
```

## Renderização de Páginas HTML

Além da API, o projeto inclui páginas HTML para exibição e gerenciamento de dados usando Jinja2:

- `GET /` - Página inicial.
- `GET /oculos` - Exibe a lista de óculos disponíveis.
- `GET /oculos/<id>` - Exibe detalhes de um óculos.

Exemplo de renderização de página:

```python
@app.route('/oculos')
def listar_oculos():
    oculos = Oculos.query.all()
    return render_template('oculos.html', oculos=oculos)
```

## Exemplo de Consulta SQL

```sql
SELECT o.Nome, o.Cor, o.Valor, m.Nome AS Marca
FROM projeto_otica_oculos o
JOIN projeto_otica_marca m ON o.ID_Marca = m.ID_Marca
WHERE o.Valor > 300.00;
```

Essa consulta retorna todos os óculos com valor superior a R$ 300, mostrando suas cores e marcas.

## Contribuições

Se desejar melhorar ou expandir este projeto, fique à vontade para sugerir alterações!

---

📌 Esse projeto permite gerenciar dados de uma ótica de forma eficiente, com uma API robusta e páginas HTML dinâmicas. Se precisar de ajustes, me avise! 🚀
```
