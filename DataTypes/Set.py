"""
unordered
iterable,mutable
unique
"""

# Empty set
Set1 = set()
print(Set1)

set2 = {'Hello', 1, "Why"}
print(set2)
# Trying duplicate
set3 = {'Hello', 'Hello', 1, "Why"} # Ignore the duplicate
print(set3)
# adding element
set3.add(10)
print(set3)
# adding duplicate element
set3.add(10)
print(set3)
#remove element
set3.remove("Why")
print(set3)