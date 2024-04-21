from utils import *


def min_vs_monte(heuristic1):

    board = []
    for i in range(24):
        board.append("x")
    # board = generateRandomBoard_stage2()
    evaluation = evaluate()
    print("Stage 1")
    for i in range(9):

        printBoard(board)
        count(board)
        print("Monte turn: ")
        
        board = mc(board,"A",1,100)
        h = heuristic1(board,True)

        if h == float('inf'):
            print("Monte WON!!!!!!!!")
            exit(0)

        printBoard(board)
        count(board)
        print("Min_max turn: ")

        evalBoard = minimax(
            board, ai_depth, False, alpha, beta, True, heuristic1)

        if evalBoard.evaluate == float('-inf'):
            print("Min-Max has won!")
            exit(0)
        else:
            board = evalBoard.board

    print("Stage 2")
    while True:
        count(board)
        printBoard(board)
        print("Monte turn: ")
        board = mc(board,"A",0,100)
        h = heuristic1(board,True)

        if h == float('inf'):
            print("Monte WON!!!!!!!!")
            exit(0)

        count(board)
        printBoard(board)
        print("Min_max turn: ")
        evaluation = minimax(
            board, ai_depth, False, alpha, beta, False, heuristic1)

        if evaluation.evaluate == float('-inf'):
            print("Min-Max has won")
            exit(0)
        else:
            board = evaluation.board


min_vs_monte(potentialMillsHeuristic)
