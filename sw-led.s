.text
_start:
    movia   r4, 0xFF200000   # LED addr
    movia   r5, 0xFF200040   # SW addr

loop:
    ldwio   r6, 0(r5)
    
    # Your code here

    stwio   r6, 0(r4)
    br      loop

