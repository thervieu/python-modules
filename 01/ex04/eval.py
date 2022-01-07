class Evaluator():

    def zip_evaluate(*args):
        if len(args) != 2:
            raise ValueError("zip_evaluate: <words> <coefs>")
        if isinstance(args[0], list) is False or isinstance(args[1], list) is False:
            raise ValueError("zip_evaluate: words and coefs must be lists")
        for a in args[0]:
            if isinstance(a, float) is False:
                raise ValueError("zip_evaluate: words must only be strings")
        for b in args[1]:
            if isinstance(b, str) is False:
                raise ValueError("zip_evaluate: coefs must only be floats")
        if len(args[0]) != len(args[1]):
            return -1
        return sum(a * len(b) for a, b in zip(args[0], args[1]))

    def enumerate_evaluate(*args):
        if len(args) != 2:
            raise ValueError("zip_evaluate: <words> <coefs>")
        if isinstance(args[0], list) is False or isinstance(args[1], list) is False:
            raise ValueError("zip_evaluate: words and coefs must be lists")
        for a in args[0]:
            if isinstance(a, float) is False:
                raise ValueError("zip_evaluate: words must only be strings")
        for b in args[1]:
            if isinstance(b, str) is False:
                raise ValueError("zip_evaluate: coefs must only be floats")
        if len(args[0]) != len(args[1]):
            return -1
        return sum(args[0][elem[0]] * len(elem[1]) for elem in enumerate(args[1]))
