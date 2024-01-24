#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    func_names = dir(hidden_4)

    for i in func_names:
        if (i[:2] != "__"):
            print(i)
