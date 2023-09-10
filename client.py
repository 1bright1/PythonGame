import pygame
from Network import Network
from Player import Player
import pickle

#creating a window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Client")

def redrawWindow(window, player, player2): # redraw window and player
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


def main(): # main loop for pygame to run continuiosuly checking for event asking the server for info
    run = True
    n = Network() #connecting to the server
    play = n.getPlay()
    clock = pygame.time.Clock()  # use for the speed of player

    while run:
        clock.tick(60) #speed is at 60fps
        play2 = n.send(play)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        play.move(redrawWindow, window, play, play2)
        redrawWindow(window, play, play2)

main()

# how play.move() works
#Yes, in the server.py code snippet you provided, the self.play attribute of the Network class in the client code would be assigned an instance of the Player class. Let's break down how it happens:

# In the server.py code, the players list is initialized with two Player objects: players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))].
#
# When a client connects to the server and the threaded_client() function is called, the server sends the players[player] object (which corresponds to the connected client's player) to the client using conn.send(pickle.dumps(players[player])).
#
# On the client side, in the Network class, the self.play attribute is assigned the object received from the server using self.play = self.connect(). The connect() method receives the pickled data using pickle.loads(self.client.recv(2048)), which effectively reconstructs the Player object on the client side.
#
# Therefore, when the client code calls play.move(), it is calling the move() method of an instance of the Player class that was received from the server.
#
# In summary, the self.play attribute in the Network class of the client code is assigned an instance of the Player class by receiving the pickled Player object from the server.

