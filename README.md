<div align="center">

```
███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ███████╗███████╗
██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗ ╚████╔╝ ██╔██╗ ██║███████║██████╔╝███████╗█████╗  
╚════██║  ╚██╔╝  ██║╚██╗██║██╔══██║██╔═══╝ ╚════██║██╔══╝  
███████║   ██║   ██║ ╚████║██║  ██║██║     ███████║███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝
```

**Runtime execution graph visualizer for Python projects.**

Trace. Analyze. Understand.

[![PyPI version](https://img.shields.io/pypi/v/synapse-tracer?style=flat-square&color=ffffff&labelColor=111111)](https://pypi.org/project/synapse-tracer/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-white?style=flat-square&labelColor=111111)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-white?style=flat-square&labelColor=111111)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-white?style=flat-square&labelColor=111111)](CONTRIBUTING.md)

</div>

---

## What is SYNAPSE?

Most Python codebases are black boxes at runtime.  
You run the code. Something breaks. You guess where.

**SYNAPSE changes that.**

It traces your program during execution and renders an interactive graph showing exactly how functions call each other — where time is spent, where errors originate, and how data flows through your system.

> One command. Your entire runtime, mapped.

---

## Demo

https://github.com/user-attachments/assets/YOUR_VIDEO_LINK_HERE

*(Replace `YOUR_VIDEO_LINK_HERE` with your actual GitHub video asset URL — drag `synapse_demo.mkv` into a GitHub issue to get the link)*

---

## Install

```bash
pipx install synapse-tracer
```

<details>
<summary>pip alternative</summary>

```bash
pip install synapse-tracer
```

</details>

---

## Usage

```bash
synapse path/to/your_project
```

That's it. SYNAPSE will:

1. **Trace** — instruments your program and records every function call at runtime
2. **Analyze** — maps relationships, frequencies, and error paths
3. **Render** — opens an interactive execution graph in your browser

---

## The Graph

Each node is a function. Each edge is a call.

| Color | Meaning |
|-------|---------|
| ⬜ White | Standard function |
| 🟨 Yellow | Hotspot — called frequently |
| 🟥 Red | Runtime error origin |

Click any node to preview the source code.  
Replay execution to watch your program run, step by step.

---

## Scale Modes

SYNAPSE adapts to your project size automatically based on available system memory.

| Mode | Max Nodes | Best For |
|------|-----------|----------|
| `CPU SAFE` | ~1,200 | Scripts, small modules |
| `BALANCED` | ~3,000 | Mid-size applications |
| `LARGE GRAPH` | ~8,000 | Frameworks, large services |
| `FULL GRAPH` | ~50,000 | Monorepos, deep systems |

---

## Features

- **Runtime call tracing** — captures the real execution path, not a static estimate
- **Interactive graph** — zoom, pan, click, explore
- **Hotspot detection** — instantly see your most-called functions
- **Error highlighting** — trace exceptions back to their source
- **Code preview** — inspect function source without leaving the graph
- **Execution replay** — visualize the runtime flow in sequence
- **Auto-scaling** — intelligently adjusts render mode to your hardware

---

## Example Workflow

```bash
# Install once
pipx install synapse-tracer

# Run on any project
synapse my_project
```

The graph opens in your browser. From there:

- **Zoom** into hot execution paths
- **Click** any function to read its source
- **Replay** the runtime to follow call sequences
- **Spot** yellow nodes — those are your performance candidates
- **Follow** red nodes back to error roots

---

## Why Not a Profiler?

Profilers give you numbers. SYNAPSE gives you a map.

| | Profiler | SYNAPSE |
|--|---------|---------|
| Call timing | ✅ | — |
| Call relationships | Partial | ✅ |
| Visual execution graph | ❌ | ✅ |
| Error path tracing | ❌ | ✅ |
| Code preview per node | ❌ | ✅ |
| Execution replay | ❌ | ✅ |
| Works on any project | ✅ | ✅ |

Use both. They answer different questions.

---

## Roadmap

- [ ] Static + runtime hybrid analysis
- [ ] Streaming graph rendering for very large projects
- [ ] VSCode extension
- [ ] CI/CD integration — generate execution graphs on every run
- [ ] Diff mode — compare graphs across commits
- [ ] Export to SVG / PNG

---

## Contributing

Pull requests are welcome.

If you find a bug or have a feature idea — [open an issue](../../issues).  
If you want to contribute code — [read the contributing guide](CONTRIBUTING.md).

This project is in active development. Good time to get involved.

---

## License

[MIT](LICENSE) — use it, fork it, build on it.

---

<div align="center">

Built for developers who want to **see** their code, not just run it.

---

*Submitted as a final project for Semester 2 — PPS (Python Programming Subject)*

</div>
