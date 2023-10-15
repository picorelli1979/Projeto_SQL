from matrix import Database

class App:
    def __init__(self):
        
        self.loja = Database('Loja_Auto_Pecas.db')
         
        while True:
            
            print('''
                    ==============================================================
                    ////////////////////CADASTRO DE CLIENTES//////////////////////
                    ==============================================================
                            1. INCLUIR CLIENTE
                            2. ALTERAR CLIENTE 
                            3. EXCLUIR CLIENTE
                            4. CONSULTAR CLIENTE PELO ID 
                            5. CONSULTAR CLIENTE PELO NOME
                            6. CONSULTAR TODOS OS CLIENTES
                            7. SAIR DO SISTEMA
                    ===============================================================
                    ///////////////////////////////////////////////////////////////
                    ===============================================================
                  ''')
    
            Op = int(input('ESCOLHA UMA OPÇÃO:    '))
    
            match Op:                
                case 1 :
                    self.incluir_cliente()
                case 2 :
                    self.alterar_cliente()
                case 3 : 
                    self.excluir_cliente()
                case 4 :
                    self.consultar_cliente_id()
                case 5 :
                    self.consultar_cliente_nome()
                case 6 :
                    self.consultar_todos_clientes()
                case 7 :
                    print('SAINDO DO SISTEMA.......')
                    break                        
                
    def incluir_cliente(self):
        print('--------------INCLUIR CLIENTE -------------------------------')
        id_cliente = int(input("Digite o Id do Cliente:        "))
        nome_cliente = input("Digite o Nome do Cliente:        ")
        cpf_cliente = int(input("Digite o Cpf do Cliente:      "))
        self.loja.insert_dados_clientes(id_cliente,nome_cliente,cpf_cliente)
        print('-------------------------------------------------------------')
            
    def alterar_cliente(self):
        pass    
    
    def excluir_cliente(self):
        pass
    
    def consultar_cliente_id(self):
        pass 
    
    def consultar_cliente_nome(self):
        pass
    
    def consultar_todos_clientes(self):
         for linha in self.loja.consultar_todos_clientes():
          print(linha)
         
#=================================================================================================
if __name__ == '__main__':
   aplicacao = App()    