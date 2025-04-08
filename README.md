# ForkDoom Ultimate

**ForkDoom Ultimate** is a powerful Linux-based resource exhaustion tool that creates massive amounts of processes (fork bomb) and can optionally consume memory (RAM bomb).  
This tool is intended for **educational and ethical stress testing only**.

> ⚠️ **WARNING:** Running this on a production system or without permission may freeze or crash the machine. Use at your own risk in isolated environments only.

---

## Features

- Fork bomb with process count control
- Optional memory exhaustion (`RAM bomb`)
- Fast (instant attack) or Slow (progressive load) mode
- Optional delay between forks
- Password-protected execution
- Fully silent output (no console messages)
- Linux only

---

## Installation

```bash
git clone https://github.com/yourusername/forkdoom.git
cd forkdoom
python3 forkdoom.py --help
