In the program, implemented a Genetic Algorithm which solves the 0-1 Knapsack problem

The program has the following criterias:

Weights and values of the items and capacity of the knapsack has to be given to
the program using a text file

The following variables have been given to program as a command line parameter.
		
		Size of population
		
		Number of generation
		
		Crossover probability
		
		Mutation probability

The program has implemented the following methods

		Parent selection: Roulette-wheel selection
		
		Crossover: n-point crossover (Parameter n should be given by user)
		
		Survival selection: Any selection method with elitism.

Parameters

		--capacity : Set the capacity. Default is 30
		--size : Set the population size. Default is 50
		-n : Set the number of points for the crossover. Default is 3
		--elitism : Set the selection type. Default is true
		--gnum : Set the number of generations. Default is 2000
		--mutationprob : Set the mutation probability (Must be between 0 and 1). Default is 0.05
		--crossoverprob : Set the crossover probability (Must be between 0 and 1). Default is 0.1
