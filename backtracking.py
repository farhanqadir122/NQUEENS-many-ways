import time
from collections import deque
from copy import deepcopy
import drawBoard


# Simple class with class variables used for GUI simplicity
class nQueens:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.printableSolution = []
        self.timeTaken = 0

    # Check if current state is safe
    def isSafe(self, col, row, currentState):
        for cols, rows in currentState:
            if (cols, rows) != (col, row):
                if (col + row == cols + rows) or (row - col == rows - cols):
                    return False
                elif row == rows:
                    return False
        return True

    # Simple backtracking with no filtering. A queen is assigned in a row then a column is chosen based on MRV or MCV or
    # just next column. Then for that column, an LCV ordering is created after testing queen assignments in all rows
    # of that column or just next row. Then it keeps testing and backtracking to arrive at the solution.
    def simpleBacktracking(self, col, currentState, unassignedCols, domains, MRV, LCV, MCV):
        print(currentState)
        self.count += 1
        if len(currentState) == self.n:
            return currentState

        for row in domains[col]:
            currentState.add((col, row))
            unassignedCols.remove(col)
            nextCol = col + 1
            isEmpty = False
            if MRV is True:
                isEmpty, updatedDomains, nextCol = self.updateDomains(currentState, unassignedCols, domains)
            if MCV is True:
                isMCVChecked = self.checkMCV(unassignedCols, domains)
            if not isEmpty:
                if LCV and nextCol < self.n:
                    LCVRowOrder = self.getLCVRowOrder(currentState, unassignedCols, domains, nextCol)
                    domains[nextCol] = LCVRowOrder
                if self.isSafe(col, row, currentState) and self.simpleBacktracking(nextCol, currentState,
                                                                                   unassignedCols,
                                                                                   domains, MRV, LCV, MCV) is not None:
                    return currentState
            currentState.remove((col, row))
            unassignedCols.add(col)
        return None

    # Backtracking with Forward Checking. A queen is assigned in a row then the domains are updated with forward
    # checking and then a column is chosen based on MRV or MCV or just next column. Then for that column,
    # an LCV ordering is created after testing queen assignments in all rows of that column or just next row. Then it
    # keeps testing and backtracking to arrive at the solution.
    def BacktrackingFC(self, col, currentState, unassignedCols, domains, MRV, LCV, MCV):
        print(currentState)
        self.count += 1
        if len(currentState) == self.n:
            return currentState

        for row in domains[col]:
            currentState.add((col, row))
            unassignedCols.remove(col)
            isEmpty, updatedDomains, nextCol = self.updateDomains(currentState, unassignedCols, domains)
            if MRV is False:
                nextCol = col + 1
            if not isEmpty:
                if LCV and nextCol < self.n:
                    LCVRowOrder = self.getLCVRowOrder(currentState, unassignedCols, updatedDomains, nextCol)
                    updatedDomains[nextCol] = LCVRowOrder
                if self.BacktrackingFC(nextCol, currentState, unassignedCols, updatedDomains, MRV, LCV,
                                       MCV) is not None:
                    return currentState
            currentState.remove((col, row))
            unassignedCols.add(col)
        return None

    # Backtracking with Arc consistency algorithm. A queen is assigned in a row then the domains are updated with
    # forward checking and then a column is chosen based on MRV or MCV or just next column. Then domains are updated
    # after performing arc consistency algorithm. Then it keeps testing and backtracking to arrive at the solution.
    def BacktrackingAC3MRV(self, col, currentState, unassignedCols, domains, arcs, neighbours, MRV, LCV, MCV):
        print(currentState)
        self.count += 1
        if len(currentState) == self.n:
            return currentState

        for row in domains[col]:
            currentState.add((col, row))
            unassignedCols.remove(col)
            isEmpty, updatedDomains, nextCol = self.updateDomains(currentState, unassignedCols, domains)
            if MRV is False:
                nextCol = col + 1
            if not isEmpty:
                if self.AC3(arcs, domains, neighbours):
                    if self.BacktrackingAC3MRV(nextCol, currentState, unassignedCols, updatedDomains, arcs, neighbours,
                                               MRV,
                                               LCV, MCV) is not None:
                        return currentState
            currentState.remove((col, row))
            unassignedCols.add(col)
        return None

    # Backtracking with Arc consistency algorithm. A queen is assigned in a row then the domains are updated with
    # forward checking and then a column is chosen based on MRV or MCV or just next column. Then domains are updated
    # after performing arc consistency algorithm. Then for that column, # an LCV ordering is created after testing
    # queen assignments in all rows of that column or just next row. Then it keeps testing and backtracking to arrive
    # at the solution.
    def BacktrackingAC3MRVLCV(self, col, currentState, unassignedCols, domains, arcs, neighbours, MRV, LCV, MCV):
        print(currentState)
        self.count += 1
        if len(currentState) == self.n:
            return currentState

        isEmpty, updatedDomains, nextCol = self.updateDomains(currentState, unassignedCols, domains)

        if not isEmpty:
            rowOrder = self.getLCVRowOrder(currentState, unassignedCols, updatedDomains, nextCol)
            for selectedRow in rowOrder:
                currentState.add((nextCol, selectedRow))
                unassignedCols.remove(nextCol)
                if self.AC3(arcs, domains, neighbours):
                    if self.BacktrackingAC3MRVLCV(nextCol, currentState, unassignedCols, domains, arcs, neighbours, MRV,
                                                  LCV, MCV) is not None:
                        return currentState
                currentState.remove((nextCol, selectedRow))
                unassignedCols.add(nextCol)
        return None

    # This function is used to update domains for Forward Checking and also to find the next column for MRV.
    def updateDomains(self, currentState, unassignedCols, domains):
        minSize = self.n + 1
        updatedDomains = deepcopy(domains)
        nextCol = len(currentState)
        for col in unassignedCols:
            possibleDomains = self.getDomain(currentState, domains, col)
            if len(possibleDomains) == 0:
                return True, {}, nextCol
            updatedDomains[col] = possibleDomains
            size = len(possibleDomains)
            if size < minSize:
                nextCol = col
                minSize = size
        return False, updatedDomains, nextCol

    # Helper function that checks safety of current state
    def getDomain(self, currentState, domains, col):
        updatedDomains = []
        for row in domains[col]:
            if self.isSafe(col, row, currentState):
                updatedDomains.append(row)
        return updatedDomains

    # Function to check MCV
    def checkMCV(self, unassignedCols, domains):
        if len(unassignedCols) > 0:
            return True
        else:
            return False

    # Given a column, keep assigning a queen in every row and test the constraints and available queen positions of
    # the following columns to assign an unconstrainedCell value for each and then order by highest to lowest
    def getLCVRowOrder(self, currentState, unassignedCols, updatedDomains, nextCol):
        lcv = []
        rowOrder = []
        tempCurrentState = deepcopy(currentState)
        tempUnassignedCols = deepcopy(unassignedCols)
        for row in updatedDomains[nextCol]:
            tempCurrentState.add((nextCol, row))
            tempUnassignedCols.remove(nextCol)
            unconstrainedCells = 0
            for col in tempUnassignedCols:
                unconstrainedCells += len(self.getDomain(tempCurrentState, updatedDomains, col))
            lcv.append((row, unconstrainedCells))
            tempCurrentState.remove((nextCol, row))
            tempUnassignedCols.add(nextCol)

        lcv = sorted(lcv, key=lambda r: r[1], reverse=True)
        for x in lcv:
            rowOrder.append(x[0])
        return rowOrder

    # After a queen is assigned, create arcs with every other variable and revise the domains according to the algorithm
    def AC3(self, arcs, domains, neighbours):
        arcQueue = deque(arcs)
        while len(arcQueue) != 0:
            arcPair = arcQueue.popleft()
            first = arcPair[0]
            second = arcPair[1]
            if self.revise(arcs, domains, first, second):
                if len(domains[first]) == 0:
                    return False
                for adjacent in neighbours[first]:
                    if adjacent == second:
                        continue
                    arcQueue.append([adjacent, first])
        return True

    # Helper function for AC3 that revises the domains according to AC3 algorithm
    def revise(self, arcs, domains, first, second):
        revised = False
        for firstRows in domains[first]:
            inFlag = False
            for secondRows in domains[second]:
                if self.isValid({first: firstRows}, arcs, second, secondRows):
                    inFlag = True
                    break
            if not inFlag:
                domains[first].remove(firstRows)
                revised = True
        return revised

    # Used to test if current state is safe for the AC3 algorithm
    def isValid(self, assignment, constraints, x, val):
        tempCurrentState = deepcopy(assignment)
        tempCurrentState[x] = val

        for rows in tempCurrentState:
            for cols in tempCurrentState:
                row1 = tempCurrentState[rows]
                col1 = tempCurrentState[cols]
                if rows != cols and (row1 == col1 or rows + row1 == cols + col1 or rows - row1 == cols - col1):
                    return False
        return True

    # The function that is called from the main class and instantiates the variables and calls the required functions
    # according to the provided values.
    def getSolution(self, Filtering, MRV=False, LCV=False, MCV=False):

        unassignedCols = set([i for i in range(self.n)])
        domains = {column: list(range(self.n)) for column in range(self.n)}
        neighbours = {}
        for first in domains.keys():
            neighbours[first] = []

        for f in range(0, self.n):
            for s in range(0, self.n):
                if f == s:
                    continue
                neighbours[f].append(s)

        arcs = []

        for i in neighbours:
            for j in neighbours[i]:
                arcs.append([i, j])

        start = time.time()

        if Filtering == "None":
            solution = self.simpleBacktracking(col=0, currentState=set(), unassignedCols=unassignedCols,
                                               domains=domains, MRV=MRV, LCV=LCV, MCV=MCV)
        elif Filtering == "FC":
            solution = self.BacktrackingFC(col=0, currentState=set(), unassignedCols=unassignedCols,
                                           domains=domains, MRV=MRV, LCV=LCV, MCV=MCV)

        elif Filtering == "AC3MRV":
            solution = self.BacktrackingAC3MRV(col=0, currentState=set(), unassignedCols=unassignedCols,
                                               domains=domains, arcs=arcs, neighbours=neighbours, MRV=MRV, LCV=LCV,
                                               MCV=MCV)

        elif Filtering == "AC3MRVLCV":
            solution = self.BacktrackingAC3MRVLCV(col=0, currentState=set(), unassignedCols=unassignedCols,
                                                  domains=domains, arcs=arcs, neighbours=neighbours, MRV=MRV, LCV=LCV,
                                                  MCV=MCV)

        end = time.time()
        self.timeTaken = end - start
        if solution is not None:
            currentState = sorted(solution, key=lambda row: row[1])
            for tup in currentState:
                self.printableSolution.append(tup[0])
            print(currentState)
        drawBoard.draw_board(self.printableSolution)
