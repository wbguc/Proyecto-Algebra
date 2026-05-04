def format_list_to_line(file_path):
    try:
        with open(file_path, "r") as file:
            # Read lines, strip whitespace, and ignore empty lines
            words = [line.strip() for line in file if line.strip()]

        # Wrap each word in quotes and join with a comma + space
        formatted_string = ", ".join(f'"{word}"' for word in words)

        print(formatted_string)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")


# Run the function
if __name__ == "__main__":
    format_list_to_line("stop_words.txt")
