# AI-Project-2

Team: Golem
Members:    Brad Bonanno
            Harry Sadoyan
            Alex Taglieri

---

Implement an agent using the minimax algorithm capable of playing Gomoku 

Our beautiful creation is named `golem`

Call `python golem.py` to start the agent
Written in `python3`
If you have aliased python to python2, it's possible to run our program by calling:
py -3 golem.py
(assuming you have python3 installed)


Our beautiful creation has `hands` to interact with the rest of the world,
a `brain` to make decisions, a `frontal_lobe`, and a `body` to act as the 
link between them all.

It uses a minimax algorithm with alpha-beta pruning and a heuristic/evaluation function to evaluate
intermediate board states. We only look at spots on the board that are adjacent to another piece on
the board.
