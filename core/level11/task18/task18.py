# Зона видимости переменной.

# Исправьте код, чтобы последний print выводил исключение.

# def bar(i):
#     if i == 1:
#         raise KeyError(1)
#     if i == 2:
#         raise ValueError(2)
#
# def bad():
#     try:
#         bar(1)
#     except KeyError as e:
#         print('key error')
#     except ValueError as e:
#         print('value error')
#     print(e)  # This should raise an exception because e is not defined in this scope
#
# bad()
def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    exception=None
    try:
        bar(1)
    except KeyError as e:
        print('key error')
        exception = e
    except ValueError as e:
        print('value error')
        exception = e
    print(exception)  # This should raise an exception because e is not defined in this scope

bad()
