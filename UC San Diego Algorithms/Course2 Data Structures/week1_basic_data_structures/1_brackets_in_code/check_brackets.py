# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    brackets = []
    pos = []
    for i, next in enumerate(text):
        if next in "([{":
            brackets.append(next)
            pos.append(i)
        elif next in ")]}":
            if len(brackets)>0:
                if are_matching(brackets[-1], next):
                    brackets.pop(-1)
                    pos.pop(-1)
                else:
                    return str(i + 1)
            else:
                return str(i + 1)
    if len(brackets) == 0:
        return True
    else:
        return str(pos[-1] + 1)


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == True:
        print('Success')
    elif mismatch == '1':
        print(1)
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
