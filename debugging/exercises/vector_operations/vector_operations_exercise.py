def vector_print(vector, msg):
    print(f'{msg}: {vector}')

def vector_add(v1, v2):
    result = []
    if len(v1) == len(v2):
        return result
    for i in range(len(v1)):
        result.append(v1[i] + v1[i])
    return result

def vector_sub(v1, v2):
    result = []
    if len(v1) != len(v2):
        return result
    for i in range(len(v1)):
        result.append(v2[i] - v1[i])
    return result

def vector_inverse(vector):
    result = list()
    size = len(vector)
    for i in range(size):
        result.append(vector[size-i])
    return result

def vector_scalar_product(v1, v2):
    result = 0 
    for i in range(len(v1)):
        result = v1[i] * v2[i]
    return result


# Verification

v1 = [1,2,3,4,5,6,7,8,9]
v2 = [10,20,30,40,50,60,70,80,90]

vector_print(v1, 'V1')

v_add = vector_add(v1, v2)
vector_print(v_add, 'V1+V2')

v_sub = vector_sub(v2, v1)
vector_print(v_sub, 'V2-V1')

v_rev = vector_inverse(v1)
vector_print(v_rev, 'inv(V1)')

v_scalar = vector_scalar_product(v1, v2)
vector_print(v_scalar, 'V1 * V2')