
from functools import wraps

from selenium.common.exceptions import StaleElementReferenceException

from config.default_driver_options import NUMBER_OF_TRIES_FOR_STALE_OBJECTS


def stale_element_reference_fix_loop(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        ok = False
        for i in range(NUMBER_OF_TRIES_FOR_STALE_OBJECTS):
            try:
                result = func(*args, **kwargs)
                ok = True
                break
            except StaleElementReferenceException:
                args[0].refresh()       #args[0] is self from method

        if ok is False:
            result = func(*args, **kwargs)
        return result
    return wrapper


def print_hi_for_class_example(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("HI")
        result = func(*args, **kwargs)
        args[0].world()
        print("BYE")
        return result
    return wrapper

def print_hi_for_function_example(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("HI")
        result = func(*args, **kwargs)
        print("BYE")
        return result
    return wrapper


class COCO():
    def __init__(self):
        self.a = 5

    @print_hi_for_class_example
    def power(self, b, c=5):
        print(c)
        return self.a ** b

    def world(self):
        print("World")

@print_hi_for_function_example
def coco():
    print("World")

if __name__ == "__main__":
    print("Returned value of the function, after the call: ", coco())

    print()
    print()
    eu = COCO()
    print("Returned value of the method, after the call: ", eu.power(2))

