import time
import matplotlib.pyplot as plt
from config import max_population, N
from fitness import calculate_conflicts, Average_Penalty
from operators import CutAndFill_X_over
from selection import generate_initial_population, parent_selection, insert_into_population

# This is for calculating the convergence speed of each generation
num_generations = []

for _ in range(50):  # Change to 1 for only 1 run
    finish = False
    counter = 0
    population = generate_initial_population(size=max_population, N=N)

    while not finish:
        '''
        CHOOSE WHICH SURVIVAL SELECTION AS PREFERRED and comment out the rest
        1- Normal Survival selection
        2- Generational replacement
        3- Elitism
        '''

        #**** Normal Survival selection
        # print (f"Average fitness : {100*(1/Average_Penalty(population))} %")
        selected_parents = parent_selection(population)
        children = CutAndFill_X_over(selected_parents[0], selected_parents[1])
        children = list(children)
        x = insert_into_population(children[0], children[1], population, max_population)
        population = x

        #**** Generational replacement
        '''
        new_population = []
        for _ in range(int(max_population / 2)) :
            selected_parents = parent_selection(population)
            children = CutAndFill_X_over(selected_parents[0], selected_parents[1])
            children = list(children)
            new_population.append(children[0])
            new_population.append(children[1])
        population = new_population
        '''

        #**** Elitism
        '''
        new_population = []
        for _ in range(int(max_population/2) - 1):
            selected_parents = parent_selection(population)
            children = CutAndFill_X_over(selected_parents[0], selected_parents[1])
            children = list(children)
            new_population.append(children[0])
            new_population.append(children[1])
        # The 2 best of the elder population    
        penalty_list = [(ind, calculate_conflicts(ind)) for ind in population]
        sorted_penalty_list = sorted(penalty_list, key=lambda item: item[1])[:2]
        f_1 = sorted_penalty_list[0][0]
        f_2 = sorted_penalty_list[1][0]
        new_population.append(f_1)
        new_population.append(f_2)
        population = new_population
        '''
        
        # Finish if we find the final answer
        for i in population:
            if calculate_conflicts(i) == 0:
                print(f"Found the Final Answer : {i} \n*************************************************")
                finish = True
        counter += 1

    num_generations.append(counter)

print(num_generations)
print(sum(num_generations) / len(num_generations))

# Plotting the final result
plt.plot(num_generations, color='r')
plt.xlabel('Runs out of 20')
plt.ylabel('Convergence speed in each run')
plt.title('Convergence speed vs Runs out of 50')
plt.show()