from lib.hands import Hands
import cProfile

def main():
    testHands = Hands(groupname="silver")
    testHands.run()

if __name__ == "__main__":
    cProfile.run('main()', sort="tottime")
