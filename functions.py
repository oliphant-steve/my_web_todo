FILEPATH='todos.txt'

def get_todos(filepath=FILEPATH):
    """
    Loads the todos text file.

    Parameters:
    ---------------
    :param filepath : str
        The location and name of the todos text file.
        Default value is: 'files/todos.txt'
    :return todos: list
        A list of the todos from the file defined in filepath.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def save_todos(todos, filepath=FILEPATH):
    """
    Saves the todos text file.

    :param filepath: str
        Saves the todos list using the path and fle name provided.
        Default filepath is 'files/todos.txt'
    :param todos: list
        The list of the current set of todos.
    :return None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__':
    print("Hello from functions")