t = int(input())

def get_string(pattern):
    len_pattern = []
    for m in pattern:
        len_pattern.append(len(m))
    max_len = max(len_pattern)
    index = len_pattern.index(max_len)
    longest = pattern[index]
    if longest[-1] == '*':
        possible = True
        for i in pattern:
            if longest[0:len(i) - 1] == i[:-1]:
                pass
            else:
                possible = False
        return possible, longest

    else:
        possible = True
        for i in pattern:
            if longest[max_len - len(i) + 1:] == i[1:]:
                pass
            else:
                possible = False
        return possible, longest

for o in range(t):
    n = int(input())
    pattern = []
    for p in range(n):
        pattern.append(input())
    before_asterisk = []
    after_asterisk = []
    merge_item = []
    for item in pattern:
        index = [i for i, value in enumerate(item) if value == '*']
        before_asterisk.append(item[0:index[0]] + '*')
        after_asterisk.append('*' + item[index[-1]+1:])
        if index[0] == index[-1]:
            merge_item.append(False)
        else:
            merge_item.append(True)
    before_possible, before_longest = get_string(before_asterisk)
    after_possible, after_longest = get_string(after_asterisk)

    ans = before_longest[:-1]

    for i in range(len(pattern)):
        if merge_item[i]:
            index = [j for j, value in enumerate(pattern[i]) if value == '*']
            val = pattern[i][index[0] : index[-1]+1]
            val = val.replace('*', '')
            ans += val
    ans += after_longest[1:]

    if before_possible and after_possible:
        print('Case #' + str(o + 1) + ': ' + ans)
    else:
        print('Case #' + str(o + 1) + ': *' )