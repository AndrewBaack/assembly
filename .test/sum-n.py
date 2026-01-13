
from util import nios2_as, get_debug, require_symbols
from csim import Nios2


def check_sum_n(asm):
    obj = nios2_as(asm.encode('utf-8'))
    r = require_symbols(obj, ['N', '_start'])
    if r is not None:
        print('Error: did not find symbols', r)
        return

    cpu = Nios2(obj=obj)

    passed = 0
    feedback = ''

    test_cases = [(10,55), (9,45), (20,210), (555,154290)]

    for cur_test, (n,ans) in enumerate(test_cases):
        # Setup CPU and N
        cpu.reset()
        cpu.write_symbol_word('N', n)

        # Run
        instrs = cpu.run_until_halted(1000000)

        their_ans = cpu.get_reg(2)
        if their_ans != ans:
            feedback += 'Failed test case %d: \n' % (cur_test)
            feedback += 'r2 should be %d for N = %d\n' % (ans,n)
            feedback += 'Your code produced r2 = %d\n' % (their_ans)
            feedback += get_debug(cpu)
            break
        passed += 1


    err = cpu.get_error()
    if err != '':
        print(err)
    del cpu

    if passed == len(test_cases):
        print('Passed all tests')
    else:
        print('Tests missed:')
        print(feedback)


import sys
check_sum_n(sys.stdin.read())
