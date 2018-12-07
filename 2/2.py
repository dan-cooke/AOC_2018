with open("./input") as file:
    sequence = file.read().split()
    twos =0
    threes = 0
    for idx, set in enumerate(([uniqueList for uniqueList in [(set(x)) for x in sequence]])):
        twos_found = False
        threes_found = False
        for i in [x for x in list(set)]:
            if sequence[idx].count(i) == 2 and not twos_found:
                twos_found = True
                twos +=1
            elif sequence[idx].count(i) == 3 and not threes_found:
                threes_found = True
                threes +=1

    print(twos * threes)
