# SERVIDOR COM ORIENTADO OBJETO
from threading import Thread
import socket



#udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class Th(Thread):
	def __init__(self, func, args=()):
		Thread.__init__(self)
		self.func = func
		self.args = args

	def run(self):
		self.func(*self.args)

#def Servidor_1(HOST, PORT)
def trat(udp, msg, client):
	msg = msg.decode('utf8')
	clients, port = client 
	if (msg == '-p'):
		mensg = 'Pong - Cliente: %s  Porta: %d  ' % (clients, port)
		udp.sendto(str(mensg).encode(), client)
	
	
	
	print('%s 	\t- Cliente: %s Port: %d'%(msg, clients, port))


sc = socket.socket()
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = ('192.168.1.251', 65025)
udp.bind(origem)

while True:
	msg,client = udp.recvfrom(1024)
	Th(trat,(udp,msg,client)).start()
	
	
	if msg.decode('utf8') == 'q':
		break
udp.close()
sc.close()



