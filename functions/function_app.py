from random import sample

def file_name():
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz_".upper()
    result_string = sample(symbols, 20)
    return "".join(result_string)