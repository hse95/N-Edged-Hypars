import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Equations are in the form of Dmax = f(A, Rn, t) 
# The equations are found in a more simplified form in the mansucript. 

### Genetic Programming Equations ###
## All results are in m ##
# N = 3
def N3GP(A, Rn, t):
    result = (7.28e-2 * A * (math.sqrt(A) - 7.9e-1 * Rn)) / (Rn * (Rn * math.sqrt(A) + 2.47e2 * t))
    result = result / 1000
    return result


## N = 3 _ Retrained on data with Deflection <= 150 mm 
def N3GP_Retrained(A, Rn, t):
    result = (0.0725 * A * (math.sqrt(A) - 0.827 * Rn)) / (Rn * (Rn * math.sqrt(A) + 246.0 * t))
    result = result / 1000
    return result


# N = 4
def N4GP(A, Rn, t):
    numerator = -(2.89e-5 * A * Rn - 4.5e-5 * A) * math.sqrt(A) + 2.42e-3 * A * t
    denominator = Rn * t
    result = numerator / denominator - 1.55e-3 * A
    result = result / 1000
    return result

# N = 5
def N5GP(A, Rn, t):
    first_term = 1.04e-5 * A * math.sqrt(A) / (Rn * t)
    second_term = 2.21e-4 * A
    third_term = 5.15e-4 * A / (Rn)
    fourth_term = 2.25e-4 * A / (Rn**2)
    result = first_term + second_term + third_term + fourth_term
    result = result / 1000
    return result

# N = 6
def N6GP(A, Rn, t):
    A_sqrt = A**0.5
    t = t*100
    term1 = (2.1753 * Rn - 0.057896 * A_sqrt) / (0.70373 * Rn)
    term2 = (0.15436 * A_sqrt) / (-0.42624 * Rn)
    term3 = (A_sqrt * A_sqrt * 1.0732) / (-1.7969 * t)
    term4 = (1.9207 * A_sqrt) / (0.96046 * Rn)
    term5 = A_sqrt * Rn * 11.619
    result = ((term1 + term2 + term3) * (term4 + term5) * -0.00030409) + 0.028686
    result = result / 1000
    return result

# N = 7
def N7GP(A, Rn, t):
    A05 = A**0.5
    result = ((A05 * (3.7279e0 * Rn + 2.0444e-1 * A05) * (1.239e0 * A05 / (1.359e2 * t) + (-2.2913e0 * Rn + 1.0429e0) / (1.9412e0 * Rn) + A05 * Rn * 2.9985e-1) * 3.0514e-3) / (1.4329e0 * Rn) - 1.6865e-2)
    result = result / 1000
    return result

# N = 8
def N8GP(A, Rn, t):
    A_05 = A**0.5
    result = ((2.3899e0 * A_05 + (A_05 * A_05 * 3.0228e-1) / (4.2724e1 * t)) * (4.5097e0 * A_05 + (8.9089e-1 * A_05) / (2.9483e0 * Rn)) * 8.454e-5) / (8.2106e-1 * Rn) - 7.3108e-3
    result = result / 1000
    return result

#############################################################################################

### Gene Expression Programming Equations ###
# All results are in m
#N = 3
def N3GEP(A, Rn, t):
    t = t * 100
    A05 = A**0.5
    numerator = (t / A05) + A05 - 5.78
    denominator = (Rn * t) / (A05 - 5.78)
    result = numerator / denominator
    result = result / 1000
    return result

#N = 4
def N4GEP(A, Rn, t):
    A = math.sqrt(A)
    t = t * 100
    numerator = A / Rn * (A - 4.3)
    denominator = 8.3 * (t + 1) + Rn
    result = numerator / denominator
    result = result / 1000
    return result

# N = 5
def N5GEP(A, Rn, t):
    result = (math.sqrt(A) ** 2) / (19.75 * (t * 100 + 4.4) * Rn)
    result = result / 1000
    return result

# N = 6
def N6GEP(A, Rn, t):
    A05 = math.sqrt(A)
    t = t * 100
    numerator = A05 ** 2
    denominator = 31.78 * Rn * (t + 3.90)
    result = numerator / denominator
    result = result / 1000
    return result

# N = 7
def N7GEP(A, Rn, t):
    A = math.sqrt(A)
    t = t * 100
    result = (A / t + 0.12 * t) / (73 * Rn / A)
    result = result / 1000
    return result

# N = 8
def N8GEP(A, Rn, t):
    A05 = math.sqrt(A)
    t = t * 100
    numerator = 0.11 * A05 / (t + 9.17)
    denominator = 2.39 * Rn / (A05 - Rn)
    result = numerator / denominator
    result = result / 1000
    return result

