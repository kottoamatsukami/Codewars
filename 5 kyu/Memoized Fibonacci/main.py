def memorize():
    memory = {
        0: 0,
        1: 1,
    }

    def _wrapper(n):
        if n in memory.keys():
            return memory[n]
        else:
            out = _wrapper(n-1) + _wrapper(n-2)
            memory[n] = out
            return out
    return _wrapper


@memorize()
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
