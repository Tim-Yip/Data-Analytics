# Description: This script tests various numeric conversion techniques.
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

# cast as int
# int(a) cannot convert string to int
int(b)
# int(c) cannot convert string to int
# int(d) cannot convert string to int

# cast as float
float(a)
float(b)
# float(c) cannot convert string to float
# float(d) cannot convert string to float

# cast into a float then integer
int(float(a))

# Use slicing to add just the numeric portion of the string to a new variable
# and cast the number as an integer or string, whichever is appropriate
a_slice = float(a[1:6])
b_slice = int(b[0:2])
c_slice = int(c[0:3])
d_slice = int(d[7:8])

print(a_slice)
print(b_slice)
print(c_slice)
print(d_slice)

# Use .strip() to remove trailing spaces
print(a.strip())
print(d.strip())