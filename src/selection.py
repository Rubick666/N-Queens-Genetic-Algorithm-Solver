import random
from fitness import calculate_conflicts
from operators import tuple_to_list

# Function to generate the initial population
def generate_initial_population(size: int, N: int):
    population = []
    base_numbers = list(range(1, N + 1))
    for _ in range(size):
        individual = random.sample(base_numbers, len(base_numbers))
        population.append(individual)
    return population

# Parent selection function
def parent_selection(population: list):
    mating_pool = []

    # Selecting 5 random individuals as parents
    for _ in range(5):
        n = random.randint(0, len(population) - 1)
        mating_pool.append(population[n])

    # Creating a list of tuples (individual, penalty)
    penalty_list = [(ind, calculate_conflicts(ind)) for ind in mating_pool]

    # Sorting by penalty and selecting the two with the least conflicts
    sorted_penalty_list = sorted(penalty_list, key=lambda item: item[1])[:2]

    # Selecting each member of the best two
    f_1 = sorted_penalty_list[0][0]
    f_2 = sorted_penalty_list[1][0]

    # turning into list
    f_1 = tuple_to_list(f_1)
    f_2 = tuple_to_list(f_2)

    return f_1, f_2

# Survival selection
def insert_into_population(child_1: list, child_2: list, population: list, max_population: int):
    # Calculate penalties
    penalty_child_1 = calculate_conflicts(child_1)
    penalty_child_2 = calculate_conflicts(child_2)

    # Build list of (individual, penalty) pairs
    population_with_penalties = [(item, calculate_conflicts(item)) for item in population]

    # Sort by penalty
    population_with_penalties.sort(key=lambda x: x[1])

    # Keep top 50 individuals
    new_population = [index for index, _ in population_with_penalties]

    # Insert child_1 if it’s better than at least one individual in new_population
    for i, (index, penalty) in enumerate(population_with_penalties):
        if penalty > penalty_child_1:
            # Replace worst candidate first occurrence
            new_population[i % max_population] = child_1
            break

    # Insert child_2 if it’s better than at least one remaining individual
    for i, (index, penalty) in enumerate(population_with_penalties):
        if penalty > penalty_child_2:
            new_population[i % max_population] = child_2
            break

    return new_population