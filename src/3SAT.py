import random

def readInput():
    pass

def generateInput(n, k):
    r = random.randint(0, int(2*n/k))

    booleanFormula = generateBooleanFormula(n, k, r)
    return booleanFormula

def generateBooleanFormula(n, k, r):
    booleanFormula = []
    for i in range(r):
        clause = random.sample(range(1,n+1), k)
        clause = [x*random.choice((-1,1)) for x in clause]
        booleanFormula.append(clause)
    return booleanFormula

def isSatisfiable(satSolver, booleanFormula, n, r, k):
    pass

def main():
    num_instances = 100
    n = 10
    k = 3
    for i in range(num_instances):
        print(generateInput(n,k))

if __name__ == "__main__":
    main()