def calculate_conflicts(individual):
    conflicts = 0
    n = len(individual)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Same row conflict (never happens !)
            if individual[i] == individual[j]:
                conflicts += 1
            
            # Same diagonal conflict
            elif abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
                
    return conflicts

# calculate the average penalty over a population
def Average_Penalty(population: list, max_population: int):
    AP = 0
    for item in population:
        AP += calculate_conflicts(item)
    return AP / max_population