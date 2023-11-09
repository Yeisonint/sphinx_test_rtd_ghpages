def func(param1, param2, param3):
    # docstring nicely generated
    """_summary_

    :param param1: _description_
    :type param1: _type_
    :param param2: _description_
    :type param2: _type_
    :param param3: _description_
    :type param3: _type_
    :return: _description_
    :rtype: _type_
    """

    random_variable = 42
    string_variable = "not a multiline string"

    return string_variable

def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum