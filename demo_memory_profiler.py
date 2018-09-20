from memory_profiler import profile

MEMORY_PROFILING = True

""" Ceci est un décorateur """


def activate(func):
    if MEMORY_PROFILING:
        return profile(func)
    else:
        return func


"""
Le décorateur @profile permet le profiling 
Le décorateur @activate lance le profiling si MEMORY_PROFILING == True
"""


# @profile
@activate
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    for tour in range(5):
        my_func()
