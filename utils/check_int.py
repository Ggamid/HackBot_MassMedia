def check(_a):
    try:
        int(_a)
        return True
    except ValueError:
        return False