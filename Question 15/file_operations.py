def read_file(file_path):
    """
    Reads the content of a file.
    :param file_path: Path to the file
    :return: Content of the file as a string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except Exception as e:
        return f"Error while reading file: {str(e)}"


def write_file(file_path, data):
    """
    Writes data to a file (overwrites if file exists).
    :param file_path: Path to the file
    :param data: Data to write into the file
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        return f"Data written successfully to '{file_path}'."
    except Exception as e:
        return f"Error while writing to file: {str(e)}"


def append_file(file_path, data):
    """
    Appends data to an existing file (creates file if it doesn’t exist).
    :param file_path: Path to the file
    :param data: Data to append
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(data)
        return f"Data appended successfully to '{file_path}'."
    except Exception as e:
        return f"Error while appending to file: {str(e)}"
