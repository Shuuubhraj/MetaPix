from PIL import Image
from PIL.ExifTags import GPSTAGS
from tkinter import Tk, filedialog
import os
import sys
import webbrowser
from datetime import datetime
from time import sleep

def read_tag_info(filename):
    tag_info = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                tag, description = line.strip().split('\t')
                tag_info[int(tag)] = description
        return tag_info
    except Exception as e:
        print("Error reading tag information:", e)
        return {}

def generate_html(metadata_dict, image_path, github_url):
    html_content = """<html>
<head>
<title>Image Metadata</title>
<style>
body {
    background-color: black;
    color: green;
    font-family: Arial, sans-serif;
}
h1 {
    color: yellow;
}
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.know-btn {
    background-color: green;
    color: white;
    border: none;
    padding: 5px 10px;
    text-align: center;
    text-decoration: underline;
    font-size: 14px;
}
.logo {
    width: 100px;
}
table {
    border-collapse: collapse;
    width: 80%;
    margin: auto;
    margin-top: 20px;
}
table, th, td {
    border: 1px solid green;
}
th, td {
    padding: 10px;
    text-align: left;
}
.btn {
    background-color: green;
    color: white;
    border: none;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    margin-left: 10px;
}
</style>
</head>
<body>
<div class="header">
    <h1><span style="color: yellow;">Image Metadata</span> <a href="https://exiv2.org/tags.html" class="know-btn" target="_blank">Click here: To Know Exif Tags Meaning</a></h1>
    <a href="https://github.com/shuuubhraj" target="_blank"><img src="resources/git.png" alt="GitHub Logo" class="logo"></a>
</div>
<table>
<tr><th>Tag Description</th><th>Value</th></tr>
"""

    for tag, value in metadata_dict.items():
        if tag == "DateTimeOriginal":
            html_content += f"<tr><td><b>{tag}</b></td><td>{value}</td></tr>"
        elif tag == "File Path":
            html_content += f"<tr><td><b>{tag}</b></td><td>{value} <a href=\"file://{value}\" class=\"btn\" target=\"_blank\">Open File</a></td></tr>"
        else:
            html_content += f"<tr><td><b>{tag}</b></td><td>{value}</td></tr>"

    html_content += """
</table>
</body>
</html>
"""
    return html_content

def main():
    root = Tk()
    root.withdraw()

    banner = "\033[32m" + r'''
███╗   ███╗███████╗████████╗ █████╗ ██████╗ ██╗██╗  ██╗
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║╚██╗██╔╝
██╔████╔██║█████╗     ██║   ███████║██████╔╝██║ ╚███╔╝ 
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔═══╝ ██║ ██╔██╗ 
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ██║██╔╝ ██╗
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝  v1.0
                                                       
'''.strip() + "\033[0m"

    print(banner)

    welcome_message = "\033[31mWelcome to MetaPix – Decode image secrets and uncover hidden details.\033[0m"
    author_info = "\033[33mBy: Rajput Shubhraj Singh\nGithub: @Shuuubhraj\033[0m"

    print("\n")
    print(welcome_message)
    print("\n")
    print(author_info)
    print("\n")
    
    countdown = 6
    image_selection_message = f"\033[37mSelect an image to view its metadata in ({countdown}sec) \033[0m"
    print(image_selection_message, end='', flush=True)
    
    while countdown > 0:
        sleep(1)
        countdown -= 1
        updated_message = f"\r\033[37mSelect an image to view its metadata in ({countdown}sec) \033[0m"
        print("\r" + " " * len(image_selection_message), end='', flush=True)
        print("\r" + updated_message, end='', flush=True)
        
    print("\n")
    
    image_path = filedialog.askopenfilename(title="Select an Image")
    if not image_path:
        print("No image selected. Exiting.")
        sys.exit(0)

    tag_info = read_tag_info("data.txt")
    if not tag_info:
        print("No tag information available. Exiting.")
        sys.exit(0)

    metadata_dict = {}

    try:
        with Image.open(image_path) as img:
            metadata_dict["Image Format"] = img.format
            metadata_dict["Image Size"] = str(img.size)

            metadata_dict["File Name"] = os.path.basename(image_path)
            metadata_dict["File Size"] = f"{os.path.getsize(image_path) / 1024:.2f} KB"
            metadata_dict["File Extension"] = os.path.splitext(image_path)[1]
            metadata_dict["File Path"] = os.path.abspath(image_path)

            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    if tag in tag_info:
                        tag_description = tag_info[tag]
                        if tag_description == "DateTimeOriginal":
                            original_time = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                            formatted_time = original_time.strftime("%I:%M:%S %p")
                            metadata_dict[tag_description] = formatted_time
                        else:
                            metadata_dict[tag_description] = str(value)
    except Exception as e:
        print("Error:", e)

    github_url = "https://github.com/Shuuubhraj"
    
    image_directory = os.path.dirname(image_path)
    local_image_path = os.path.join(image_directory, "resources", "git.png")
    html_content = generate_html(metadata_dict, local_image_path, github_url)
    
    html_file = "image_metadata.html"
    with open(html_file, "w") as f:
        f.write(html_content)

    webbrowser.open(html_file)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
