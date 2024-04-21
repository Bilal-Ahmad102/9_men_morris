from utils import *


def AI_VS_HUMAN(heuristic1):

    board = []
    for i in range(24):
        board.append("x")

    # board = generateRandomBoard_stage2()
    evaluation = evaluate()
    print("Stage 1")
    for i in range(9):

        printBoard(board)
        count(board)
        m = int(input("Enter your Move: "))
        while(True):
            possibleMoves = possibleMoves_stage1(board,True)
            if 0<=m<24:
                test_board = deepcopy(board)
                test_board[m] = "A"    
                if test_board in possibleMoves:
                    board[m] = "A"
                    break
                else:
                    m = int(input("Enter Correct Move(on empty spaces): "))
            else:
                m = int(input("Enter Correct Move(between 0 and 23): "))
        board = remove(board,m)

        board[m] = "A"
        h = heuristic1(board,True)

        if h == float('inf'):
            print("Human WON!!!!!!!!")
            exit(0)

        printBoard(board)
        count(board)
        evalBoard = minimax(
            board, ai_depth, False, alpha, beta, True, heuristic1)

        if evalBoard.evaluate == float('-inf'):
            print("AI Bot 2 has won!")
            exit(0)
        else:
            board = evalBoard.board

    print("Stage 2")
    while True:

        printBoard(board)
        count(board)
        selection = []
        player_position = []
        for i in range(24):
            if board[i] == "A": player_position.append(i)
        for player in player_position:
            ad = [board[i] for i in adjacentLocations(player)]
            if "x" in ad:
                selection.append(player)
        print(selection)
        m = int(input("Enter your player: "))

        while(True):
            if m  in selection:
                break
            else:
                m = int(input("Enter your player: "))

        empty_space = []
        for player in adjacentLocations(m):
            if board[player]=="x":
                empty_space.append(player)

        print(f"empty : {empty_space}")
        goal = int(input("Enter the destination: "))
        while(True):
            if goal in empty_space: break
            else: goal = int(input("Enter the destination: "))


        board[m]    = "x"
        board = remove(board,goal)
        board[goal] = "A"

        if h == float('inf'):
            print("Human WON!!!!!!!!")
            exit(0)

        printBoard(board)
        count(board)        
        evaluation = minimax(
            board, ai_depth, False, alpha, beta, False, heuristic1)

        if evaluation.evaluate == float('-inf'):
            print("AI Bot 2 has won")
            exit(0)
        else:
            board = evaluation.board

def remove(board,m,isStage1=True):
    
        if isMill(m,board) == True:
            print("Taking out: ")
            copy = deepcopy(board)
            boardlist,bs = removePiece(copy,[],"A",True)
            while(True):
                print(bs)
                selected_index = int(input("Selected Index of B to take Out(enter from 0 to n 'index'): "))
                if selected_index < len(bs):                
                    board = boardlist[selected_index]
                    break
        return board

AI_VS_HUMAN(potentialMillsHeuristic)
