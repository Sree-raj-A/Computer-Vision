
# BatchCLI Face Blur for Privacy

This is a Python CLI program that **blurs** detected faces in images. It handles a batch of images and outputs the **blurred** batch to a newly created folder.
---
## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
---
## Overview
This project uses computer vision to blur faces in images. It does the following:
- **Detect faces** in images using OpenCV
- **Blur faces** so the person cannot be identified
- **Process multiple images at a time** using a simple command-line interface

The tool looks for image files in the same folder, finds faces in each image, blurs them, and saves the processed images to a separate folder. It does not modify the original images.
You do not need a **GPU or dedicated graphics card** to use this tool. It works on any computer, as long the libraries are supported.

---
## Prerequisites
You need to have **a few** things installed on your computer before you can use this tool.
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
You need to install OpenCV to use this tool. OpenCV is a computer vision library that helps the tool find faces in images. You can install it using pip:
```bash
pip install opencv-python
```
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
### Step 1. Add your images
Put your image files in the **same** folder as the tool. The tool can process `.jpg`, `.jpeg`, and `.png` files.
### Step 2. Run the tool
```bash
python BatchCLI_Face_Blur_for_Privacy.py
```
### Step 3. Check the results
The tool saves the images to a separate folder called `Output`. Your original images are not changed.
### Example output
```
Scanning for images in: /your/project/folder
Saving images to: /your/project/folder/Output

Found 3 image(s). Processing them now...

Processing: photo1.jpg
 -> Detected 2 face(s). Applying blur...
 -> Saved to Output/photo1.jpg

Processing: group.png
 -> Detected 5 face(s). Applying blur...
 -> Saved to Output/group.png

Processing: landscape.jpg
 -> No faces detected. Saving original image.
 -> Saved to Output/landscape.jpg

Batch processing complete!
```
---
## Configuration
You can adjust the blur intensity by using an option.
### Blur Intensity (`-b` / `--blur`)
You can use the `-b` option to control how strongly faces are blurred. **Lower numbers produce a stronger blur.**
```bash
python BatchCLI_Face_Blur_for_Privacy.py -b 2    # Strong blur
python BatchCLI_Face_Blur_for_Privacy.py -b 4    # Default
python BatchCLI_Face_Blur_for_Privacy.py -b 10   # Subtle blur
```
### Help
```bash
python BatchCLI_Face_Blur_for_Privacy.py --help
```
