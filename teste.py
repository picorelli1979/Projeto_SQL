from matrix import Database

loja = Database('Loja_Auto_Pecas.db')

loja.create_table()

loja.insert_dados_clientes(1, 'FABRICIO PAIM', 79228810530)