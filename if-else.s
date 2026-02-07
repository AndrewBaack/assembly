.text
_start:
    
    mov     r2, r4

    bgt     r5, r2, r5_is_bigger
    br      check_r6

r5_is_bigger:
    mov     r2, r5

check_r6:
    bgt     r6, r2, r6_is_bigger
    br      done

r6_is_bigger:
    mov     r2, r6

done:
