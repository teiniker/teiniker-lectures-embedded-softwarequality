"""
This module contains code which has benn improved by the help of Pylint.
"""

def vector_print(vector, msg):
    """Print the content of a given vector."""
    print(f'{msg}: {vector}')

def vector_add(vector1, vector2):
    """Add the elements of two vectors one by one."""
    result = []
    if len(vector1) != len(vector2):
        return result
    for element1, element2 in zip(vector1, vector2):
        result.append(element1 + element2)
    return result

def vector_sub(vector1, vector2):
    """Subtract the elements of two vectors one by one."""
    result = []
    if len(vector1) != len(vector2):
        return result
    for element1, element2 in zip(vector1, vector2):
        result.append(element1 - element2)
    return result

def vector_inverse(vector):
    """Inverse the order or elements in the given vector."""
    result = []
    size = len(vector)
    for i in range(size):
        result.append(vector[size-1-i])
    return result

def vector_scalar_product(vector1, vector2):
    """Calculate the scalar product of the two given vectors."""
    result = 0
    for element1, element2 in zip(vector1, vector2):
        result += element1 * element2
    return result


# Verification

v1 = [1,2,3,4,5,6,7,8,9]
v2 = [10,20,30,40,50,60,70,80,90]

vector_print(v1, 'V1')

v_add = vector_add(v1, v2)
vector_print(v_add, 'V1+V2')
assert [1+10, 2+20, 3+30, 4+40, 5+50, 6+60, 7+70, 8+80, 9+90] == v_add

v_sub = vector_sub(v2, v1)
vector_print(v_sub, 'V2-V1')
assert [10-1, 20-2, 30-3, 40-4, 50-5, 60-6, 70-7, 80-8, 90-9] == v_sub

v_inv = vector_inverse(v1)
vector_print(v_inv, 'inv(V1)')
assert [9, 8, 7, 6, 5, 4, 3, 2, 1] == v_inv

v_scalar = vector_scalar_product(v1, v2)
vector_print(v_scalar, 'V1 * V2')
assert 1*10 + 2*20 + 3*30 + 4*40 + 5*50 + 6*60 + 7*70 + 8*80 + 9*90 == v_scalar
