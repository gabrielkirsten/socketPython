# socketPython
This project opens a socket to receive data from a remote hardware and connection to a database to save the data. PROJECT Sismov. 

    Ps. Description in PT-BR
------------------------------------------------------------------------
##Descrição
Desenvolvido em Python v2.7.12 utilizando como base a biblioteca psycopg2, curses e socket.
Sistema Operacional: Ubuntu 16.04 LTS 

O software recebe os dados de um dispositivo para monitoramento veicular que é integrado a interface de diagnostico do veiculo. Os dados são recebidos e separados por um caractere '#' utilizando a função _split()_, e então os dados são salvos em um banco de dados PostgreSQL.  

######Imagem do software 
![alt tag](https://cloud.githubusercontent.com/assets/15522193/18116163/67d47fc0-6f13-11e6-9593-f91dd9bb03bc.png)

Software desenvolvido para o projeto de graduação no curso de Engenharia de Computação.

	**Etapas de desenvolvimento:
		- Estudo da biblioteca socket
		- Implementação do socket
		- Tratamento de erros do socket
		- Implementação da interface utilizando curses
		- Tratamento de erros do curses
		- Implementação da conexão com o banco de dados
		- Tratamento de erros do banco de dados
        
------------------------------------------------------------------------	
##Utilização
        - Instale (se não estiver instalado) a biblioteca "psycopg2" com o comando: "sudo apt-get install python-psycopg2";
        - Configure o arquivo configBD.json com as suas configurações do banco de dados;
        	(confira o template no arquivo 'configBD(example).json')
        - Execute o arquivo py.py
        
------------------------------------------------------------------------		
##Estrutura de diretórios
	.
	|-- socketPython
	|	|-- pg.py (codigo em python)
	|	|-- configBD(example).json (template do arquivo de configuração com o BD)
	
------------------------------------------------------------------------
##Comandos
	Comando			Descrição
    CTRL-C          Encerra execução

(a medida que forem atualizados os comandos, eles podem ser vistos na ultima linha do programa)

-------------------------------------------------------------------------
