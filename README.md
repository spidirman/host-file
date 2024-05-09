---

# Telegraph File Uploader

This Python script allows you to upload files to Telegraph, a platform for hosting media files, using its API. The script supports various file types including images (JPEG, JPG, PNG, GIF) and videos (MP4).

## Features

- **File Upload**: Upload files to Telegraph for hosting by providing the file path.
- **Supported File Types**: Accepts files with extensions `.jpg`, `.jpeg`, `.png`, `.gif`, and `.mp4`.
- **Simple Interface**: Interact with the script via the command line interface.

## Prerequisites

- Python 3
- requests

## Usage

1. **Clone the Repository**: Clone this repository to your local machine:

   ```
   git clone https://github.com/spidirman/host-file.git
   ```

2. **Install Dependencies**: Install the required dependencies using pip:

   ```
   pip install requests
   ```

3. **Run the Script**: Execute the script by running the Python file:

   ```
   python telegraph.py
   ```

4. **Follow the Prompts**: Enter the file name (including extension) when prompted. Ensure the file exists in the specified location.

5. **Retrieve Telegraph URL**: After successful upload, the script will provide the Telegraph URL of the uploaded file.

## Example

```
$ python telegraph.py
your file name (ex : file.jpg)
>>> example.jpg
https://telegra.ph/your-image-01-01
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script utilizes the Telegraph API to provide a convenient way to host files for various purposes.

---
