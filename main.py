import logging

# Configure logging to track what happens during execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(input_file, output_file):
    """
    Reads data, performs a calculation, and writes to a new file.
    Handles common issues like FileNotFoundError or PermissionError.
    """
    try:
        logging.info(f"Opening file: {input_file}")
        with open(input_file, 'r') as file:
            data = file.readlines()

        processed_data = []
        for line in data:
            # Example logic: strip whitespace and convert to uppercase
            clean_line = line.strip().upper()
            processed_data.append(clean_line)

        with open(output_file, 'w') as file:
            for item in processed_data:
                file.write(f"{item}\n")
        
        logging.info(f"Successfully processed {len(processed_data)} lines to {output_file}")

    except FileNotFoundError:
        logging.error(f"The file {input_file} was not found.")
    except PermissionError:
        logging.error(f"Permission denied accessing {input_file}.")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    process_data('input.txt', 'output.txt')