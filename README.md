# Zen

Zen Text Editor is a minimalist extensible text editor designed for simplicity
and ease of use.

**@Note:** If you are a CS50 reviewer please goto the CS50 branch and read the
[CS50_README.md](https://github.com/NewDawn0/zen/blob/CS50/CS50_README.md)
aswell

## Contents

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Philosophy](#philosophy)
* [Contributing](#contributing)
    * [Review process](#review-process)
    * [How to contribute](#how-to-contribute)
    * [Code structure](#code-structure)
* [Future Goals](#future-goals)

<!-- vim-markdown-toc -->

## Installation

To install Zen Text Editor, follow these steps:

1. Clone the project
   ```bash
   git clone https://github.com/NewDawn0/zen
   cd zen
   ```
2. Install Zen using pip
   ```bash
   python -m pip install .
   ```

## Usage

```bash
zen <file(s)>
```

## Configuration

On install the Zen editor creates a `~/.config/zen/__init__.py` Using the
[`api`](https://github.com/NewDawn0/zen/tree/main/zen) module of the editor
allows for customizing the editor's behaviour. With the availability of the
[`api`](https://github.com/NewDawn0/zen/tree/main/zen) and creating your own
modules which can be sourced in the `__init__.py` the editor can be extended to
support your own needs.

The Zen editor allows for key chording inspired by
[Emacs](https://www.gnu.org/software/emacs/) with a default timeout of `500ms`.
Whenever a key is pressed, the timeout is reset.

Per default the text editor uses the following key-bindings:

- `<ctrl>i+<space>+i` Trigger info notification
- `<ctrl>o+<space>+o` Open Firefox
- `<space>+e` Toggle file explorer
- `<space>+w` Save file
- `<space>+o` Open file
- `<space>+q` Close file
- `Z+Z` Quit file

## Philosophy

At Zen Text Editor, simplicity is the guiding principle. Keeping the default
user configuration minimal and clutter-free. Rather than packing it with
numerous enabled features and key-binds, aim to provide a streamlined
experience.

The philosophy is to offer a robust set of features as built-ins, readily
available for users to enable as needed. By keeping the default configuration
simple, it empowers users to customize their experience according to their
preferences, without overwhelming them with unnecessary complexity.

Strive to strike a balance between functionality and simplicity, ensuring that
Zen remains intuitive and easy to use, while also offering a wealth of features
for those who seek them.

## Contributing

Thank you for considering contributing to Zen Editor! This project is open to
contributions from anyone interested in improving it. Whether you want to fix a
bug, add a feature, or suggest an enhancement, your contributions are welcome.

### Review process

As the primary maintainer of this project, I strive to review contributions in a
timely manner. However, please note that I may occasionally shift focus to other
projects, which might result in longer review times. Rest assured, your
contributions are valuable, and I will do my best to review and merge them as
promptly as possible. If someone would be interested in reviewing and merging
please contact me and I will appoint you to be the reviewer.

### How to contribute

1. **Fork the Repository:** Start by forking this repository to your GitHub
   account.
2. **Create a branch:** Create a new branch for your contribution. This helps
   keep your changes isolated from the main codebase.

3. **Make Changes:** Implement your changes, whether it's fixing a bug, adding a
   feature, or making an enhancement.

4. **Test Your Changes:** Before submitting your changes, it's crucial to ensure
   that they work as expected and do not introduce any regressions. To
   thoroughly test your modifications, create a test file following the naming
   convention `test_<dir>_<file you are testing>.py`. For instance, if you're
   testing changes in the `api/builtins.py` file, the corresponding test file
   should be named `test_api_builtins.py`. Once you've prepared your test file,
   run the command `pytest tests` to execute the test suite and verify the
   integrity of your changes.

5. **Submit a Pull Request:** Once you're satisfied with your changes, submit a
   pull request. Provide a clear description of your changes and why they are
   valuable.
6. **Review Process:** Your pull request will undergo a review process. I or
   another designated reviewer will provide feedback and may request changes if
   necessary.
7. **Merge:** Once your pull request passes the review process, it will be
   merged into the main codebase.

Thank you for contributing to Zen Editor! Your help is greatly appreciated in
making this project better for everyone. If you have any questions or need
assistance with the contribution process, feel free to reach out.

### Code structure

The codebase of Zen Text Editor is organized into several directories:

- **`api`**: This directory contains modules for user-facing APIs. Functions and
  classes defined here are intended for interaction with the text editor's
  functionality, providing users with programmable control over various aspects
  of the editor's behaviour.

- **`components`**: The `components` directory houses visual UI components
  utilized by the text editor. These components are responsible for rendering
  various elements of the user interface, ensuring a cohesive and user-friendly
  editing experience.

- **`utils`**: Non-visible utilities essential for the functioning of the text
  editor are located in this directory. These utilities may include helper
  functions, data processing modules, or other backend functionalities that
  support the editor's operation.

- **`utils/globals`**: Global variables and instances are stored within this
  subdirectory. Organizing these entities separately helps maintain code clarity
  and prevents clutter in other parts of the codebase.

This structured approach to organizing code ensures maintainability, modularity,
and clarity, making it easier for developers to navigate and contribute to the
Zen Text Editor project.

## Future Goals

In future, if I have the time and motivation, I will try complete the following:

- Rewrite Zen Text Editor in [Rust](https://www.rust-lang.org), utilizing the
  [Dioxus](https://dioxuslabs.com) UI framework
- Implement a plugin system using a WebAssembly System Interface (WASI) and/or a
  [Lua](https://www.lua.org) plugin system similar to [NVim](https://neovim.io)
  using either [rlua](https://crates.io/crates/rlua) or
  [hlua](https://crates.io/crates/hlua)

> ![Rewrite in Rust](https://s3.fission.codes/2022/10/rust_poster.png)
