import numpy as np

LESS_THAN_OR_EQUAL = -1
EQUAL = 0
GREATER_THAN_OR_EQUAL = 1

class Restriction:
    
    def __init__(self, *var_coefficients: float, ineq_type : int = LESS_THAN_OR_EQUAL, tech_coef: float = 0.0):

        self.coefficients = np.array(var_coefficients)
        self.ineq_type = ineq_type
        self.tech_coef = tech_coef
    
    def reverse_direction(self):
        
        self.coefficients *= -1
        self.ineq_type *= -1
    
    def equalize(self) -> bool:

        if self.ineq_type == EQUAL:
            return False

        if self.ineq_type == GREATER_THAN_OR_EQUAL:
            self.reverse_direction()
         
        return True
    
    @property
    def var_count(self):
        return len(self.coefficients)

def get_increased_form(*restrictions : Restriction):
    
    indexes = []
    var_coeffs = np.empty((0, restrictions[0].var_count))
    b = []

    for idx, r in enumerate(restrictions):
        if r.equalize():
            indexes.append(idx)
        var_coeffs = np.vstack((var_coeffs, r.coefficients))
        b.append(r.tech_coef)

    slack_vars = np.zeros((len(restrictions), len(indexes)))

    for i, row in enumerate(indexes):
        slack_vars[row][i] = 1

    return np.hstack((var_coeffs, slack_vars)).tolist(), b