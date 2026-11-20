# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# """
#     THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
#     NEW TO PROGRAMMING.
#
#     Complete the folllowing function that takes a mathematical expression
#     as a string and evaluates it. This function allows for an arbitrary number
#     of keyword arguments using **kwargs, and provide default values for
#     variable x, and y if they are not provided.
# """
#
#
# def evaluate_expression(expression, x=0, y=0, **kwargs):
#     """
#     Evaluates a mathematical expression with arbitrary variables.
#     - expression: A string representing the mathematical expression.
#     - x, y: Default values for 'x' and 'y' if not provided.
#     - **kwargs: Arbitrary additional variables for the expression.
#
#     Example usage:
#         evaluate_expression('x + y + z', x=1, y=2, z=3) -> 6
#         evaluate_expression('a * b + c', a=5, b=3, c=10) -> 25
#
#     To get started with this task, you can have a look at Python built-in
#     function eval that will return the results of an evaluated expression.
#     """
# ============================================================================
# Completed solution
# ============================================================================
"""Evaluate basic arithmetic expressions with named variables, without eval."""
import ast
import operator

OPERATORS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod, ast.Pow: operator.pow,
}
UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate_expression(expression, x=0, y=0, **kwargs):
    """Evaluate numeric expressions containing x, y, and keyword variables."""
    variables = {"x": x, "y": y, **kwargs}

    def resolve(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.Name) and node.id in variables:
            result = variables[node.id]
            if type(result) not in (int, float):
                raise TypeError("Variables must be numeric")
            return result
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](resolve(node.left), resolve(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY:
            return UNARY[type(node.op)](resolve(node.operand))
        raise ValueError("Unsupported expression")

    return resolve(ast.parse(expression, mode="eval").body)


if __name__ == "__main__":
    assert evaluate_expression("x + y + z", x=1, y=2, z=3) == 6
    assert evaluate_expression("a * b + c", a=5, b=3, c=10) == 25
    print(evaluate_expression("x + y + z", x=1, y=2, z=3))
