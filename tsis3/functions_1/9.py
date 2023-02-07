import math
def sphere_volume(R):
    return (4/3)*(math.pi)*(R**3)

r = int(input())
print(sphere_volume(r))