
```
 ____  _____    _    ____  __  __ _____ 
|  _ \| ____|  / \  |  _ \|  \/  | ____|
| |_) |  _|   / _ \ | | | | |\/| |  _|  
|  _ <| |___ / ___ \| |_| | |  | | |___ 
|_| \_\_____/_/   \_\____/|_|  |_|_____|
				     _                                              _        _   
				 ___(_)___ _ __ ___   _____   __     ___  ___   ___| | _____| |_ 
				/ __| / __| '_ ` _ \ / _ \ \ / /____/ __|/ _ \ / __| |/ / _ \ __|
				\__ \ \__ \ | | | | | (_) \ V /_____\__ \ (_) | (__|   <  __/ |_ 
				|___/_|___/_| |_| |_|\___/ \_/      |___/\___/ \___|_|\_\___|\__|

```
This project opens a socket to receive data from a remote hardware and connection to a database to save the data. PROJECT Sismov. 

    Ps. Description in PT-BR
------------------------------------------------------------------------
## Descrição
Desenvolvido em Python v2.7.12 utilizando como base a biblioteca psycopg2, curses e socket. 

##### Imagem do software: 
![alt tag](https://cloud.githubusercontent.com/assets/15522193/18116163/67d47fc0-6f13-11e6-9593-f91dd9bb03bc.png)

Sistema Operacional: Ubuntu 16.04 LTS 

O software recebe os dados de um dispositivo para monitoramento veicular que é integrado a interface de diagnostico do veiculo. Os dados são recebidos e separados por um caractere '#' utilizando a função _split()_, e então os dados são salvos em um banco de dados PostgreSQL.  

Software desenvolvido para o projeto de graduação no curso de Engenharia de Computação.

### Etapas de desenvolvimento:
		- Estudo da biblioteca socket
		- Implementação do socket
		- Tratamento de erros do socket
		- Implementação da interface utilizando curses
		- Tratamento de erros do curses
		- Implementação da conexão com o banco de dados
		- Tratamento de erros do banco de dados
        
------------------------------------------------------------------------	
### Utilização
        - Instale (se não estiver instalado) a biblioteca "psycopg2" com o comando: "sudo apt-get install python-psycopg2";
        - Configure o arquivo configBD.json com as suas configurações do banco de dados;
        	(confira o template no arquivo 'configBD(example).json')
        - Execute o arquivo py.py
        
------------------------------------------------------------------------		
### Estrutura de diretórios
	.
	|-- socketPython
	|	|-- pg.py (codigo em python)
	|	|-- configBD(example).json (template do arquivo de configuração com o BD)
	
------------------------------------------------------------------------
### Comandos
	Comando			Descrição
    CTRL-C          Encerra execução

(a medida que forem atualizados os comandos, eles podem ser vistos na ultima linha do programa)

-------------------------------------------------------------------------
### Detalhes
Este projeto faz parte do projeto SISMOV, que consiste em um sistema de monitoramento veicular, onde foi desenvolvida a parte de hardware e software.
![pcb_sim](https://cloud.githubusercontent.com/assets/15522193/23223502/fec2436a-f909-11e6-9f18-c49714e767bc.png)
![placa-montada-antena](https://cloud.githubusercontent.com/assets/15522193/23223503/fec3d446-f909-11e6-8b81-4ca39b395a36.jpg)
![ps_dtop](https://cloud.githubusercontent.com/assets/15522193/23223670/6b04de0c-f90a-11e6-8f2b-88aae639bd3d.png)
