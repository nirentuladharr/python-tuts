#doesnt work with python3

def my_logger(orig_func):
    import logging
    logging.basicConfig(fileName="{}.log".format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age):
    print("display_info ran with args ({}, {})".format(name, age))
display_info("John", 25)