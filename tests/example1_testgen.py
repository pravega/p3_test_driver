#!/usr/bin/env python3

"""
This script generates test definitions for P3 Test Driver.
Usage: tests/example1_testgen.py | p3_test_driver -t -
"""

import json
import sys


def add_test():
    t = dict(
        test='simple',
        command='echo hello world param1=%d, param2=%s' % (param1, param2),
        param1=param1,
    )
    test_list.append(t)


test_list = []

for param1 in [1, 2, 4]:
    for param2 in ['a', 'b']:
        add_test()

print(json.dumps(test_list, sort_keys=True, indent=4, ensure_ascii=False))
print('Number of tests generated: %d' % len(test_list), file=sys.stderr)
