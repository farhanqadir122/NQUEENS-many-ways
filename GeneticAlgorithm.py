import random
import time
from typing import List


class State:
#Chess board state
    def __init__(self, N):
        self.queenRows = [random.randrange(N) for i in range(N)]
        self.fitnessValue = self.nonAttackPairs()
#calculating fitness
    def nonAttackPairs(self):
        N = len(self.queenRows)
        maxAttackPairs = (N * (N - 1)) // 2
        attackingPairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                if self.queenRows[i] == self.queenRows[j]:
                    attackingPairs += 1
                else:
                    diagonal_row = abs(self.queenRows[i] - self.queenRows[j])
                    diagonal_col = abs(i - j)
                    if diagonal_col == diagonal_row:
                        attackingPairs += 1
        return maxAttackPairs - attackingPairs

    def __str__(self):
        return f'Queen Rows: {self.queenRows} | Fitness: {self.fitnessValue}'

    def __repr__(self):
        return f'Queen Rows: {self.queenRows} | Fitness: {self.fitnessValue}'


class Population:
#contains a list of states that represents a generation
    def __init__(self, populationSize, N):
        self.generationStates: List[State] = [State(N) for i in range(populationSize)]

    def __str__(self):
        for state in self.generationStates:
            print(state)
        return ''

    def __len__(self):
        return len(self.generationStates)

    def __getitem__(self, item):
        return self.generationStates[item]


class AlgoFunctions:

    @staticmethod
    #Use the random.choice with a probability for each population member to get a good random parent (Similar to roulette selection)
    def getParent(generation: Population, generationProbabilities: List[float]):
        return random.choices(generation, generationProbabilities)[0]

    @staticmethod
    #Crossover the given parents to get two children using single point
    def crossoverSP(parent1: State, parent2: State):
        N = len(parent1.queenRows)
        point = random.randint(1, N - 1)
        child1 = State(N)
        child1.queenRows.clear()
        child2 = State(N)
        child2.queenRows.clear()

        child1.queenRows.extend(parent1.queenRows[0:point])
        child1.queenRows.extend(parent2.queenRows[point:])

        child2.queenRows.extend(parent2.queenRows[0:point])
        child2.queenRows.extend(parent1.queenRows[point:])

        child1.fitnessValue = child1.nonAttackPairs()
        child2.fitnessValue = child2.nonAttackPairs()

        return child1, child2

    @staticmethod
    # Crossover the given parents to get two children using single point
    def crossoverMP(parent1: State, parent2: State):
        N = len(parent1.queenRows)
        point1 = random.randint(1, N // 2)
        point2 = random.randint(point1 + 1, N - 1)
        child1 = State(N)
        child1.queenRows.clear()
        child2 = State(N)
        child2.queenRows.clear()

        child1.queenRows.extend(parent1.queenRows[0:point1])
        child1.queenRows.extend(parent2.queenRows[point1:point2])
        child1.queenRows.extend(parent1.queenRows[point2:])

        child2.queenRows.extend(parent2.queenRows[0:point1])
        child2.queenRows.extend(parent1.queenRows[point1:point2])
        child2.queenRows.extend(parent2.queenRows[point2:])

        child1.fitnessValue = child1.nonAttackPairs()
        child2.fitnessValue = child2.nonAttackPairs()

        return child1, child2

    @staticmethod
    #shift a queen in a random row to a random column as needed from the mutation probability
    def mutateChild(child: State):
        N = len(child.queenRows)
        random_row = random.randint(0, N - 1)
        random_col = random.randint(0, N - 1)
        child.queenRows[random_row] = random_col
        child.fitnessValue = child.nonAttackPairs()
        return child


class runAlgo:
    @staticmethod
    def run_algo(N=4, popSize=100, maxGenerations=60000, mutationProb=0.05,
                 crossover_type='S', crossoverRate=0.6, elitism='N'):

        generation = 1
        solutionState: State = None
        maxFitness = (N * (N - 1)) // 2
        solutionFound = False

        startTime = time.time()

        print("Initial random population:")
        currentPopulation = Population(popSize, N)
        print(currentPopulation)
        print(f'Max Fitness: {maxFitness}')
        print()

        crossoverPopulationSize = int(crossoverRate * popSize)

        while generation < maxGenerations:

            newPopulation = Population(popSize, N)
            newPopulation.generationStates.clear()

            currentPopulation.generationStates.sort(key=lambda state: state.fitnessValue, reverse=True)
            sumFitness = 0
            for x in currentPopulation.generationStates:
                sumFitness += x.fitnessValue

            probList = []
            for x in currentPopulation.generationStates:
                probList.append(float(x.fitnessValue / sumFitness))

            crossoverred = 0

            while crossoverred < (crossoverPopulationSize // 2):

                if elitism == 'Y':
                    parent1 = currentPopulation.generationStates[0]
                    parent2 = currentPopulation.generationStates[1]
                else:
                    parent1 = AlgoFunctions.getParent(currentPopulation, probList)
                    parent2 = AlgoFunctions.getParent(currentPopulation, probList)

                if crossover_type == 'S':
                    child1 = AlgoFunctions.crossoverSP(parent1, parent2)[0]
                    child2 = AlgoFunctions.crossoverSP(parent1, parent2)[1]
                elif crossover_type == 'M':
                    child1 = AlgoFunctions.crossoverMP(parent1, parent2)[0]
                    child2 = AlgoFunctions.crossoverMP(parent1, parent2)[1]

                if random.random() > mutationProb:
                    child1 = AlgoFunctions.mutateChild(child1)
                if random.random() > mutationProb:
                    child2 = AlgoFunctions.mutateChild(child2)

                child1.fitnessValue = child1.nonAttackPairs()
                child2.fitnessValue = child2.nonAttackPairs()

                newPopulation.generationStates.append(child1)
                newPopulation.generationStates.append(child2)

                crossoverred += 1

            while len(newPopulation) != popSize:
                newPopulation.generationStates.append(currentPopulation.generationStates[random.randrange(N // 2)])

            newPopulation.generationStates.sort(key=lambda state: state.fitnessValue, reverse=True)
            bestCurrentState = newPopulation.generationStates[0]

            print(newPopulation)
            print(f'Best State so far: {bestCurrentState}')
            print()
            if bestCurrentState.fitnessValue == maxFitness:
                print(f'Found solution :  {bestCurrentState}')
                solutionFound = True
                break

            generation += 1

        if not solutionFound:
            print('Solution not found')

        stopTime = time.time()
        timeTaken = stopTime - startTime
        print(f'Total Steps = {generation}')
        print(f'Time taken = {timeTaken} s')


        return bestCurrentState.queenRows
