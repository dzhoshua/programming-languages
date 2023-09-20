%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro

%macro print 2
    pushd
    mov rax, 1
    mov rdi, 1
    mov rdx, %1
    mov rsi, %2
    syscall
    popd
%endmacro


section   .text
global    _start

_start:   
	    fild dword [number]	
	    fsqrt
	    fistp dword [result]
        mov rcx, 10
        mov rbx, 0 
        mov rax, [result]

divide:
        xor rdx, rdx
        div rcx
        push rdx
        inc rbx 
        test rax, rax
        jnz divide

        ;mov rax, rbx 
        ;add rax, '0'
        ;mov [result], rax
        ;print 1, result

display:
        pop rax
        add rax, '0'
        mov [result], rax
        print 1, result
        dec rbx
        cmp rbx, 0
        jg display

        print len, line

        mov       rax, 60
        xor       rdi, rdi
        syscall

section   .data
    number dd 121
    line db 0xA, 0xD
    len equ $ - line
    result db 0