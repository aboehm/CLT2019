# BSD 2-Clause License
# 
# Copyright (c) 2019, Alexander Böhm
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# MicroPython implementation for optimized fibonanci computation

# Fibonaci number computation with inline assembler
@micropython.asm_thumb
def fib_asm(r0):
    push({r1, r2, r3})

    cmp(r0, 3)
    blt(go_out_ret_1)

    mov(r3, r0)

    mov(r1, 1) # a 
    mov(r2, 0) # b
    mov(r0, 0) # c

    label(while_loop)

    add(r0, r1, r2)
    mov(r1, r2)
    mov(r2, r0)

    sub(r3, 1)

    cmp(r3, 0)
    beq(go_out_w_ret)
    b(while_loop)

    label(go_out_ret_1)
    pop({r1, r2, r3})
    mov(r0, 1)
    b(go_out)
    
    label(go_out_w_ret)
    pop({r1, r2, r3})

    label(go_out)

# Fibonaci number computation with python
def fib_py(r0):
    if r0 < 3:
        return 1

    r0 -= 1

    a = 1
    b = 0
    c = 0

    while True:
        c = a + b
        b = a
        a = c

        r0 -= 1

        if r0 == 0:
            return c

# Test of the implementations
for name, fib in [('native', fib_py), ('assembler', fib_asm)]: 
    for k, v in [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]:
        r = fib(k)
        print('running', name, 'fibonaci number', k, 'should be', v, 'function returned', r, 'is correct', r == v)
