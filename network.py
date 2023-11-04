import socket
import pickle


class Network:
    def __init__(self):
        # print('asddasdassda')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.71"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def get_pos(self):
        return self.pos

    def connect(self):
        # print('trying')
        try:
            self.client.connect(self.addr)
            print('worked')
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)

    def send(self, obj):
        try:
            b = pickle.dumps(obj)
            self.client.send(b)

            # return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


n = Network()

# s = 'asddsadsa'

# pickle.dumps(s)
