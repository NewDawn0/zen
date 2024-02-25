# Zen

Zen Text Editor is a minimalist extensible text editor designed for simplicity
and ease of use.

## Contents

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
* [Usage](#usage)
* [Future Goals](#future-goals)
* [Contributing](#contributing)
    * [Api reference](#api-reference)
* [My experience](#my-experience)
    * [Challenges and Hardships](#challenges-and-hardships)

<!-- vim-markdown-toc -->

## Installation

To install Zen Text Editor, follow these steps:

1. Clone the project
   ```bash
   git clone https://github.com/NewDawn0/zen
   cd zen
   ```
2. Create and activate a new virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages using pip
   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

## Future Goals

In future, If I have the time and motivation, I will try complete the follwing:

- Rewrite Zen Text Editor in [Rust](https://www.rust-lang.org), utilizing the
  [Dioxus](https://dioxuslabs.com) UI framework
- Implement a plugin system using a WebAssembly System Interface (WASI) and/or a
  [Lua](https://www.lua.org) plugin system similar to [NVim](https://neovim.io)
  using either [rlua](https://crates.io/crates/rlua) or
  [hlua](https://crates.io/crates/hlua)

![Rewrite in Rust](https://s3.fission.codes/2022/10/rust_poster.png)

## Contributing

### Api reference

## My experience

### Challenges and Hardships

During the development process, I encountered several challenges, including:

- Missing data types like `uint`, commonly found in languages like C, C++, Go,
  and Rust.
- Issues with Python's import system, leading to potential circular imports and
  clashes, which were mitigated by organizing global variables into separate
  files in the `utils/globals` directory.
