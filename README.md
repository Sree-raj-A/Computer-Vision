# BatchCLI Face Blur for Privacy

This is a Python CLI program that censors detected faces in images. It handles a batch of images and outputs the censored batch to a newly created folder. 

---

## Table of Contents

- [Overview](#overview)

- [Prerequisites](#prerequisites)

- [Installation](#installation)

- [Usage](#usage)

- [Configuration](#configuration)

- [How It Works](#how-it-works)

- [Limitations](#limitations)

---

## Overview

This project uses computer vision to blur faces in pictures. It does the following:

- **Detect faces** in pictures using OpenCV

- **Make faces blurry** so the person cannot be identified

- **Process lots of pictures** at the time using a simple command-line interface

The tool looks for picture files in the same folder finds faces in each picture makes them blurry and saves the new pictures to a separate folder. It does not change the pictures.

---

## Prerequisites

You need to have a things installed on your computer before you can use this tool.

### 1. Python 3.7 or higher

You can download Python from the Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

To check if Python is installed you can type this command in your terminal:

```bash

python --version

```

### 2. Pip (Python package manager)

pip is included with Python 3.4 and later. You can check if pip is installed by typing this command:

```bash

pip --version

```

### 3. OpenCV for Python (`opencv-python`)

You need to install OpenCV to use this tool. OpenCV is a computer vision library that helps the tool find faces in pictures. You can install it using pip:

```bash

pip install opencv-python

```

> **Note:** You do not need a computer or graphics card to use this tool. It works on any computer.

---

## Installation

To install the tool you need to do two things:

1. **Download the code:**

```bash

git clone https://github.com/Sree-raj-A/Computer-Vision.git

cd Computer-Vision

```

2. **Install the required library:**

```bash

pip install opencv-python

```

That is all you need to do. You do not need to set up an environment or install anything else.

---

## Usage

To use the tool you need to do three things:

### Step 1. Add your pictures

Put your picture files in the folder as the tool. The tool can process `.jpg` `.jpeg`..Png` files.

### Step 2. Run the tool

```bash

python BatchCLI_Face_Blur_for_Privacy.py

```

### Step 3. Check the results

The tool saves the pictures to a separate folder called `Output`. Your original pictures are not changed.

### Example output

```

Looking for pictures in: /your/project/folder

Saving pictures to: /your/project/folder/Output

Found 3 picture(s). Processing them now...

Processing: photo1.jpg

-> Found 2 face(s). Making them blurry...

-> Saved to Output/photo1.jpg

Processing: group.png

-> Found 5 face(s). Making them blurry...

-> Saved to Output/group.png

Processing: landscape.jpg

-> No faces found. Saving picture.

-> Saved to Output/landscape.jpg

Done processing pictures!

```

---

## Configuration

You can adjust how blurry the faces are by using an option.

### Blur Intensity (`-b` / `--blur`)

You can use the `-b` option to control how blurry the faces are. **Lower numbers make the faces more blurry.**

```bash

python BatchCLI_Face_Blur_for_Privacy.py -b 2    # blurry

python BatchCLI_Face_Blur_for_Privacy.py -b 4    # Default

python BatchCLI_Face_Blur_for_Privacy.py -b 10   # Not blurry

```

| Value | Effect |

|-------|--------|

| 2     | Very blurry (good for privacy)

| 4     | Default. Blurry, but not too much |

| 8+    | Not very blurry you can still see some face features |

### Help

```bash

python BatchCLI_Face_Blur_for_Privacy.py --help

```

---


