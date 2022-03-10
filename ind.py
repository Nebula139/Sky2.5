#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def before_max(*args):
    if args:
        ans = 0
        idx = args.index(max(args))
        for item in args:
            if args.index(item) < idx:
                ans += item
        return ans
    else:
        return None


if __name__ == "__main__":
    print(before_max())
    print(before_max(2, 1, 0, 8, 7))
    print(before_max(2, 4, 5, 1, 6, 3))
