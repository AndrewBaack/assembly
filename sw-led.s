    .text
    .equ LEDs, 0xFF200000
    .equ SWITCHES, 0xFF200040
    .global _start
    
_start:
    movia r2, LEDs         # Address of LEDs
    movia r3, SWITCHES     # Address of switches

loop:
    ldwio r4, 0(r3)        # Read the state of switches

    andi r5, r4, 0x1F
    srli r6, r4, 5
    andi r6, r6, 0x1F

    add r4, r6, r5

    stwio r4, 0(r2)        # Display the state on LEDs

    br loop       
