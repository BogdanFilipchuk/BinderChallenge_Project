"""
Numbers in Python
a = 7; b = 2.5
a + b, a - b, a * b, a / b   # add, subtract, multiply, divide (always gives a float)
a // 2      # integer division → 3
a % 2       # remainder (modulo) → 1
a ** 2      # power → 49
abs(-3)     # absolute value
round(3.14159, 2)   # → 3.14
int(3.9)    # → 3 (cuts off the decimals)
float(3)    # → 3.0
max(1, 5, 3), min(1, 5, 3)
import math
math.sqrt(16), math.log10(1e-7), math.log(x), math.exp(x), math.pi

strings in Python

s = "Hello World"
len(s)              # length
s[0], s[-1]         # first and last character
s[0:5]              # slice → "Hello"
s.upper(), s.lower()
s.strip()           # remove spaces at the start and end
s.split(" ")        # → ["Hello", "World"]
" ".join(["a","b"]) # → "a b"
s.replace("World", "Python")
s.find("o")         # index of the first match (-1 if there is none)
s.count("l")
s.startswith("He"), s.endswith("ld")
"World" in s        # → True
str(42)             # number → string
f"pH = {7.123:.2f}" # f-string formatting → "pH = 7.12"

booleans in Python

True, False
and, or, not
==, !=, <, >, <=, >=
bool(0)   # → False (0, "", [] and None all count as False)

lists in Python

L = [3, 1, 2]
len(L)
L[0], L[-1], L[1:3]   # indexing and slicing
L.append(4)           # add to the end
L.insert(0, 9)        # insert at an index
L.extend([5, 6])      # add several items
L.remove(9)           # remove by value
L.pop()               # remove and return the last item
L.pop(0)              # remove and return the item at an index
L.index(2)            # position of a value
L.count(2)
L.sort()              # sorts in place
sorted(L)             # returns a new sorted list
L.reverse()
sum(L), max(L), min(L)
2 in L
L + [7, 8]            # joins two lists
[0] * 5               # → [0, 0, 0, 0, 0]
[x**2 for x in L]     # list comprehension
[x for x in L if x > 1]

Tuples in Python
t = (1, 2, 3)
t[0], len(t), t.count(1), t.index(2)
a, b, c = t          # unpacking

Dictionaries in Python

d = {"HCl": 36.46, "NaOH": 40.00}
d["HCl"]              # get a value
d.get("KOH", 0)       # get with a default if the key is missing
d["KOH"] = 56.11      # add or change
del d["HCl"]
d.keys(), d.values(), d.items()
"NaOH" in d
for key, val in d.items(): print(key, val)

sets in Python

s = {1, 2, 3}
s.add(4); s.remove(1)
s | {5}, s & {2, 3}, s - {2}   # union, intersection, difference

type conversion in Python
type(x)
isinstance(x, int)
int("5"), float("2.3"), str(5), list("abc"), tuple([1,2]), set([1,1,2])

numpy arrays in Python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
np.zeros(5), np.ones((2, 3))
np.arange(0, 10, 2)        # → [0 2 4 6 8]
np.linspace(0, 1, 5)       # 5 evenly spaced points from 0 to 1
np.random.rand(3)

# Information about an array
a.shape, a.size, a.ndim, a.dtype

# Indexing
a[0], a[-1], a[1:3]
M = np.array([[1,2],[3,4]])
M[0, 1], M[:, 0]           # one element, first column
a[a > 1]                   # boolean mask (filtering)

# Math, applied element by element
a + 1, a * 2, a ** 2, a + a
np.sqrt(a), np.log10(a), np.exp(a), np.abs(a)

# Statistics
a.sum(), a.mean(), a.std(), a.min(), a.max()
a.argmin(), a.argmax()     # index of the min/max

# Reshaping and combining
a.reshape(3, 1)
M.T                        # transpose
np.concatenate([a, a])
np.append(a, 4)
np.sort(a)

# Linear algebra
M @ M                      # matrix multiplication
np.linalg.inv(M), np.linalg.det(M)

# Useful for lab data
np.diff(a)                 # differences between neighbours (handy for titration curves)
np.gradient(y, x)          # derivative dy/dx
np.polyfit(x, y, 1)        # linear fit → [slope, intercept]
np.loadtxt("data.txt")     # load data from a text file

built-in functions in Python

print(), input(), len(), range(0, 10, 2), type()
enumerate(L)    # for i, x in enumerate(L): gives index and value
zip(L1, L2)     # loop over two lists together
help(obj)       # shows the documentation for anything
dir(obj)        # lists all methods of an object

"""