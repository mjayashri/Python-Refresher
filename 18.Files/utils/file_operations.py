def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
