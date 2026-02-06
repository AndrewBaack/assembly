.text
    .equ    LED_ADDR,   0xFF200000
    .equ    SW_ADDR,    0xFF200040
    .global _start
_start:
    movia   r2, LED_ADDR
    movia   r3, SW_ADDR

loop:
    ldwio   r4, 0(r3)
   

    stwio   r4, 0(r2)
    br      loop

