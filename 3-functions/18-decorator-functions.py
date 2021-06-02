def decorator(func):
    def wrapper():
        print('start')
        func()
        print('stop')

    return wrapper

def do_it():
    print('did it')

wrapped_do_it = decorator(do_it)

wrapped_do_it()

######
def decorator(func):
    def wrapper():
        print('start')
        func()
        print('stop')

    return wrapper


@decorator
def do_it():
    print('did it')

do_it()

####
def decorator(func):
    def wrapper(message):
        print('start')
        func(message)
        print('stop')

    return wrapper


@decorator
def do_it(message):
    print(message)

do_it('hello!')

####
def decorator(func):
    def wrapper(*args):
        print('start')
        func(*args)
        print('stop')

    return wrapper


@decorator
def do_it(message):
    print(message)

do_it('hello!')

###

def decorator_params(*decorator_args):
    def decorator(func):
        def wrapper(*wrapper_args):
            print('start')
            print(f'decorator_args: {decorator_args}')
            func(*wrapper_args)
            print('stop')

        return wrapper
    return decorator

@decorator_params("a", "b")
def do_it(*args):
    print(*args)

do_it('hello!')