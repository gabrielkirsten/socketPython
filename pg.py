#! /usr/bin/env python
#coding: utf-8
import sys, os, socket, curses, datetime, time, psycopg2, json

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

#ininia a tela do curses
myscreen = curses.initscr()

dims = myscreen.getmaxyx() 																					#obtem os valores do tamanho da janela
curses.start_color()																						#inicia as cores da janela
#cores do terminal --------------------------------------------------------------
curses.init_pair(1, 227, curses.COLOR_BLACK)															
curses.init_pair(2, 51, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
#fim cores do terminal ----------------------------------------------------------
curses.noecho() 		#não imprime caracteres digitados
myscreen.border(0)		#define a borda da janela
#mesangens janela ---------------------------------------------------------------
myscreen.addstr(0, (dims[1]/2)-(24/2), " SISMOV SOCKET SOFTWARE ", curses.A_BOLD | curses.color_pair(1))
myscreen.addstr((dims[0]-2), 1, " CTRL+C ") 
myscreen.addstr((dims[0]-2), 1+8,"finaliza execucao", curses.color_pair(3))
myscreen.addstr((dims[0]-2), 1+8+18,"")
myscreen.addstr((dims[0]-1), (dims[1]-37), " desenvolvido por: Gabriel Kirsten ")
#fim mesangens janela -----------------------------------------------------------
#mensagens de progresso ---------------------------------------------------------
myscreen.hline(1, 1, curses.ACS_HLINE, dims[1]-2, curses.color_pair(2))
myscreen.addstr(1, 5, " Inicializacao ", curses.color_pair(1) | curses.A_BOLD)
myscreen.refresh()
myscreen.addstr(3, 1, "  > Iniciando socket | PORT:")
myscreen.addstr(3, 30, str(PORT), curses.A_BOLD)
myscreen.refresh()
try:																										#try abertura de socket
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	orig = (HOST, PORT)
	tcp.bind(orig)
	tcp.listen(1)
except socket.error, msg:
	curses.endwin()
	print "Couldnt connect with the socket-server: %s\n terminating program" % msg
	sys.exit(1)
try:																										#try do JSON
	with open('configBD.json', 'r') as outfile:
		data = json.load(outfile)
except:
	curses.endwin()
	print "JSON ERROR"
	sys.exit(1)
try:																										#try conexão banco
	conn = psycopg2.connect("dbname='"+data['dbname']+"' user='"+data['user']+"' host='"+data['host']+"' password='"+data['password']+"'")
except:
	curses.endwin()
	print "Unable to connect to the database"
	sys.exit(1)
cur = conn.cursor()																							#inicia o cursor do BD
myscreen.addstr(4, 1, "  > Conexao OK.. Aguandando conexao na porta " + str(PORT))					
myscreen.refresh()
myscreen.hline(6, 1, curses.ACS_HLINE, dims[1]-2, curses.color_pair(2))
#titulos ------------------------------------------------------------------------
myscreen.addstr(6, 5, " Log de Conexoes ", curses.color_pair(1) | curses.A_BOLD)
myscreen.hline(7, 1, " ", dims[1]-2, curses.color_pair(3))
myscreen.addstr(7, 1, " IP/PORTA\t\t\tSTATUS ",  curses.A_BOLD|curses.color_pair(3))	
myscreen.refresh()
myscreen.hline(15, 1, curses.ACS_HLINE, dims[1]-2, curses.color_pair(2))
myscreen.addstr(15, 5, " Mensagens ", curses.color_pair(1) | curses.A_BOLD)
myscreen.hline(16, 1, " ", dims[1]-2, curses.color_pair(3))
myscreen.addstr(16, 1, " IP/PORTA\t\t\tHORA\t\t\tMENSAGEM ",  curses.A_BOLD|curses.color_pair(3))	
myscreen.refresh()
#fim titulos --------------------------------------------------------------------
key=-1
try:
    try:
        key=scr.getkey()
    except:
        while True:
			try:																						#tenta realizar uma conexão com o BD
				con, cliente = tcp.accept()
				myscreen.addstr(8, 1, " ")
				myscreen.clrtoeol()
				myscreen.addstr(8, 1, str(cliente) + "\t\tCONECTADO")
				myscreen.refresh()
				while True:
					msg = con.recv(1024)
					if not msg: break
					ts = time.time()
					st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')				#data atual no formato do POSTGRESQL
					msgsplit = msg.rstrip('\n').split('#')
					try:
						#query do BD
						cur.execute("INSERT INTO mensagem VALUES(default, "+msgsplit[0]+", '"+st+"', "+msgsplit[1]+", "+msgsplit[2]+", "+msgsplit[3]+", "+msgsplit[4]+", "+msgsplit[5]+", "+msgsplit[6]+", "+msgsplit[7]+");")
						conn.commit()																	#commit nas alterações
						myscreen.addstr(17, 1, " ")														#limpa a janela
						myscreen.clrtoeol()
						myscreen.addstr(17, 1, str(cliente) + "\t\t" + st + "\t" + msg)
					except psycopg2.ProgrammingError, msg:
						myscreen.addstr(17, 1, " ")														#limpa a janela
						myscreen.clrtoeol()
						myscreen.addstr(17, 1, "ERROR psql", curses.A_BOLD|curses.color_pair(4))
					except psycopg2.IntegrityError, msg:
						myscreen.addstr(17, 1, " ")														#limpa a janela
						myscreen.clrtoeol()
						myscreen.addstr(17, 1, "ERROR Integrity", curses.A_BOLD|curses.color_pair(4))
					except psycopg2.InternalError, msg:
						myscreen.addstr(17, 1, " ")														#limpa a janela
						myscreen.clrtoeol()
						myscreen.addstr(17, 1, "ERROR Internal", curses.A_BOLD|curses.color_pair(4))
					except IndexError:
						myscreen.addstr(17, 1, " ")														#limpa a janela
						myscreen.clrtoeol()
						myscreen.addstr(17, 1, "ERROR msg", curses.A_BOLD|curses.color_pair(4))
					myscreen.refresh()
				myscreen.addstr(8, 1, " ")																#limpa a janela
				myscreen.clrtoeol()
				myscreen.addstr(8, 1, str(cliente) + "\t\tDESCONECTADO")
				myscreen.refresh()
				con.close() 																			#encerra a conexão com o socket
			except socket.error, msg:
				pass
	
except KeyboardInterrupt:																				#encerra execução se for pressionado CTRL-C
	curses.endwin()
	conn.close()
	print "finalizando..."
	sys.exit(1)
