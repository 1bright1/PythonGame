import socket
import  pickle #allows you to serialize objects into 0's and 1's and send it over the nect work, decompose and turn it back into an object
# coding the client side of the network. In other words allowing client to connect to the server. Will we be testing and sending info to the server as well as receiving info from the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.2.14"
        self.port = 5555
        self.addr = (self.server, self.port)
        #self.id = self.connect() # sending an ID (a string) to our clients to know if they are player 1 or 2 or just of they are connected
        #print(self.id)
        self.play = self.connect() #when we first connect to our server, the server should return to each of our clients the starting position (pos) of their player cuz starting position depends if they are player one or two

    def getPlay(self):
        return self.play

    def connect(self):
        try:
            self.client.connect(self.addr) # client to connect to server so that client can recieve info from the server. Once connected we will return that string "Connected" in server.py line 21 which is done below
            return pickle.loads(self.client.recv(2048)) # pickle.loads is to load byte data and the size is 2048 bits
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))  # Send position data to the server
            return pickle.loads(self.client.recv(2048))  # Receive and deserialize server response
        except socket.error as e:
            print(e)


#we dont need these below anymore. it was just for testing
# n = Network()
# print(n.send("hello"))
# print(n.send("working"))

#note when you want to run this you must run server.py first.

