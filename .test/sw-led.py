from util import nios2_as, get_debug, require_symbols, hotpatch, get_clobbered, get_regs
from csim import Nios2

def check_p1(asm):
    obj = nios2_as(asm.encode('utf-8'))
    cpu = Nios2(obj=obj)

    class p1grader(object):
        def __init__(self, test_cases=[]):
            # test_cases is an array of (sw_val, expected_led_val)
            self.test_cases = test_cases
            self.cur_test = 0
            self.feedback = ''
            self.num_passed = 0

        def write_led(self, val):
            # Check it's the correct value            
            sw, expected = self.test_cases[self.cur_test]
            if val != expected:
                led_val = val & 0x3ff
                if led_val != expected:
                    # only looking at the 10 that would set an LED
                    self.feedback += 'Failed test case %d: ' % (self.cur_test+1)
                    self.feedback += f'LEDs set to {led_val:08b} (should be {expected:08b}) for SW {sw:010b}'
                    self.feedback += get_debug(cpu)
                    cpu.halt()
                    return
                #else:
                    #self.feedback += 'Test case %d: ' % (self.cur_test+1)
                    #self.feedback += f'Warning: wrote 0x{val:08x} (instead of 0x{expected:08x}) to LEDs for SW {sw:010b}'
                
            self.feedback += 'Passed test case %d\n' % (self.cur_test+1)
            self.cur_test += 1
            self.num_passed += 1
            if self.cur_test >= len(self.test_cases):
                cpu.halt()

        def read_sw(self):
            if self.cur_test > len(self.test_cases):
                print('Error: read_sw after should have halted?')
                return 0
            sw, _ = self.test_cases[self.cur_test]  
            return sw

    # Test cases
    tests = [(0, 0),
            (0b0000100001, 2),
            (0b0001100010, 5),
            (0b1011101110, 37),
            (0b1111111111, 62),
            (0b1111011111, 61),
            (0b0000111111, 32)]

    p1 = p1grader(tests)
    
    # Setup MMIO
    cpu.add_mmio(0xFF200000, p1.write_led)
    cpu.add_mmio(0xFF200040, p1.read_sw)

    # Run CPU
    instrs = cpu.run_until_halted(1000)

    # Check errors
    err = cpu.get_error()
    if err != '':
        print(err)
    del cpu

    if p1.num_passed == len(tests):
        print('Passed all tests')
    else:
        print('Tests missed:')
        print(p1.feedback)
        

import sys
check_p1(sys.stdin.read())

