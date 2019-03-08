""" To execute module as a script
    __name__ evaluates to __main
    special attributes in Python are delimited by double underscores (dunder) """


def zen_of_python():
    import this


if __name__ == '__main__':
    zen_of_python()
