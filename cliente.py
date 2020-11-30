import socket
import threading
import sys
import pickle




class Cliente():
	def __init__(self, host="localhost", port=9000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			"""a = 1
			if a == 1:
				self.send_msg("usuario conectado")"""
			msg = input('->')
			if msg != 'salir':
				self.send_msg(msg)
			else:
				self.send_msg("usuario desconectado")
				self.sock.close()
				sys.exit()
			#a = a + 1

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))


c = Cliente()
