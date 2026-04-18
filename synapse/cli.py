import argparse
import psutil
from synapse.tracer import run_project
from synapse.visualizer import render_graph


def detect_memory():
    mem = psutil.virtual_memory().total / (1024 ** 3)
    return round(mem, 2)


def choose_mode():

    print("\nSYNAPSE RENDER MODES\n")

    print("1) CPU SAFE (≈1200 nodes)")
    print("2) BALANCED (≈3000 nodes)")
    print("3) LARGE GRAPH (≈8000 nodes)")
    print("4) FULL GRAPH (dangerous)\n")

    choice = input("Select mode [1‑4]: ").strip()

    modes = {
        "1": "cpu",
        "2": "balanced",
        "3": "large",
        "4": "full"
    }

    return modes.get(choice, "cpu")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()

    ram = detect_memory()

    print("\nDetected RAM:", ram, "GB")

    if ram <= 4:
        print(
            "\n⚠ WARNING: Low RAM system detected.\n"
            "Recommended mode: CPU SAFE\n"
        )

    mode = choose_mode()

    print("\nRunning SYNAPSE in", mode.upper(), "mode\n")

    events, functions, edges = run_project(args.target)

    render_graph(events, functions, edges, mode)


if __name__ == "__main__":
    main()
