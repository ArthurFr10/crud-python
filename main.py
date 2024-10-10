import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#criando tabela

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    #definindo campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    
    #definindo atributos da classe
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)


#salvar no banco de dados
os.system("cls || clear")

#create
print("Solicitando dados para o usuário")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")


usuario = Usuario(nome="Marta", email="marta@gmail.com", senha="123")
session.add(usuario)
session.commit()


usuario = Usuario(nome="Marta", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

#listando todos os usuários do banco de dados
print("\nExibindo todos os usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

#delete
print("\nExcluindo um usuário")
email_usuario = input("Informe o email do usuário para ser excluído: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluído com sucesso")

#listando todos os usuários do banco de dados
print("\nExibindo todos os usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")


#update
print("\nAtualizando dados do usuário")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = Usuario(
    nome = input("Digite seu nome: "),
    email = input("Digite seu email: "),
    senha = input("Digite sua senha: ")
)

usuario = novos_dados
session.add(usuario)
session.commit()

#fechando conexão
session.close()