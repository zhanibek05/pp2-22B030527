import itertools

def print_permutations(s):
    permutations = list(itertools.permutations(s))
    for s in permutations:
        print("".join(s))

s = input()
print_permutations(s)
    