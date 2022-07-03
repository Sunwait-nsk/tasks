def count_el(el: int, sp: list) -> int:
    result = 0
    el1 = el
    el2 = el
    while result == 0:
        if sp.count(el1) > 0 and sp.count(el2) > 0:
            result = sp[min(sp.index(el1), sp.index(el2))]
        elif sp.count(el1) > 0:
            result = el1
        elif sp.count(el2) > 0:
            result = el2

        else:
            el1 += 1
            el2 -= 1
    return result


command = int(input())
result = []
for c in range(command):
    len_com = int(input())
    abcdef = input().split()
    st = [int(x) for x in abcdef]
    st1 = [x + 1 for x in range(len_com)]
    for _ in range(len_com // 2):
        ind_first = st1[0]
        first = st[0]
        st.pop(0)
        st1.pop(0)

        ind_sec = count_el(first, st)  # число ближайшее
        x = st.index(ind_sec)
        ind = st1[x]
        st.pop(x)
        st1.pop(x)
        result.append('{} {}\n'.format(ind_first, ind))
    if c < command:
        result.append('\n')
result_out = "".join(result)
print(result_out)
