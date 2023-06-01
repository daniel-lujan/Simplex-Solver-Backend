import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np
from io import BytesIO

def get_solution_graph(
        A: List[List[int]],
        b: List,
        solution: Tuple[int, int]) -> BytesIO:
    
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)

    x = np.linspace(0, round(solution[0]*1.1), 200)
    
    for i, r in enumerate(A):
        y = -(r[0]/r[1])*x + b[i]/r[1]
        axes.plot(x, y, label= f"{r[0]}*x1 + ({r[1]}*x2) - {b[i]}")
        axes.fill_between(x, 0, y,
                          where=(y >= 0) & (x >= 0),
                          alpha=0.15)
        
    axes.set_xlim((0, None))
    axes.set_ylim((0, None))
    axes.legend()
    axes.set_xlabel("$x_{1}$")
    axes.set_ylabel("$x_{2}$")
    
    axes.plot(solution[0], solution[1], "ro")

    image = BytesIO()

    plt.savefig(image, format="png")
    image.seek(0)

    return image