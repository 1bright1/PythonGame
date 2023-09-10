import socket #using socket and threading to handle connections to our server
from _thread import* #we are going to set up a socket to allow for connections to come in into our server on a certain port
from Player import Player
import pickle



server = "192.168.2.14" #create a server which is in strings. So we will be inputing an ip address in that string. We will be using our IP4v addr as our sever addr which can be find in your command promt
port = 5555 #choose a port in this case port number 5555 was chosen

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # these are just the types of connection. We are going to be connecting to a an IPv4 address.
# so for the parameters socket.AF_INET is just the type for IPv4 connection and socket.SOCK_STREAM represent how the server string comes in

# bind our server and port to the socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)# opens up the port so we can have multiple clients connecting to server. the listen() takes one arguement and its optional. If left blank then unlimited number of clients can connect. For now we want only two people to connect
print("waiting for connection, server started")



players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))] # this list will hold the positions of our players. so player 1 will start at (0,0) and player 2 will start at (100,100). remember Player() is a class. this list creats players


def threaded_client(conn, player): #thread is another process starting in the background like proccess 2 while process 1 is still running. We won't have to wait for process 1 to be done. Meaning we don't have to wait for a connection to finish executing before starting another connection
    conn.send(pickle.dumps(players[player])) #sending it to server
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) #2048 is the amount of bits (amount of info you are trying to recieve). basically you want to recieve some kind of data from our connection. The larger the size of bits the longer it takes to recieve the info.
            players[player] = data
            #reply = data.decode("utf-8") # to decode the info we recieve into strings humans can read and understand
            if not data: # if we not getting any info from client then disconnect and break
                print("Disconnected")
                break
            else: # Send updated player position to the other client
                if player == 1:
                    reply = players[0]  # Serialize the player object
                else:
                    reply = players[1]  # Serialize the player object
                print("recieved: ", data)
                print("sending : ", reply)

            conn.sendall(pickle.dumps(reply))  # Serialize and send position data to client
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0 #
while True: #this loop will continously look for connections. this loop will start a process like process 1
    conn, addr = s.accept() # accept any incoming connection using accept(). note conn is an object representing whats connecting and addr is the adress which is an IP address
    print("connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1 # to keep track of which player we are using so we know what position to update and send to that player based on the connection. There's only going to be 2 players for now so currentplayer will either be 0 or 1

#Pickle in Python is primarily used in serializing and deserializing a Python object structure.
# In other words, it's the process of converting a Python object into a byte stream to store it in a file/database,
# maintain program state across sessions, or transport data over the network

# the pickle_load reads pickled objects from a file, whereas loads() deserializes them from a bytes-like object.

# so pickle_load is like decoding data to readable format while pickle_dumps is like encoding data to bytes for computer language