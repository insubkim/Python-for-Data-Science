from ft_filter import ft_filter

def f(v) -> bool:
    if v % 2:
        return False
    return True

a = [1, 2, 3, 5, 6, 7]

ft = ft_filter(f, a)

print(ft)
