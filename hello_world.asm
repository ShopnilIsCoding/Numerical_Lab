section .data
    hello db 'Hello, world!', 0Ah ; string to print, 0Ah is the newline character
    len equ $-hello ; length of the string

section .text
    global _start

_start:
    ; write the string to stdout
    mov eax, 4 ; system call for write
    mov ebx, 1 ; file descriptor for stdout
    mov ecx, hello ; address of the string
    mov edx, len ; number of bytes to write
    int 80h ; invoke the kernel to perform the system call

    ; exit with success
    mov eax, 1 ; system call for exit
    xor ebx, ebx ; return code of 0 for success
    int 80h ; invoke the kernel to perform the system call  
