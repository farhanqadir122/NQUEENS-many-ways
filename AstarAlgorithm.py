import copy
import heapq
import random
import time
from typing import List

from test import draw_board

class State:
    #A state of a chessboard
    def __init__(self, N):
        self.queen_rows = [random.randrange(N) for i in range(N)]
        self.heuristic = self.AttackPairs()
        self.g = 0
        self.f = self.heuristic + self.g
        self.parent = None

    #The heuristic value calculated by checking rows and diagonals to look for attacking pairs of queens
    def AttackPairs(self):
        N = len(self.queen_rows)
        attackingPairs = 0
        for i in range(N):
            # queen_pos = (self.queen_rows[i], i)
            for j in range(i + 1, N):
                if self.queen_rows[i] == self.queen_rows[j]:
                    attackingPairs += 1
                else:
                    # nextcolqueen_pos = (self.queen_rows[j], j)
                    diagonal_row = abs(self.queen_rows[i] - self.queen_rows[j])
                    diagonal_col = abs(i - j)
                    if diagonal_col == diagonal_row:
                        attackingPairs += 1
        return attackingPairs

    def updateCost(self):
        self.g += 1
        self.f = self.heuristic + self.g

    def __eq__(self, other):
        return self.queen_rows == other.queen_rows

    def __str__(self):
        return f'Queen Rows: {self.queen_rows} | h(n): {self.heuristic} | g(n): {self.g} | f(n): {self.f}'

    def __lt__(self, other):
        return self.f < other.f


class AlgoFunctions:

    @staticmethod
    def randomState(N):
        return State(N)

    @staticmethod
    def childStates(openStates: List[State], closedStates: List[State], currentState: State):
        #Generate child states by shifting one queen of each state by one column and taking the edge cases into account
        queenRows = currentState.queen_rows
        N = len(queenRows)
        childrenStates = []
        i = 0
        while i < N:
            if queenRows[i] > 0:
                childState1 = copy.deepcopy(currentState)
                childState1.parent = currentState
                childState1.queen_rows[i] = queenRows[i] - 1
                childState1.heuristic = childState1.AttackPairs()
                childState1.updateCost()
                if childState1 in closedStates:
                    del childState1
                elif childState1 in openStates:
                    for x in openStates:
                        if childState1 == x:
                            if childState1.g > x.g:
                                openStates.remove(x)
                                childrenStates.append(childState1)
                else:
                    childrenStates.append(childState1)

            if queenRows[i] < N - 1:
                childState2 = copy.deepcopy(currentState)
                childState2.parent = currentState
                childState2.queen_rows[i] = queenRows[i] + 1
                childState2.heuristic = childState2.AttackPairs()
                childState2.updateCost()
                if childState2 in closedStates:
                    del childState2
                elif childState2 in openStates:
                    for x in openStates:
                        if childState2 == x:
                            if childState2.g > x.g:
                                openStates.remove(x)
                                childrenStates.append(childState2)
                else:
                    childrenStates.append(childState2)
            i += 1
        return childrenStates

    @staticmethod
    def goalReachCheck(state: State):
        return state.heuristic == 0

    def printBestPath(goalState: State):
        #recursive function that can print the best path from the starting state to the goal state by using its parent(inspired by LinkedList)
        if goalState.parent is None:
            return
        else:
            AlgoFunctions.printBestPath(goalState.parent)
            print(goalState)
            # draw_board(goalState.queen_rows)


class runAlgo:
    @staticmethod
    def run_algo(N_queens):
        #Generate random states and keep a close state list that contains visited states and open list containing nodes to be visited
        #priority queue is used to maintain the open list to know the least cost node to pop and test
        closedStates: List[State] = []
        openStates: List[State] = []
        goalReach = False
        steps = 1
        startTime = time.time()

        startState: State = AlgoFunctions.randomState(N_queens)
        openStates.append(startState)
        heapq.heapify(openStates)

        while len(openStates) != 0 and not goalReach:
            currentBestState = heapq.heappop(openStates)
            print(f'Current Best State: {currentBestState}')
            closedStates.append(currentBestState)

            if AlgoFunctions.goalReachCheck(currentBestState):
                print(f'GOAL STATE => {currentBestState}')
                finish_time: float = time.time()
                time_taken: float = finish_time - startTime

                if not goalReach:
                    steps -= 1

                print(f'Total Steps: {steps} | Time taken: {time_taken}')
                print(f'Best Path:')
                print(startState)
                goalReach = True
                AlgoFunctions.printBestPath(currentBestState)
                break
            else:
                child_states: List[State] = AlgoFunctions.childStates(openStates, closedStates, currentBestState)
                openStates.extend(child_states)
                heapq.heapify(openStates)
            steps += 1
        else:
            print('SOLUTION NOT FOUND!')

        return currentBestState.queen_rows
