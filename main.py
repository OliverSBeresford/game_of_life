from simulation import Simulation
    
def main():
    sim = Simulation()
    print("press 'p' to pause")
    print("Once the game is paused you can click on cells to make them alive")
    print("To speed up, press the up arrow")
    print("To slow down, press the down arrow")
    print("When paused, press 'r' to create to randomize")
    print("To change colors, use the left and right arrows")
    print("To randomize color, press 'c'")
    sim.start()

if __name__ == "__main__":
    main()