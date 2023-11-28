class TreeWalkInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        if isinstance(ast, list):  # It's an S-expression
            operator = ast[0]
            if operator == '+':
                return self.interpret(ast[1]) + self.interpret(ast[2])
            elif operator == '-':
                return self.interpret(ast[1]) - self.interpret(ast[2])
            elif operator == '*':
                return self.interpret(ast[1]) * self.interpret(ast[2])
            elif operator == '/':
                return self.interpret(ast[1]) / self.interpret(ast[2])
            else:
                raise ValueError(f"Unknown operator: {operator}")
        elif isinstance(ast, int):  # It's a literal number
            return ast
        else:
            raise ValueError(f"Unexpected AST node: {ast}")

# Example usage:
ast = ['+', 3, ['*', 4, 5]]  # Represents (+ 3 (* 4 5))
interpreter = TreeWalkInterpreter()
result = interpreter.interpret(ast)
print(result)
