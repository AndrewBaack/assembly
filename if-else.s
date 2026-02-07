.text
_start:
    
    movi     r2, 0

bge r5, r4, r5_Larger
br r4_Larger  

r5_Larger:
    bge r6, r5, r6_Larger
    mov r2, r5 
    br stop

r6_Larger:
    mov r2, r6 
    br stop

r4_Larger:
    bge r6, r4, r6_Larger 
    mov r2, r4 
    br stop

stop: break
