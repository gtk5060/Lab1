# -*- coding: utf-8 -*-

# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b": None,
    "1d": None,
    "1e": None,
    "2b": None,
    "2c": None,
    "2d": None,
    "2e": None,
    "3b": None,
    "3c": None,
    "4a": None,
    "4bi": None,
    "4bii": None,
    "4biii": None,
    "4biv": None,
    "4bv": None,
    "4bvi": None
}
numerical = {
    "1a": None,
    "1c": None,
    "2ai32": None,
    "2aii32": None,
    "2aiii32": None,
    "2ai64": None,
    "2aii64": None,
    "2aiii64": None,
    "3ai32": None,
    "3aii32": None,
    "3aiii32": None,
    "3ai64": None,
    "3aii64": None,
    "3aiii64": None,
}

###########################################################
# Answer Section
# You may edit the values of variables below
###########################################################

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = "gtk5060"

###########################################################
# (1) Stack, heap, and system calls
###########################################################

# (1.a) What is the size of the proces stack when it is
#   waiting for user input?
#   Enter your answer in bytes.
numerical["1a"] = 135168

# (1.b) Which addresses are for the local variables and
#   which ones are for the dynamically allocated variables?
#   What are the directions in which the stack and the heap
#   grow on your system?
wordy["1b"] = "Local variables are stored on the stack (7ffc8bf65000-7ffc8bf86000) and dynamic variables are stored in the heap(01cf4000-01d15000). The stack grows down(from high to low addresses) and the heap grows up(from low to high addresses)."

# (1.c) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 135168

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = "Address limits of stack are 7ffc8bf65000-7ffc8bf86000 and address limits of heap are 01cf4000-01d15000"

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = "execve: This executes the program. brk: Allocates space in the heap for the dynamic variables. access: Checks if a file is accessible. openat: Opens the specified file, or create one if it doesnt exist. fstat: Retrieves specified information on a file. mmap: Maps to a section in the virtual address space. close: Stops referncing an open file. read: Returns the size of a file in bytes. mprotect: Changes the access permissions of the process's memory. arch_prctl: Sets the proccess's thread state. write: Outputs text to a user.  "

###########################################################
# (2) Debugging Refresher
###########################################################

# (2.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables

# (2.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["2ai32"] = 2148352

# (2.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["2aii32"] = 9633792

# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = 1925120

# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["2ai64"] = 2223104

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = 11845632

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = 4116480

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = "allocate(count - 1);"

# (2.c) Explain the cause of this error.
wordy["2c"] = "The error is caused by the count variable for one of the recusion calls being allocated out of the stack, so it cant be accessed. The memory address for this version of count is 0x7fffff7fb0ac but the stack's lower limit is 0x7fffff91f000."

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = "Each stack frame is 1200064 bytes, my stack limit is 8388608, so 6 invocations should be possible. There were 6 invoations before the segfault when prog2 runs."

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = "Each invocation is 1200064 bytes, and contain: the starting location of the frame on the stack, the instruction pointer, which frame its being called by and the frame it calls, the source language, the arguments list location and the arguments used in the function, the location of the local variable list on the stack, the stack pointer of the previous frame, and the location of the instruction and base pointer on the stack."

###########################################################
# (3) More debugging
###########################################################

# (3.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables:

# (3.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["3ai32"] = 2409472

# (3.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["3aii32"] = 447655936

# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = 2768896

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = 2549760

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] = 452833280

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] = 7909376

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = "Line 19, the memset operation caused the error. In the last iteration, malloc allocated outside of the heap, heap range was 0x555555756000-0x555555777000 but the variable was allocated to 0x7fffdced6010. The memset operation tired to write to an invalid location which caused the segmentation fault."

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = "The error in prog2 was caused by a stack overflow while the error in prog3 was caused by a heap overflow."

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = None

# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = None

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = None

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = None

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = None

# (4.b.v) voluntary context switches
wordy["4bv"] = None

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = None

###########################################################
# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
###########################################################
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error of answer %s (should be a string)" % key)
