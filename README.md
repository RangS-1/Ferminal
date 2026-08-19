<div align="center">

<a href="https://github.com/RangS-1/Ferminal">
<img src="src/windows/icon.png" alt="Ferminal Icon" width="312" height="272"/>
</a>

# Ferminal

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.4.3-purple)](https://github.com/RangS-1/Ferminal/releases)

**A lightweight custom terminal and CLI wrapper built with Python.**

</div>

**Ferminal** is a lightweight Python-based terminal designed to make common command-line tasks shorter and easier to access.

Instead of repeatedly typing longer commands such as `mkdir`, `cd`, `git status`, or `git clone`, Ferminal provides short custom commands and aliases for frequently used operations.

Ferminal also includes utilities for:

- File and directory management
- Git operations
- Project template generation
- A simple interactive terminal interface

> **Note:** Ferminal is currently a lightweight wrapper around existing system commands rather than a replacement shell.

## Features

- ⚡ Short command aliases for common terminal operations
- 📁 File and directory management
- 🌿 Built-in Git command shortcuts
- 🧰 Project template generator
- 🐍 Python-based and lightweight
- 🖥️ Available through prebuilt releases and platform-specific packages

## Requirements

For running Ferminal from source, the documentation currently lists:

- Python **3.13 or newer**
- Git
- `colorama`
- `prompt_toolkit`

Additional Python packages are required when building/installing the package from source:

- `python-build`
- `python-wheel`
- `python-installer`

See the full installation guide for platform-specific requirements.

## Installation

### Arch Linux

Ferminal is available through the Arch User Repository (AUR).

Using `yay`:

```bash
yay -S ferminal
```

Using `paru`:

```bash
paru -S ferminal
```

You can also build the package manually:

```bash
git clone https://github.com/RangS-1/Ferminal.git
cd Ferminal
makepkg -si
```

### Windows

The easiest way to install Ferminal on Windows is through the prebuilt executable.

1. Open the [Ferminal Releases](https://github.com/RangS-1/Ferminal/releases) page.
2. Open the latest release.
3. Download the `.exe` file from **Assets**.
4. Run the executable.

### FreeBSD

Prebuilt `.pkg` packages are available through the GitHub Releases page.

Download the appropriate package and install it with:

```sh
pkg install ferminal-<version>.pkg
```

For the latest platform-specific instructions, see the documentation.

## Quick Start

After launching Ferminal, you can use its short commands from the interactive prompt.

### Basic commands

| Command | Description |
|---|---|
| `h` | Show the Ferminal help menu |
| `b` | Clear the screen |
| `l` | List directory contents |
| `la` | List directory contents including hidden files |
| `w` | Show the current working directory |
| `d <path>` | Change directory |
| `k <name>` | Create a directory |
| `m <name>` | Remove a directory |
| `r <file>` | Remove a file |
| `f <file>` | Create a file |
| `v ...` | Move a file or directory |
| `c ...` | Copy a file |
| `u <file>` | Display file contents |
| `p <host>` | Ping a host |
| `x` | Exit Ferminal |

Ferminal also provides shortcuts for common Git operations and project generation.

For the complete command reference, see the documentation.

## Git Shortcuts

Ferminal provides short aliases for several Git commands, including:

```text
gia   git add
gis   git status
gic   git clone
gin   git init
gib   git branch
gip   git pull
gih   git push
gim   git commit
gil   git log
gif   git fetch
gir   git remote
gie   git merge
gio   git checkout
gig   git tag
gid   git diff
girs  git restore
gist  git stash
gista git stash apply
gish  git show
gibl  git blame
```

Refer to the Git documentation page for the exact syntax and arguments supported by each shortcut.

## Project Generator

Ferminal can generate projects from templates stored in the `rrc` repository.

Available templates include:

```text
nm                 # check or update the templates repo
nm py
nm blog
nm doc
nm love2d
nm react
```

The project generator uses the `~/.rrc` directory. If the directory does not exist, Ferminal can clone the template repository automatically. When `nm` is used without a template name, it checks for `~/.rrc` and offers to update it. The template repository is on:

**[RRC Repository](https://github.com/RangS-1/RRC)**

## Documentation

The README is intended as a quick introduction. For complete usage instructions, installation details, command references, Git shortcuts, and the project generator, visit:

**[Ferminal Documentation](https://rangs-1.github.io/Ferminal/)**

## Repository

**GitHub:** [RangS-1/Ferminal](https://github.com/RangS-1/Ferminal)

**Releases:** [Ferminal Releases](https://github.com/RangS-1/Ferminal/releases)

**AUR:** [Ferminal on AUR](https://aur.archlinux.org/packages/ferminal)

## License

Ferminal is released under the **MIT License**.

See the [LICENSE](LICENSE) file for the complete license text.
