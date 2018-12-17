import random , select , argparse
from item import Item

##########################################################################################
# CONFIG

parser = argparse.ArgumentParser()
parser.add_argument("--capacity", help="Set the capacity. Default is 30.")
parser.add_argument("--size", help="Set the population size. Default is 50.")
parser.add_argument("-n", help="Set the number of points for the crossover. Default is 3.")
parser.add_argument("--generations", help="Set the number of generations. Default is 2000.")
parser.add_argument("--mutationprob", help="Set the mutation probability (Must be between 0 and 1). Default is 0.05")
parser.add_argument("--crossoverprob", help="Set the crossover probability (Must be between 0 and 1). Default is 0.1")
args = parser.parse_args()

# Read txt file and get items
ITEMS = []
with open("items.txt", "r") as items:
    for line in items.readlines():
        weight = line.split(" ")[0]
        value = line.split(" ")[1]
        ITEMS.append(Item(weight, value))

# Number of items
ITEMS_COUNT = len(ITEMS)

# Capacity of the knapsack entered by the user. Default is 30
CAPACITY = args.capacity if args.capacity else 30

# Number of points for the multi point crossover entered by the user. Default is 3
N_POINT = args.n if args.n else 3

# Number of individulas in the population filled with some permutation of 0s and 1s entered by the user. Default is 50 
POP_SIZE = args.size if args.size else 50

# Number of generations entered by the user. Default is 2000
GENERATIONS = args.generations if args.generations else 2000

# Crossover probability enterd by the user. Default is 0.1
CROSSOVER_PROBABILTY = args.crossoverprob if args.crossoverprob else 0.1

# Mutate probability entered by the user. Defaulst is 0.05
MUTATION_PROBABITLY = args.mutationprob if args.mutationprob else 0.05

# END OF CONFIG
##########################################################################################

def fitness(target):
    total_value = 0
    total_weight = 0
    index = 0
    # Sum of value and weight
    for i in target:        
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1
    # Cheking to fit
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

# Getting total value of current population
def get_total_value(pop):
    total_value = 0
    for target in pop:
        total_value+= fitness(target)
    return total_value         

# generating initial population
def generate_starting_population(amount):
    return [generate_individual() for x in range (0,amount)]
def generate_individual():
    return [random.randint(0,1) for x in range (0,ITEMS_COUNT)]

# mutating a point on a solution
def mutate(target):
    r = random.randint(0,len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1
# selecting parents by using roulette wheel selection
def roulette_wheel_selection(pop, parent_number):
    parents = []
    total_value = get_total_value(pop)
    current_value = 0
    # spining the wheel and select parent based on rate of value and total value
    for spin in range(0, parent_number):
        spin_value = random.randint(0,total_value)
        for target in pop:
            current_value+= fitness(target)
            if current_value >= spin_value:
                print "SPIN!!! ,%s, fit: %s" % (str(target), fitness(target)) 
                parents.append(target)
                pop.remove(target)
                break
    return parents

# n-point crossover by using two solution to generate their child
def crossover(father, mother):
    # deciding the lines to split the solution
    genes_points = [0]
    genes_points += sorted(random.sample(range(2, ITEMS_COUNT), N_POINT))
    genes_points += [ITEMS_COUNT]
    child = []
    # creating a new child by using father and mother data 
    for count in range(0, N_POINT+1):
        start = genes_points[count]
        end = genes_points[count+1]
        # chosing which part of father or mother
        if count % 2 == 0:
            child += father[start:end]
        else:
            child += mother[start:end]
    return child

# generating a new generation by mutation and crossover
def creating_new_generation(pop):
    # selection with roulette_wheel_selection
    parents = roulette_wheel_selection(pop, (len(pop)/5))
    parents_length = len(parents)
    # mutating selected parents
    for p in parents:
        if MUTATION_PROBABITLY > random.random():
            mutate(p)
    children = []
    desired_length = POP_SIZE - len(parents)
    # creating new children using with parents
    while len(children) < desired_length:
        # crossover cheking
        if CROSSOVER_PROBABILTY > random.random():
            # selecting two parents randomly
            father_and_mother = random.sample(range(0, parents_length-1),2)
            father = parents[father_and_mother[0]]
            mother = parents[father_and_mother[1]]
            # crossover selected two parents to create a new child
            child = crossover(father, mother)  
        else:
            # or cloning a parent randomly
            child =  parents[random.randint(0,parents_length-1)]
        # checking to mutate the new child
        if MUTATION_PROBABITLY > random.random():
            mutate(child)
        children.append(child)
    parents.extend(children)
    return parents


def main():
    generation = 1
    population = generate_starting_population(POP_SIZE)
    max_fit = 0
    for g in range(0,GENERATIONS):
        print "Generation %d with %d" % (generation,len(population))
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        for i in population:        
            print "%s, fit: %s" % (str(i), fitness(i)) 
            if fitness(i) > max_fit:
                max_fit = fitness(i)     
        population = creating_new_generation(population)
        generation += 1
    # for item in ITEMS:
    #     print(item)
    print "Maximum fitness: " + str(max_fit)

if __name__ == "__main__":
    main()
