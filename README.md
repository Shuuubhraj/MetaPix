<h1 align="left">MetaPix</h1>

<p align="left">
  <img src="https://img.shields.io/badge/MetaPix-v1.0-008000">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg">
</p>

MetaPix is a tool that decodes image metadata and uncovers hidden details in images. It provides a graphical user interface (GUI) built with the Tkinter library to display the metadata of selected images.

---

<h2>Features</h2>

- Decode and display image metadata, including format, size, file name, and more.
- View image details such as file size, file extension, and file path.
- Show Exif data (if available) with descriptions of various tags.
- Open images and their metadata in a user-friendly HTML report.

---

<h2>Prerequisites</h2>

- Python 3.6+
- Required Python libraries: `PIL`, `tkinter`, `os`, `sys`, `webbrowser`, `datetime`, `time`

---

<h2>Executable Version (Windows)</h2>

An executable version of MetaPix is available for Windows users. You can download it. The executable version doesn't require Python to be installed.

[Download MetaPix.exe](https://mega.nz/file/AIZFAQBQ#6ran7Rj3zc0eg1XA5AN7vE_ZSRvnD699BxEHVc0tkgs)

---

<h2>Usage</h2>

1. Run the `MetaPix.py` script using Python.
2. A countdown will start; select an image to view its metadata.
3. The tool will display metadata details and Exif information (if available).
4. An HTML report containing the metadata will open in your default web browser.

---

<h2>Important Notes</h2>

- **Do not delete the "resources" folder**: The "resources" folder contains necessary files for the tool to function properly. Deleting it may cause errors in the tool's operation. Make sure to keep this folder intact.

- **Editing the "data.txt" file**: The "data.txt" file contains tag information that the tool relies on. You can modify this file to update or add tag descriptions. However, be cautious not to break the file's format.

- **Using the tool**:
  - Run the script and select an image file to view its metadata.
  - The generated HTML page will display metadata information along with a link to open the image file.

- **Disclaimer**: This tool is provided as-is without any warranties. Use at your own risk.

- **GitHub Repository**: The source code for this tool can be found at my GitHub profile. Feel free to provide feedback.

---

<h2>Author</h2>

GitHub: [@Shuuubhraj](https://github.com/shuuubhraj)

---

<h2>Acknowledgement</h2>

MetaPix utilizes the PIL (Pillow) library to extract image metadata and the Tkinter library to build the GUI. The Exif tag descriptions are sourced from the `data.txt` file, making it easier for users to understand the metadata information.

I appreciate the open-source contributions made by various developers that empower projects like MetaPix with functionality and usability.

---

