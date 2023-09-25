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

section   .text
global    main

extern printf

main:   
	mov eax, [len]
	xor ecx, ecx

loop:
	mov ebx, [x+eax*4]
	sub ebx, [y+eax*4]
    	add ecx, ebx
	mov [sum], ecx
    	dec eax
        test eax, eax
	jnz loop

print:
    	mov eax, [sum]
    	mov ecx, [len]
    	cdq
    	idiv ecx
    	mov [result], eax
    	pushd
    	push rdi
    	mov rdi, line
    	mov rsi, [result]
    	call printf
    	pop rdi
    	popd

end:
        mov       rax, 60
        xor       rdi, rdi
        syscall

section   .data
	line db "%d", 10, 0;
	x dd 5, 3, 2, 6, 1, 7, 4
	y dd 0, 10, 1, 9, 2, 8, 5
	sum dq 0
	len db 7
	result dq 0