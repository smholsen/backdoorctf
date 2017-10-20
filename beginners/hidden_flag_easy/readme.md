# hidden flag easy

## Description
n00b just learnt about binary files. He tried to hide a flag in it. Here is the file[http://hack.bckdr.in/HIDE-EASY/hide_easy].
Created by: Dhaval Kapil
No. of Correct Submissions: 1175

## Solution

Download and check the file type.
```
$ wget http://hack.bckdr.in/HIDE-EASY/hide_easy

$ file hide_easy
hide_easy: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=cf56f38a7483f0f337aa3b25644426028885c9b9, not stripped

```
Inspecting the file with IDA we can see a function called print_flag(). This sounds interesting.

Let's make the file executable and try to call it with gdb.

```
$ chmod 700 hide_easy
$ gdb hide_easy

(gdb) disas main
Dump of assembler code for function main:
   0x0804846c <+0>:	push   %ebp
   ...
End of assembler dump.
(gdb) break *0x0804846c
Breakpoint 1 at 0x804846c
(gdb) run
Starting program: ...
Breakpoint 1, 0x0804846c in main ()
(gdb) call print_flag()
939d9556640d4
$1 = 64

```

I tried entering this into the flag, but it seemed to not be correct.
Lets take a close look at the print_flag function.

```
(gdb) disas print_flag
Dump of assembler code for function print_flag:
   0x0804844c <+0>:	push   %ebp
   0x0804844d <+1>:	mov    %esp,%ebp
   0x0804844f <+3>:	sub    $0x18,%esp
   0x08048452 <+6>:	movl   $0x8048520,(%esp)
   0x08048459 <+13>:	call   0x8048320 <puts@plt>
   0x0804845e <+18>:	movl   $0x8048530,(%esp)
   0x08048465 <+25>:	call   0x8048310 <printf@plt>
   0x0804846a <+30>:	leave  
   0x0804846b <+31>:	ret    
End of assembler dump.
```

Ok, so it seems to use two movl instructions to fetch data from memory. Lets try to look at both of them.

```
(gdb) x/s 0x8048520
0x8048520:	"939d9556640d4"
(gdb) x/s 0x8048530
0x8048530:	"<flag>"
```

There we find our flag. I also noticed that the print_flag function would print the flag the second time the function was called. 
