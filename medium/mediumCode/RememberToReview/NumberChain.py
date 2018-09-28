import sys


if __name__ == "__main__":

    for i, v in enumerate(sys.stdin.readlines()):

        if i % 2 == 1:
            v = v.strip().split()
            v.sort(cmp=lambda x, y: cmp(x + y, y + x), reverse=True)
        #     print v
            print('0' if v[0] == '0'else "".join(v))