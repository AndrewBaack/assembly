.text
_start:
    movia   r4, N
    ldw     r4, 0(r4) 
    movi    r2, 0 

    movi    r3, 1

loop:
    bgt     r3, r4, done
    add     r2, r2, r3
    addi    r3, r3, 1
    br      loop

done:
    break

.data
N:  .word 9

