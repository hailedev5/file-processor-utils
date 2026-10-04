
▎Simple File Processor
A lightweight, robust Python utility for processing text files. This script reads raw input data, applies basic cleaning transformations (stripping whitespace and converting to uppercase), and saves the result to a specified output file, all while maintaining comprehensive logging.

▎✨ Features

• Robust Error Handling: Catches FileNotFoundError, PermissionError, and unexpected exceptions.
• Detailed Logging: Tracks file operations and provides real-time feedback using Python's built-in logging module.
• Simple Logic: Easily customizable to fit your specific text-processing needs.

▎🚀 Getting Started

▎Prerequisites

• Python 3.x installed on your machine.

▎Installation

1. Clone this repository:
      git clone https://github.com/your-username/simple-file-processor.git
   cd simple-file-processor
   

2. No external dependencies are required as the script uses standard Python libraries.

▎Usage

1. Place your source file (e.g., input.txt) in the root directory.
2. Run the script:
      python main.py
   

3. The script will generate an output.txt file with the processed contents.

▎🛠 Customization

You can modify the transformation logic inside the process_data function within main.py:

for line in data:
    # Change the logic here
    clean_line = line.strip().upper() 
    processed_data.append(clean_line)


▎📝 Logging Output

The script provides timestamped logs in the console:

2023-10-27 10:00:00,123 - INFO - Opening file: input.txt
2023-10-27 10:00:00,125 - INFO - Successfully processed 15 lines to output.txt


▎🤝 Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

▎📄 License

This project is open-source and available under the MIT License.