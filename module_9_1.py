def m_in(args):
    return min(args)


def m_ax(args):
    return max(args)


def l_en(args):
    return len(args)


def s_um(args):
    return sum(args)


def sor_ted(args):
    return sorted(args)


def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))