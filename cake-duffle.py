# https://www.interviewcake.com/question/python/cake-thief

def max_duffel_bag_value(tups, cap):
    tuple_with_value_by_weight = []
    for tup in tups:
        if tup[0] == 0:
            print("No space cakes allowed.")
        else:
            per_kilo = tup[1]/tup[0]
            tuple_with_value_by_weight.append((per_kilo, tup[0], tup[1]))

    # Creates list of tuples with per-kilo value, cake weight, cake value
    sorted_tuples_by_value = sorted(tuple_with_value_by_weight, key=lambda value: value[0], reverse=True)
    sorted_tuples_by_weight = sorted(tups, key=lambda weight: weight[0])
    lowest_weight = sorted_tuples_by_weight[0][0]
    remaining_cap = cap
    duffel_value = 0

    while remaining_cap >= lowest_weight: # Need lowest weight here as bottom boundary of while loop
        for pair in sorted_tuples_by_value:
            if pair[1] <= remaining_cap: # If the weight of the most expensive one is less than the remaining capacity
                remaining_cap -= pair[1]
                duffel_value += pair[2]

    print("Max duffel value: ", duffel_value)

# Tuples: (weight, value)
cake_tuples = [(7, 160), (2, 15), (3, 90)]
# Capacity: max weight the bag can hold
capacity = 20

cake_tuples_2 = [(0, 0), (3, 20), (2, 17)]
capacity_2 = 100
max_duffel_bag_value(cake_tuples, capacity)
max_duffel_bag_value(cake_tuples_2, capacity_2)
