from Games import Games
      
try:
    game = Games()
    game.menu()
except(Exception):
    print("An error occured. Please try again.")
    game.menu()
    

