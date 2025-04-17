# ICS32Assignment1

# Diary Notebook (ICS 32 — Assignment 1)

A command‑line diary notebook program that stores entries in JSON files.  
You can create, open, edit, print, and delete notebooks through simple shell‑style commands.

---

## Table of Contents

- [Features](#features)  
- [Getting Started](#getting-started)  
- [Project Structure](#project-structure)  
- [Usage](#usage)  
  - [Commands](#commands)  
  - [Examples](#examples)  
- [Error Handling](#error-handling)  
- [Validity Checker](#validity-checker)  
- [Submission](#submission)  

---

## Features

- **C**: Create a new notebook  
- **D**: Delete an existing notebook  
- **O**: Open (load) a notebook with authentication  
- **E**: Edit loaded notebook (change user info, add/delete entries)  
- **P**: Print loaded notebook data  
- **Q**: Quit the program  

Supports shell‑style quoting and whitespace via the `shlex` module, cross‑platform paths via `pathlib`, and JSON serialization.

---

## Getting Started

1. **Clone or download** this repository.  
2. **Install** any required libraries (none beyond the Python standard library).  
3. Place the provided **validity checker** (`validity_checker.py`) in the same directory as `a1.py`.  
4. Run your program:  
   ```bash
   python a1.py
