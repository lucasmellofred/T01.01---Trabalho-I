import os

resposta = ''
print("Bem vindo, use --help para ajuda")

while resposta != 'end':
    resposta = input(os.getcwd() + "> ")
    if resposta == '--help':
        print(" ")
        print("---------------------- Lista de Comandos Possíveis ------------------------")
        print("|  --help    - Listar todos os comandos                                   |")
        print("|  --version - Mostrar versão atual do software                           |")
        print("|  mkdir     - Criar um diretório                                         |")
        print("|  dltdir    - Deletar um diretório                                       |")
        print("|  cgdir     - Mudar o diretório                                          |")
        print("|  ls        - Listar os subdiretórios no diretório atual                 |")
        print("|  newarv    - Criar um novo arquivo                                      |")
        print("|  delete    - Deletar um arquivo                                         |")
        print("|  end       - Encerrar sessão atual                                      |")
        print("|-------------------------------------------------------------------------|")
        print(" ") 
    elif resposta == '--version':
        print("Versão atual: 0.1") 
    elif resposta.startswith('mkdir'):
        nomeDiretorio = resposta.replace("mkdir ",'')
        os.makedirs(nomeDiretorio) 
        print(" ") 
    elif resposta.startswith('dltdir'):
        nomeDiretorio = resposta.replace("dltdir ",'')
        os.rmdir(nomeDiretorio)
        print(" ")
    elif resposta.startswith('cgdir'):
        nomeDiretorio = resposta.replace("cgdir ",'')
        os.chdir(nomeDiretorio)
        print(" ") 
    elif resposta.startswith('ls'):
        nomeDiretorio = resposta.replace("ls ",'')
        ls = os.listdir()
        print(ls) 
    elif resposta.startswith('newarv'):
        nomeDiretorio = resposta.replace("newarv ",'')
        open(nomeDiretorio,"a")
        print(" ") 
    elif resposta.startswith('delete'):
        nomeDiretorio = resposta.replace("delete ",'')
        os.remove(nomeDiretorio)
        print(" ") 
    elif resposta == 'end':
        print(" ")
    else:
        print("Comando inválido")