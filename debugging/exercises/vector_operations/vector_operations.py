def vector_print(vector, msg):
    print(f'{msg}: {vector}')

def vector_add(v1, v2):
    result = []
    # Bug: if len(v1) == len(v2):
    if len(v1) != len(v2):
        return result
    for i in range(len(v1)):
        # Bug: result.append(v1[i] + v1[i])
        result.append(v1[i] + v2[i])
    return result

def vector_sub(v1, v2):
    result = []
    if len(v1) != len(v2):
        return result
    for i in range(len(v1)):
        # Bug: result.append(v2[i] - v1[i])
        result.append(v1[i] - v2[i])
    return result

def vector_inverse(vector):
    result = list()
    size = len(vector)
    for i in range(size):
        # Bug: result.append(vector[size-i])
        result.append(vector[size-1-i])
    return result

def vector_scalar_product(v1, v2):
    result = 0 
    for i in range(len(v1)):
        # Bug: result = v1[i] * v2[i]
        result += v1[i] * v2[i]
    return result


# Verification

v1 = [1,2,3,4,5,6,7,8,9]
v2 = [10,20,30,40,50,60,70,80,90]

v_add = vector_add(v1, v2)
assert [1+10, 2+20, 3+30, 4+40, 5+50, 6+60, 7+70, 8+80, 9+90] == v_add

v_sub = vector_sub(v2, v1)
assert [10-1, 20-2, 30-3, 40-4, 50-5, 60-6, 70-7, 80-8, 90-9] == v_sub

v_inv = vector_inverse(v1)
assert [9, 8, 7, 6, 5, 4, 3, 2, 1] == v_inv

v_scalar = vector_scalar_product(v1, v2)
assert 1*10 + 2*20 + 3*30 + 4*40 + 5*50 + 6*60 + 7*70 + 8*80 + 9*90 == v_scalar
