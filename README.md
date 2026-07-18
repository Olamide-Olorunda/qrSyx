# qrSyx

QR code generator built with Python and tkinter. Enter text or a URL, and it saves a PNG QR code.

## Requirements

- Python 3.x
- **Tkinter (Tk)** — this is part of Python's standard library, but it depends on the system Tk libraries being present. It is **not** a pip package, so do not add it to `requirements.txt` or try `pip install tkinter`. How you get it depends on your OS (see below).
- The Python packages listed in `requirements.txt` (installed with pip): `pyqrcode`, `pypng`, `Pillow`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Olamide-Olorunda/qrSyx.git
cd qrSyx
```

Make sure Tkinter is available for your platform:

- **macOS** — the easiest route is the official installer from [python.org](https://www.python.org/downloads/), which bundles Tk. If you use Homebrew's Python instead, install the matching Tk package once, e.g. `brew install python-tk@3.14` (match your Python version).
- **Linux** — Tk usually is not installed by default:
  - Debian/Ubuntu: `sudo apt install python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - Arch: `sudo pacman -S tk`
- **Windows** — the official python.org installer includes Tk by default; no extra step needed.

Verify Tk is available:

```bash
python3 -c "import tkinter; print('Tk', tkinter.TkVersion)"
```

Create a virtual environment and install the pip dependencies:

```bash
python3 -m venv .venv
# macOS/Linux:
.venv/bin/pip install -r requirements.txt
# Windows:
.venv\Scripts\pip install -r requirements.txt
```

## Usage

Run the script:

```bash
# macOS/Linux:
.venv/bin/python qrSyx.py
# Windows:
.venv\Scripts\python qrSyx.py
```

(Or `python qrSyx.py` / `python3 qrSyx.py` if you are not using a virtual environment and Tk is available on that interpreter.)

Enter any text or URL in the input field, click "Create QR Code", choose where to save the PNG, and your QR code will be generated and displayed.
