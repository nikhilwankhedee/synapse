import os
import sys
import runpy
import traceback

events = []


def trace_calls(frame, event, arg):

    if event != "call":
        return trace_calls

    code = frame.f_code
    func_name = code.co_name
    file_name = code.co_filename

    caller = None

    if frame.f_back:
        caller = f"{frame.f_back.f_code.co_filename}:{frame.f_back.f_code.co_name}"

    events.append({
        "type": "call",
        "function": f"{file_name}:{func_name}",
        "caller": caller
    })

    return trace_calls


def run_with_trace(script_path):

    global events
    events = []

    sys.settrace(trace_calls)

    try:
        runpy.run_path(script_path, run_name="__main__")

    except Exception as e:

        tb = traceback.extract_tb(e.__traceback__)

        if tb:
            last = tb[-1]

            events.append({
                "type": "error",
                "function": f"{last.filename}:{last.name}",
                "line": last.lineno
            })

        print("Execution error:", e)

    finally:
        sys.settrace(None)

    return events


def find_python_files(directory):

    py_files = []

    for root, _, files in os.walk(directory):

        for f in files:
            if f.endswith(".py"):
                py_files.append(os.path.join(root, f))

    return py_files


def run_project(project_dir):

    from synapse.parser import extract_functions

    print("Scanning project directory...")

    functions, static_edges = extract_functions(project_dir)

    print("Found", len(functions), "functions")

    py_files = find_python_files(project_dir)

    entrypoints = []

    for f in py_files:

        try:
            with open(f, "r", errors="ignore") as file:
                code = file.read()

                if "__main__" in code:
                    entrypoints.append(f)

        except:
            pass

    if not entrypoints:
        entrypoints = py_files[:3]

    print("Detected entrypoints:")

    for e in entrypoints[:5]:
        print(" -", e)

    runtime_events = []

    for entry in entrypoints[:3]:

        print("Executing:", entry)

        try:
            runtime_events += run_with_trace(entry)
        except Exception as e:
            print("Execution failed:", e)

    return runtime_events, functions, static_edges
