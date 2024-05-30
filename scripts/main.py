class Test:
    """
    New class
    """

    def __init__(self, info: str):
        self.info = info

    def run(self):
        """Test method

        :return: str - Hello world
        """
        return 'Hello world!'


def fun():
    """ Function

    :return: int
    """

    return 7


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
