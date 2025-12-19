#child module
import builtin
print(builtin(5))

from math import sqrt, factorial
print(sqrt(16))
print(factorial(16))

#builtin module ---> math, random
import random
print(random.randint(1,5))

#user defined module ---> calc.py, builtin.py

#3rd party module
#requests, pandas, numpy
import requests
requests.get("http://google.com")
r.status_code
