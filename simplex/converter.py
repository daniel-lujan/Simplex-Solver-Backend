from simplex.restrictions import Restriction
from typing import List

def matrix_to_restrictions(
        matrix: List[List[float]]) -> List[Restriction]:
    
    restrictions = []

    for row in matrix:
        r = Restriction(*row[:-2], ineq_type=row[-2], tech_coef=row[-1])
        restrictions.append(r)

    return restrictions

def complete_objective_function(
        objective_function: List[float],
        increased_vars: int):

    objective_function += [0] * increased_vars

    return objective_function