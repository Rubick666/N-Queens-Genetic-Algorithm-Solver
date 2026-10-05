import random

# To transform from tuple to list
def tuple_to_list(tup: tuple):
    list = []
    for i in tup:
        list.append(i)
    return list

# Mutation
def mutation(individual: list, rate=10):  # rate expects values like 10, 50, 60 etc...
    # Implementing the rate aspect into my function
    rate = rate / 10
    i = random.randint(0, 10)
    if i <= rate:
        r1 = random.randint(0, 7)
        r2 = random.randint(0, 7)
        individual[r1], individual[r2] = individual[r2], individual[r1]
    return individual

# Recombination with CUT AND FILL method
def CutAndFill_X_over(i_1: list, i_2: list, rate=100):
    # Implementing the rate aspect into my function
    rate = rate / 10
    i = random.randint(0, 10)
    if i <= rate:

        # Random break point
        bp = random.randint(1, 7)
        
        # breaking each member in 2 sections
        i_1_part_1 = list(i_1)[:bp]
        i_1_part_2 = list(i_1)[bp:]
        i_2_part_1 = list(i_2)[:bp]
        i_2_part_2 = list(i_2)[bp:]
        
        # Adding the first part of a chromosome to the end of it's second part 
        new_i_1 = i_1_part_2 + i_1_part_1
        new_i_2 = i_2_part_2 + i_2_part_1

        # Doing the X-OVER 
        for element in new_i_1:
            if element in i_2_part_1:
                continue
            else:
                i_2_part_1 += [element]
        
        for element in new_i_2:
            if element in i_1_part_1:
                continue
            else:
                i_1_part_1 += [element]
        
        return mutation(i_1_part_1), mutation(i_2_part_1)
    else:
        return mutation(i_1), mutation(i_2)

# Recombination with PMX method
def PMX_X_over(i_1: list, i_2: list, rate=100):
    rate = rate / 10
    i = random.randint(0, 10)
    if i <= rate:
        size = len(i_1)
        pt1 = random.randint(0, size - 2)
        pt2 = random.randint(pt1 + 1, size - 1)

        # Initialize offspring with None
        o1 = [None] * size
        o2 = [None] * size

        # Copy crossover segment
        o1[pt1:pt2+1] = i_2[pt1:pt2+1]
        o2[pt1:pt2+1] = i_1[pt1:pt2+1]

        def fill_remaining(offspring, parent, start, end):
            for idx in range(size):
                if idx >= start and idx <= end:
                    continue
                gene = parent[idx]
                while gene in offspring[start:end+1]:
                    mapped_gene = parent[start + list(offspring[start:end+1]).index(gene)]
                    gene = mapped_gene
                offspring[idx] = gene
            return offspring

        o1 = fill_remaining(o1, i_1, pt1, pt2)
        o2 = fill_remaining(o2, i_2, pt1, pt2)

        return mutation(o1), mutation(o2)
    else:
        return mutation(i_1), mutation(i_2)
    
# Recombination with 2-cut method
def TwoCut_X_over(i_1: list, i_2: list, rate=100):
    rate = rate / 10
    i = random.randint(0, 10)
    if i <= rate:
        # Generate two distinct cut points
        cut1 = random.randint(0, 6)
        cut2 = random.randint(cut1 + 1, 7)

        # Copy middle segments
        mid1 = i_1[cut1:cut2]
        mid2 = i_2[cut1:cut2]

        # Fill remaining positions from the other parent, skipping duplicates
        def fill_rest(parent, mid):
            rest = [x for x in parent if x not in mid]
            return rest[:cut1] + mid + rest[cut1:]

        child1 = fill_rest(i_2, mid1)
        child2 = fill_rest(i_1, mid2)

        return mutation(child1), mutation(child2)
    else:
        return mutation(i_1), mutation(i_2)

# Recombination with 3-cut method
def ThreeCut_X_over(i_1: list, i_2: list, rate=100):
    rate = rate / 10
    i = random.randint(0, 10)
    if i <= rate:
        n = len(i_1)  # length of chromosome

        # three valid break points
        cuts = sorted(random.sample(range(1, n - 1), 2))
        cut1, cut2 = cuts[0], cuts[1]
        cut3 = random.randint(cut2 + 1, n - 1)

        # dividing parents to 4 sections
        seg1 = [i_1[:cut1], i_1[cut1:cut2], i_1[cut2:cut3], i_1[cut3:]]
        seg2 = [i_2[:cut1], i_2[cut1:cut2], i_2[cut2:cut3], i_2[cut3:]]

        mid1 = seg2[1] + seg1[2]
        mid2 = seg1[1] + seg2[2]

        def fill_valid(prefix, mid, suffix, valid_set):
            combined = prefix + mid + suffix
            seen = set()
            corrected = []
            for val in combined:
                if val in valid_set and val not in seen:
                    corrected.append(val)
                    seen.add(val)

            missing = [x for x in valid_set if x not in seen]
            return corrected + missing

        valid_values = set(i_1)  

        child1 = fill_valid(seg1[0], mid1, seg1[3], valid_values)
        child2 = fill_valid(seg2[0], mid2, seg2[3], valid_values)

        return mutation(child1), mutation(child2)
    else:
        return mutation(i_1), mutation(i_2)