try:
    # ValueError
    num = int("abc")

    # TypeError
    result = 10 + "20"

    # ZeroDivisionError
    a = 10 / 0

    # IndexError
    lst = [1, 2, 3]
    print(lst[5])

    # KeyError
    d = {"name": "Rahul"}
    print(d["age"])

    # FileNotFoundError
    file = open("student.txt", "r")

    # NameError
    print(x)

    # AttributeError
    s = "Python"
    s.append("A")

    # ImportError
    from math import xyz

    # AssertionError
    assert 5 > 10, "Assertion Failed"

    # StopIteration
    it = iter([1, 2])
    next(it)
    next(it)
    next(it)

    # OverflowError
    import math
    print(math.exp(1000))

except ValueError:
    print("ValueError handled")

except TypeError:
    print("TypeError handled")

except ZeroDivisionError:
    print("ZeroDivisionError handled")

except IndexError:
    print("IndexError handled")

except KeyError:
    print("KeyError handled")

except FileNotFoundError:
    print("FileNotFoundError handled")

except NameError:
    print("NameError handled")

except AttributeError:
    print("AttributeError handled")

except ImportError:
    print("ImportError handled")

except AssertionError:
    print("AssertionError handled")

except StopIteration:
    print("StopIteration handled")

except OverflowError:
    print("OverflowError handled")

else:
    print("No exception occurred")

finally:
    print("Program execution completed")