# PicTool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**PicTool** is a simple Python command-line tool for image manipulation.  
It supports:

- **Resizing images**
- **Changing image formats**

All from the terminal, quickly and easily.

---

## Features

- Resize images: `pictool <image_path> -r <width> <height> <new_image_path>`
- Change image format: `pictool <image_path> -f <new_image_path>`
- Cross-platform (Linux, macOS, Windows with Python)

---

## Installation

### Option 1: Install from PyPI / Build Locally

1. Ensure Python ≥ 3.8 is installed.
2. Clone the repository:

```bash
git clone https://github.com/thanthtetaung4/pictool.git
cd pictool
```

3. Build the package:

```bash
python3 -m pip install --upgrade build
python3 -m build
```

4. Install the built wheel:

```bash
pip install dist/pictool-0.1.0-py3-none-any.whl
```

Now the `pictool` command is available globally (or in your virtual environment).

---

### Option 2: Install via `.deb` package (Ubuntu/Debian)

1. Download the latest `.deb` from the [Releases page](https://github.com/thanthtetaung4/pictool/releases/latest):

```bash
wget https://github.com/thanthtetaung4/pictool/releases/latest/download/python3-pictool_0.1.0_all.deb
```

2. Install it using `apt`:

```bash
sudo apt install ./python3-pictool_0.1.0_all.deb
```

3. Test the installation:

```bash
pictool
```

---

## Usage

### Show help

```bash
pictool -h
```

Output:

```
Usage:
  pictool <image_path> -r <width> <height> <new_image_path>
  pictool <image_path> -f <new_image_path>
Options:
  -r     Resize image
  -f     Change image format
  -h     Show this help message
```

### Resize an image

```bash
pictool input.jpg -r 200 200 output.jpg
```

- `input.jpg` → source image
- `200 200` → new width and height
- `output.jpg` → output image path

### Change image format

```bash
pictool input.png -f output.jpg
```

- Converts PNG → JPG

---

## Requirements

- Python ≥ 3.8
- [Pillow](https://python-pillow.org/) library (installed automatically with the package)

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

---
```
