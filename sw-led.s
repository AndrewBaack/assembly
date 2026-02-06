.text
    .equ    LED_ADDR,   0xFF200000
    .equ    SW_ADDR,    0xFF200040
    .global _start
_start:
    movia   r2, LED_ADDR
    movia   r3, SW_ADDR

loop:
    andi r5, r4, 0x1F     #r5 = B
    
    srli r6, r4, 5        #shift right 5 bits
    andi r6, r6, 0x1F     #r6 = A

    add r4, r6, r5        #r4 = A + B

    stwio r4, (r2)
    br      loop

