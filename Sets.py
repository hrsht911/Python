s1 = {1,2,3}
s2 = {2,3,4}
print(s1 | s2) #union
print(s1 & s2) #intersection
print(s1 - s2) #difference
print(s1 ^ s2) #symmetric difference
print("union of s1 and s2:", s1.union(s2))
print("intersection of s1 and s2:", s1.intersection(s2))
print("difference of s1 and s2:", s1.difference(s2))
print("difference of s2 and s1:", s2.difference(s1))
print("symmetric difference of s1 and s2:", s1.symmetric_difference(s2))