'''
MIN MAX ALGORITHM (https://www.youtube.com/watch?v=fInYh90YMJU)
-----------------

- Designed for perfect information games (eg: chess, checkers)
- Solves for best move of each player (during their turn)

LOGIC
-----

- Generate tree of all possible moves
- Each position or node of the tree holds a Heuristic Value
- Algo goes to the bottom of the tree and works its way upwards

IMPLEMENTATION (STICK GAME)
---------------------------

- Each player takes turns to pick up either 1 or 2 sticks
- Goal is to pick up the last stick
- If you try to pick up two when only one remains, you lose
'''

from sys import maxsize # TO GET THE CLOSEST VALUE NEAR INFINITY, JUST A REALLY BIG / SMALL NUMBER (FOR -VE INFINITY)

# TREE BUILDER
# ------------

class Node(object): # EACH INDIVIDUAL ELEMENT OF THE TREE
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value = 0):
        self.i_depth = i_depth # DEPTH IN TREE, REPRESENTED IN INTEGER (ROOT IS 0)
        self.i_playerNum = i_playerNum # PLAYER NUMBER (EITHER +1 OR -1)
        self.i_sticksRemaining = i_sticksRemaining 
        self.i_value = i_value # VALUE OF EACH NODE (GAME STATE, EITHER -VE INFINITY, 0, OR +VE INFINITY)
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0: # DEPTH CAN'T BE IN NEGATIVE NO. LOL (STOPS THE RECURSION)
            for i in range(1, 3): # HOW MANY STICKS WE GONNA BE REMOVING
                v = self.i_sticksRemaining - i 
                self.children.append(Node(self.i_depth - 1, -self.i_playerNum, v, self.RealVal(v)))
                # KEEPS CREATING CHILDREN UNTIL DEPTH OF 0 IS REACHED
                # -self.i_playerNum -> REPRESENTS THE PLAYER BEING CHANGED (IE, FROM +1 TO -1, VICE VERSA)

    def RealVal(self, value): # DETERMINES THE VALUE OF THE GAME (WINNER, LOSER, OR IF OVERDRAWN)
        if (value == 0):
            return maxsize * self.i_playerNum
        elif (value < 0):
            return maxsize * -self.i_playerNum
        return 0

# ALGORITHM
# ---------

def MinMax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize): # CHECK TO SEE IF DEPTH IS 0, OR NODE IS WIN / LOSE CONDITION
        return node.i_value # RETURN VALUE OF THE BOTTOM MOST NODE
    
    i_bestValue = maxsize * -i_playerNum # STARTING CASE (IF YOU'RE OPITIMISING FOR +VE, THEN -VE INFINITY WOULD BE YOUR START CASE, AND VICE VERSA)
    
    for i in range(len(node.children)): #ITERATE THROUGH ALL CHILDREN AND RUN ALGO ON THEM
        child = node.children[i]
        i_val = MinMax(child, i_depth - 1, -i_playerNum) # FLIPPING PLAYER 
        if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
            # CHECKS THE DISTANCE FROM WHERE WE WANT TO BE VS WHERE WE CURRENTLY ARE (i_val)
            i_bestValue = i_val # IF ITS CLOSER, THEN WE STORE THAT VALUE AND RETURN IT
    
    return i_bestValue

# IMPLEMENTATION
# --------------

def WinCheck(i_sticks, i_playerNum): # WIN OR LOSE CHECKER
    if i_sticks <= 0:
        print("*" * 30)
        if i_playerNum > 0: 
            if i_sticks == 0:
                print("\tYOU WIN!")
            else:
                print("\tTOO MANY! YOU LOSE")
        else:
            if i_sticks == 0:
                print("\tCOMPUTER WINS!")
            else:
                print("\tCOMPUTER ERROR!")
        print("*" * 30)
        return 0 # RETURNS 0, IF SOMEONE WINS / LOSES (IE, GAME OVER!)
    return 1 # RETURNS 1, IF THE GAME IS STILL GOING ON

if __name__ == '__main__': # CHECKS TO SEE IF THIS FILE IS THE MAIN FILE BEING RUN
    i_stickTotal = 11 # DEFAULTS: NO. OF STICKS AT START, 
    i_depth = 4 # DEPTH WE WANT THE COMPUTER TO CALCULATE TO,
    i_curPlayer = 1 # CURRENT STARTING PLAYER (HUMAN)
    print(""" INSTRUCTIONS: BE THE PLAYER TO PICK UP THE LAST STICK
          \t\t\tYOU CAN ONLY PICK UP ONE(1) OR TWO(2)
          \t\t\tSTICKS AT A TIME!""")
    while(i_stickTotal > 0): # AS LONG AS THERE ARE STICKS, KEEP ITERATING
        print("\n%d STICKS REMAIN. HOW MANY WOULD YOU LIKE TO PICK UP?" %i_stickTotal)
        i_choice = input("\n1 OR 2: ")
        i_stickTotal -= int(float(i_choice)) # SUBTRACT HOW MANY STICKS THE PLAYER CHOSE TO REMOVE
        if WinCheck(i_stickTotal, i_curPlayer): # WINCHECK TO SEE IF THE PLAYER HAS WON
            i_curPlayer *= -1 # NEXT PLAYER PLAYS (COMPUTER)
            node = Node(i_depth, i_curPlayer, i_stickTotal) #CREATE TREE FOR ALGO TO RUN ON
            bestChoice = -100 
            i_bestValue = -i_curPlayer * maxsize
            for i in range(len(node.children)): # SAME AS THE PART IN THE ALGORITHM
                n_child = node.children[i]
                i_val = MinMax(n_child, i_depth, -i_curPlayer)
                if (abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue)):
                    i_bestValue = i_val
                    bestChoice = i
            bestChoice += 1
            print("COMPUTER CHOOSES: " + str(bestChoice) + "\tBASED ON VALUE: " + str(i_bestValue))
            i_stickTotal -= bestChoice # REDUCE STICK TOTAL BY AMOUNT THAT THE COMPUTER CHOSE
            WinCheck(i_stickTotal, i_curPlayer)
            i_curPlayer *= -1