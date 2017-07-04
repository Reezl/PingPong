import socket, time

HOST = '192.168.1.251'
PORT = 65025

sc = socket.socket()
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST,PORT)

def p(mil):
	nmsg, cliente = udp.recvfrom(1024)
	mil_pong = int(round(time.time()*1000))
	TIMESTAMP = mil_pong - mil
	nmsg = str(nmsg.decode()) +'TimeStamp ' +  str(TIMESTAMP)

	return nmsg
while True:
	msg = input(">> ")
	if msg == 'q':
		udp.sendto(msg.encode(),dest) # Enviando / codificando a mensagem em bytes
		break


	#msg += ''+mil

	udp.sendto(msg.encode(),dest)
	if msg == '-p':
		mil = int(round(time.time() * 1000))
		print(p(mil))

udp.close()
sc.close()
