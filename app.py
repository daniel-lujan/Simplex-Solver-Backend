from flask import Flask, request, send_file, abort
from flask_cors import CORS

from simplex import simplex
from simplex.converter import matrix_to_restrictions, complete_objective_function
from simplex.restrictions import get_increased_form
from simplex.graph import get_solution_graph

import numpy as np

app = Flask(__name__)

CORS(app)

@app.route("/solve", methods=["POST"])
def solve():
    
    as_image = request.args.get("image", False) == "true"

    try:
        rest = request.json["restrictions"]
        obj = request.json["objective"]
    except KeyError:
        abort(400)

    n = len(obj)

    if as_image and n != 2:
        abort(400)

    try:
        rest = matrix_to_restrictions(rest)
        A, b = get_increased_form(*rest)

        c = complete_objective_function(obj, len(A[0])-n)

        solution = simplex(c, A, b)
    except:
        abort(400)

    if as_image:
        return send_file(get_solution_graph(A, b, solution), mimetype="image/png")
    else:
        crop = n-len(A[0])
        return [*solution[:crop], float(np.array(solution[:crop]).dot(np.array(obj[:crop])))]

if __name__ == "__main__":
    app.run(debug=True, port=5000)