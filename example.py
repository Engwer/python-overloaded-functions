import inspect

def func1(a: int, b: int) -> int:
    return a + b

def func2(a: int, b: list) -> int:
    res = a
    while b:
        res += b.pop()
    return res

def func3(a: list, b: list) -> int:
    a, b = a[::-1], b[::-1]
    res = 0
    while a and b:
        res += a.pop() * b.pop()
    return res

def overload(functions: list):
    def inner(**kwargs):
        for f in functions:
            specs = inspect.getfullargspec(f)
            annotations = specs.annotations
            isMatch = False
            for key in kwargs.keys():
                if key in annotations:
                    var = kwargs[key]
                    varType = annotations[key]
                    if isinstance(var, varType):
                        isMatch = True
                    else:
                        isMatch = False
                        break
            if isMatch:
                return f(**kwargs)
        else:
            raise AttributeError("Function parameters do not match any overloaded function")
    return inner

def func(**kwargs):
    return overload([func1, func2, func3])(**kwargs)

if __name__ == "__main__":
    print(func(a=1, b=2))
    print(func(a=1, b=[2, 3]))
    print(func(a=[3, 2], b=[2, 3, 4]))
    print(func(a=[3, 2], b=(2, 3, 4)))
