from util import nios2_as, get_debug, require_symbols
from csim import Nios2
import ctypes

def check_if_else(asm):
    obj = nios2_as(asm.encode('utf-8'))
    cpu = Nios2(obj=obj)

    passed = 0
    feedback = ''

    test_cases = [(1, 2, 3, 3), (15, 10, 5, 15), (30, 83, 19, 83), (14, 14, 20, 20), (99, 99, -3, 99), (-2, 0, -1, 0)]

    for test_num, (n1, n2, n3, ans) in enumerate(test_cases):
        cpu.reset()

        cpu.set_reg(4, n1)
        cpu.set_reg(5, n2)
        cpu.set_reg(6, n3)

        instrs = cpu.run_until_halted(1000000)

        their_ans = ctypes.c_int32(cpu.get_reg(2)).value

        if their_ans != ans:
            feedback += 'Failed test case %d: \n' % (test_num)
            feedback += 'r2 should be %d for (%d, %d, %d) \n' % (ans, n1, n2, n3)
            feedback += 'Your code produced r2 = %d \n' % (their_ans)
            feedback += get_debug(cpu)
            break
        passed += 1

    err = cpu.get_error()
    if err != '':
        print(err)
    del cpu

    if instrs == 1000000:
        print('Break never executed')
    elif passed == len(test_cases):
        print('Passed all tests')
    else:
        print('Tests Missed:')
        print(feedback)

import sys
check_if_else(sys.stdin.read())
