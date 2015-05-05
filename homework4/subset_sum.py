#algorithm at http://en.wikipedia.org/wiki/Subset_sum_problem
def subset_sum(input_list, input_sum):
    s = [0]
    p = 5
    c = 2 ** -p
    if input_sum == 0:
        return True
    for i in input_list:
        t = []
        for y in s:
            t.append(i + y)

        union_of_s_and_t = s
        union_of_s_and_t += t
        union_of_s_and_t.sort()
        s = []
        k = union_of_s_and_t[0]
        s.append(k)
        for z in union_of_s_and_t:
            if k + c * input_sum / len(input_list) < z and z not in s:
                union_of_s_and_t[0] = z
                s.append(z)

    for i in s:
        if (i > 0 and (1 - c) * input_sum <= i <= input_sum) or \
        (i < 0 and (1 - c) * input_sum >= i >= input_sum):
            return True
    return False