# Banco de Dados - Projeto Ótica

Este projeto consiste em um banco de dados relacional para gerenciar informações de uma ótica, incluindo materiais, marcas, formas de óculos, óculos disponíveis e vendas realizadas.

## Estrutura do Banco de Dados

O banco de dados contém as seguintes tabelas:

- `projeto_otica_material`: Armazena os materiais dos óculos.
- `projeto_otica_marca`: Contém as marcas disponíveis.
- `projeto_otica_forma`: Define as formas das armações.
- `projeto_otica_oculos`: Registra os óculos disponíveis na ótica.
- `projeto_otica_vendas`: Armazena as informações das vendas realizadas.

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
- **Linguagem**: SQL

## Como Usar

1. **Criação do Banco**: Execute o script SQL para criar as tabelas e definir os relacionamentos.
2. **Inserção de Dados**: Adicione registros às tabelas conforme necessário.
3. **Consultas**: Faça buscas para obter relatórios de vendas, inventário de óculos e outras informações úteis.

## Exemplo de Consulta SQL

```sql
SELECT o.Nome, o.Cor, o.Valor, m.Nome AS Marca
FROM projeto_otica_oculos o
JOIN projeto_otica_marca m ON o.ID_Marca = m.ID_Marca
WHERE o.Valor > 300.00;
