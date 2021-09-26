def announce(f):
    def wrapper():
        print("About to run")
        f()
        print("Done with the function")
    return wrapper


@announce  # add decorator
def hello():
    print("Hello,world!")


hello()
