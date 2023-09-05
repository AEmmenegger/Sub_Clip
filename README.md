# Subtitle Area Capture Tool

Welcome to the Subtitle Area Capture Tool! This utility is designed to enable users to effortlessly capture subtitles from any section of their screen, and automatically copy the captured subtitles to the clipboard. Whether you're working with video playback tools, streaming platforms, or any other medium - our tool is optimized to streamline the subtitle capturing process.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contribution](#contribution)
4. [Support](#support)
5. [License](#license)

## Installation

Before you can run the Subtitle Area Capture Tool, ensure you have the necessary dependencies installed.

1. **Install the Requirements**:
    ```
    pip install -r requirements.txt
    ```

Make sure you're in the root directory of the project when running this command.

## Usage

### Command-line Arguments

To initiate the tool, you need to provide the type of subtitle color you are working with. The available options are `black` and `white`.

```bash
python japan_sub.py --mask [black/white]
```

For example, if your video has black subtitles:

```bash
python japan_sub.py --mask black
```

### Marking the Capture Area

After calling the script with the appropriate arguments:

1. **Mark the Top-Left Corner**: Click on the top-left corner of the area where the subtitles appear.
2. **Mark the Top-Right Corner**: Click on the top-right corner of the subtitle area.

Post these steps, the script will automatically begin capturing subtitles from the defined area and copying them to your clipboard.

## Contribution

Your contributions are always welcome! Please fork the repository and make changes as you'd like. Pull requests are encouraged.

## Support

If you encounter any bugs or have suggestions, please file an issue in the GitHub issue tracker, or better yet, submit a pull request!

## License

This project is licensed under the terms of the MIT License.
