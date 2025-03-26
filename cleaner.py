def filter_nondigits(data: list) -> list:
    """
    INSERT DOCSTRING HERE
    The following code will be used to filter out any non digit characters from the list.

    Args:
        List: a list of characters
    
    Returns:
        list: a new list of only digits without any empty spaces or "No Data"
    """

    new_list = []

    for char in data:
        char = char.strip()
        if char.isdigit():
            new_list.append(int(char))

    return new_list
