from lib.hands import Hands
import cProfile

def main():
    testHands = Hands()
    testHands.run()

if __name__ == "__main__":
    cProfile.run("main()", sort="tottime")