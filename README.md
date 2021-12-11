# CSE598-Project1
This gdb plugin provides some extra shortcut commands to make it more convenient when solving CTF challenges or whatever your program is.
Before running the script, make sure you have GEF - GDB Enhanced Features installed. 

First, if you feel like typing *set $zf = 0* to bypass the conditional jump is a little annoying when you have to do it a lot of times,
then you probably need the following commands to make your life easier:
***cf
pf
af
zf
sf
of***

The commands above will toggle the value of corresponding flags register and print out their current value:
*Carry flag,
Parity flag,
Auxiliary Carry flag,
Zero flag,
Sign flag,
Overflow flag*

Alternatively, you can use command:
***tz***
to set register *RAX* to 0 whenever there is a *TEST RAX, RAX* or *CMP RAX, RAX* before conditional jump or anytime you want.

Second, in order to solve the problem of unable to use process record function in gdb under virtual machine environment, the script will perform auto logging when you start running the inferior, and every time you *create/modified/delete a breakpoint/watchpoint or modified a register/memory*, the related specific details will be printed on the screen and so be logged. The log file will be created seperated every time you run the gdb and will not be overwritten automatically.

Finally, the script will auto detect if there is a ***ptrace*** function in the target file. If there is, a temporary breakpoint will be set up for you.
