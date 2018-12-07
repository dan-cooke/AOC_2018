with open("./input") as input:
        
    freaki_boys = [int(n.strip()) for n in input.read().split()]
    print(sum(freaki_boys))

    from itertools import accumulate, cycle
    seen = set()
    print(next(f for f in accumulate(cycle(freaki_boys)) if f in seen or seen.add(f)))
