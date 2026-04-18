import ast
import os


def extract_functions(directory):

    functions = {}
    edges = []

    for root, _, files in os.walk(directory):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            try:

                with open(path, "r", encoding="utf-8", errors="ignore") as f:

                    tree = ast.parse(f.read())

                for node in ast.walk(tree):

                    if isinstance(node, ast.FunctionDef):

                        func_id = f"{path}:{node.name}"

                        functions[func_id] = {
                            "file": path,
                            "line": node.lineno
                        }

                        for child in ast.walk(node):

                            if isinstance(child, ast.Call):

                                if isinstance(child.func, ast.Name):

                                    edges.append(
                                        (func_id, child.func.id)
                                    )

            except Exception:
                continue

    return functions, edges
