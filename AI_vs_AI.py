from utils import *


def AI_VS_AI(heuristic1):

    board = []
    for i in range(24):
        board.append("x")

    evaluation = evaluate()
    print("Stage 1")
    for i in range(9):
        count(board)
        printBoard(board)
        print("A Turn :")
        evalBoard = minimax(
            board, ai_depth, True, alpha, beta, True, heuristic1)

        if evalBoard.evaluate == float('inf'):
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board
        count(board)
        printBoard(board)
        print("B Turn :")
        evalBoard = minimax(
            board, ai_depth, False, alpha, beta, True, heuristic1)

        if evalBoard.evaluate == float('-inf'):
            print("AI Bot 2 has won!")
            exit(0)
        else:
            board = evalBoard.board

    print("Stage 2")
    while True:

        count(board)
        printBoard(board)
        print("A Turn :")
        evalBoard = minimax(
            board, ai_depth, True, alpha, beta, False, heuristic1)

        if evalBoard.evaluate == float('inf'):
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board

        count(board)
        printBoard(board)
        print("B Turn :")
        evaluation = minimax(
            board, ai_depth, False, alpha, beta, False, heuristic1)

        if evaluation.evaluate == float('-inf'):
            print("AI Bot 2 has won")
            exit(0)
        else:
            board = evaluation.board


AI_VS_AI(potentialMillsHeuristic)
