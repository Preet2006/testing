import ast

class SafeCalculator(ast.NodeVisitor):
    """
    A secure AST visitor for evaluating basic arithmetic expressions.
    Supports integers and floats with +, -, *, / operators.
    Raises ValueError for unsupported nodes, operators, or division by zero.
    """
    def __init__(self):
        self.stack = []  # Stack to store intermediate results

    def visit_Module(self, node):
        # For mode='eval', the module body contains a single Expression node
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Expression):
            raise ValueError("Invalid expression structure: Expected a single expression.")
        self.visit(node.body[0])  # Visit the Expression node

    def visit_Expression(self, node):
        # The body of an Expression node is the actual expression
        self.visit(node.body)

    def visit_Constant(self, node):
        # Handles numeric literals (int, float) in Python 3.8+
        if isinstance(node.value, (int, float)):
            self.stack.append(node.value)
        else:
            raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")

    def visit_Num(self, node):
        # Handles numeric literals (int, float) in Python < 3.8
        self.stack.append(node.n)

    def visit_BinOp(self, node):
        # Visit left and right operands, then perform the operation
        self.visit(node.left)
        left = self.stack.pop()

        self.visit(node.right)
        right = self.stack.pop()

        if isinstance(node.op, ast.Add):
            self.stack.append(left + right)
        elif isinstance(node.op, ast.Sub):
            self.stack.append(left - right)
        elif isinstance(node.op, ast.Mult):
            self.stack.append(left * right)
        elif isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("Division by zero.")
            self.stack.append(left / right)
        else:
            raise ValueError(f"Unsupported binary operator: {type(node.op).__name__}")

    def visit_UnaryOp(self, node):
        # Handles unary operators like negation (-)
        self.visit(node.operand)
        operand = self.stack.pop()

        if isinstance(node.op, ast.USub):
            self.stack.append(-operand)
        else:
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")

    def generic_visit(self, node):
        # Catch any other node types that are not explicitly handled
        raise ValueError(f"Unsupported AST node type: {type(node).__name__}")

    @property
    def result(self):
        """Returns the final result from the stack."""
        if len(self.stack) != 1:
            raise ValueError("Evaluation error: stack not in expected state.")
        return self.stack[0]

def calculate_expression(expr: str) -> float:
    """
    Safely evaluates a mathematical expression string using the AST module.
    Supports basic arithmetic operations (+, -, *, /) on integers and floats.
    Raises ValueError for invalid expressions, unsupported operations, or division by zero.
    """
    if not isinstance(expr, str) or not expr.strip():
        raise ValueError("Invalid expression: Input must be a non-empty string.")

    try:
        # Parse the expression into an Abstract Syntax Tree (AST)
        # mode='eval' expects a single expression
        tree = ast.parse(expr, mode='eval')

        # Use the SafeCalculator to traverse and evaluate the AST
        calculator = SafeCalculator()
        calculator.visit(tree)

        return float(calculator.result)
    except SyntaxError as e:
        raise ValueError(f"Invalid expression: Syntax error - {str(e)}")
    except ValueError as e:
        # Re-raise ValueErrors from SafeCalculator directly
        raise ValueError(f"Invalid expression: {str(e)}")
    except Exception as e:
        # Catch any other unexpected exceptions during parsing or visiting
        raise ValueError(f"Invalid expression: An unexpected error occurred - {type(e).__name__}: {str(e)}")
