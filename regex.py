import re
# Leia o conteúdo do arquivo
with open('produtos.txt', 'r') as file:
    linhas = file.readlines()

# Aplique a regex para cada linha e atribua os valores a variáveis
for linha in linhas:
    padrao = r'\b(?:Produto \d|[\d.]+)\b'
    itens = re.findall(padrao, linha)

    # Atribua cada item a uma variável
    produto_nome = itens[0] if itens else None  # Assumindo que o primeiro item é o nome do produto
    quantidade = float(itens[1]) if len(itens) > 1 else None
    preco = float(itens[2]) if len(itens) > 2 else None


 # Imprima as variáveis para cada linha
    print("Nome do Produto:", produto_nome)
    print("Quantidade:", quantidade)
    print("Preço:", preco)
    print("---") 
 # Separador entre conjuntos de itens
