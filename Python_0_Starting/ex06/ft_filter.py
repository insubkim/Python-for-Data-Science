def ft_filter(expr: type(abs), iter_obj: type(list)):
    # assert type(expr) is type(abs), 'expr is not function'

    if type(iter_obj) is type([]):
        return [iter_obj for iter_obj in iter_obj if expr(iter_obj)]
    elif type(iter_obj) is type({}):
        return {iter_obj for iter_obj in iter_obj if expr(iter_obj)}
    else:
        assert False is type(list), 'iter_obj is not iterable'
