import pytest

# generate_pyramid
def generate_pyramid(n, char='*'):
    if not isinstance(n, int) or not (1 <= n <= 20):
        raise ValueError("n must be between 1 and 20.")
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("char must be a single character string.")

    pyramid = ""
    for i in range(n):
        num_chars = 2 * i + 1
        num_spaces = n - i - 1
        level = ' ' * num_spaces + char * num_chars + '\n'
        pyramid += level
        
    return pyramid.rstrip()  


# Testing: run "pytest generate_pyramid.py" in terminal

def test_generate_pyramid():
    # Verify the default character is '*'
    assert generate_pyramid(1) == '*'
    
    # Verify the char can be a different character
    assert generate_pyramid(1, '#') == '#'
    assert generate_pyramid(2, '@') == ' @\n@@@'
    assert generate_pyramid(3, '!') == '  !\n !!!\n!!!!!'
    
    # Test edge case
    assert generate_pyramid(20, '*') == (
'                   *\n                  ***\n                 *****\n                *******\n               *********\n              ***********\n             *************\n            ***************\n           *****************\n          *******************\n         *********************\n        ***********************\n       *************************\n      ***************************\n     *****************************\n    *******************************\n   *********************************\n  ***********************************\n *************************************\n***************************************'
    )

    # Test exceptional cases
    # Verify n cannot < 1
    with pytest.raises(ValueError):
        generate_pyramid(0)

    # Verify n cannot > 20
    with pytest.raises(ValueError):
        generate_pyramid(21)

    # Verify char is a single character
    with pytest.raises(ValueError):
        generate_pyramid(5, '##')

    # Verify char cannot be null
    with pytest.raises(ValueError):
        generate_pyramid(5, '')