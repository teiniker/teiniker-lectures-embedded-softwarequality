# Example: Use ChatGPT5 to Decompile Python Bytecode


## Prompt

> Given the following Python 3.13 Bytecode, generate the corresponding Source Code:

```
0 LOAD_CONST 0 (code object fibonacci)
2 MAKE_FUNCTION
4 STORE_NAME 0 (fibonacci)

6 LOAD_NAME 1 (__name__)
8 LOAD_CONST 1 ("__main__")
10 COMPARE_OP 88 (==)
12 POP_JUMP_IF_FALSE 23 (to 34)

14 LOAD_CONST 2 (0)
16 LOAD_CONST 3 (None)
18 IMPORT_NAME 2 (dis)
20 STORE_NAME 2 (dis)

22 LOAD_NAME 2 (dis)
24 LOAD_ATTR 4 (dis)
26 PUSH_NULL
28 LOAD_NAME 0 (fibonacci)
30 CALL 1
32 POP_TOP
34 RETURN_CONST 3 (None)

36 RETURN_CONST 3 (None)


0 LOAD_FAST 0 (n)
2 LOAD_CONST 1 (0)
4 COMPARE_OP 58 (<=)
6 POP_JUMP_IF_FALSE 1 (to 8)

8 RETURN_CONST 1 (0)

10 LOAD_FAST 0 (n)
12 LOAD_CONST 2 (1)
14 COMPARE_OP 88 (==)
16 POP_JUMP_IF_FALSE 1 (to 18)

18 RETURN_CONST 2 (1)

20 LOAD_CONST 3 ((0, 1))
22 UNPACK_SEQUENCE 2
24 STORE_FAST_STORE_FAST 18 (a, b)

26 LOAD_GLOBAL 1 (NULL + range)
28 LOAD_CONST 4 (2)
30 LOAD_FAST 0 (n)
32 LOAD_CONST 2 (1)
34 BINARY_OP 0 (+)
36 CALL 2
38 GET_ITER
40 FOR_ITER 8 (to 54)
42 STORE_FAST 3 (_)

44 LOAD_FAST_LOAD_FAST 33 (b, a)
46 LOAD_FAST 2 (b)
48 BINARY_OP 0 (+)
50 STORE_FAST_STORE_FAST 33 (b, a)
52 JUMP_BACKWARD 10 (to 38)

54 END_FOR
56 POP_TOP

58 LOAD_FAST 2 (b)
60 RETURN_VALUE
```

## ChatGPT5 Answer

```python
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        b, a = a + b, b
    return b


if __name__ == "__main__":
    import dis
    dis.dis(fibonacci)
```

*Egon Teiniker, 2025, GPL v3.0*