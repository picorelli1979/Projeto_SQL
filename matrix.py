import sqlite3

class Database():      
    def __init__(self, nome_db):
        self.nome_db = nome_db
        self.conn = None
        self.cursor = None
        
    def conecta_db(self):
        self.conn = sqlite3.connect(self.nome_db)
        self.cursor = self.conn.cursor()
        
        return(f'CONECTADO!!!')
    
    def desconecta_db(self):
        self.conn.close()
        
        return(f'DESCONECTADO !!!')
                

# CRIANDO AS TABELAS :

    def create_table(self):  
        self.conecta_db()
        
        self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS clientes(
                                id INTEGER PRIMARY KEY,
                                nome VARCHAR(20) NOT NULL, 
                                cpf INTEGER NOT NULL);
                            ''')
    
        self.conn.commit()
        self.desconecta_db()
        
                
# AQUI ABAIXO VAI ACONTECER O CRUD (CRIAR, LER, ATUALIZAR, DELETAR)  
      
#===================================================================         
        
# METODO DE INSERIR CLIENTE :   CRIAR O CLIENTE 
        
    def insert_dados_clientes(self, id_cliente,nome_cliente,cpf_cliente):
        self.conecta_db()
        
        self.cursor.execute('''INSERT INTO clientes(id,nome,cpf) VALUES (?,?,?);''',(id_cliente,nome_cliente,cpf_cliente))
        
        self.conn.commit()
        self.desconecta_db()
        return(f'CLIENTES INSERIDOS NA TABELA !!!!')

# METODO DE CONSULTAR OS CLIENTES : LER O CLIENTE    
    
    def consultar_todos_clientes(self):
        self.conecta_db()
        
        return self.cursor.execute(f'''SELECT * FROM clientes;''').fetchall()
    
    def consultar_nome_cliente(self, nome_cliente):
        self.conecta_db()
        
        return self.cursor.execute(f'''SELECT * FROM clientes WHERE nome = ? ;''',(nome_cliente)).fetchall()    
                                       
# METODO DE ATUALIZAR DADOS DO CLIENTE : ATUALIZAR O CLIENTE  

    def update_dados_clientes(self, id_cliente, novo_nome_cliente, novo_cpf_cliente):
        self.conecta_db()
        
        self.cursor.execute(f'''UPDATE clientes SET nome = ?, cpf = ? , WHERE id_cliente = ?;''',(id_cliente,novo_nome_cliente,novo_cpf_cliente))
        
        self.conn.commit()
        self.desconecta_db()
        return (f'INFORMAÇÕES ALTERADAS COM SUCESSO !!!!')

# METODO DE DELETAR O CLIENTE PELO ID  :   DELETAR O CLIENTE   
    
    def delete_cliente_pelo_id(self,id_cliente):
        self.conecta_db()
        
        self.cursor.execute(f'''DELETE FROM clientes  WHERE id = ?;''',(id_cliente,))
        
        self.conn.commit()
        self.desconecta_db()
        return (f'CLIENTE FOI APAGADO DO BANCO COM SUCESSO !!!!')
         
# AQUI ACIMA TODOS OS METODOS REFEREM-SE A TABELA DE CLIENTES
#========================================================================================================================= 
    
    
    
    
    