from CPU.InstructionSet__8BITS_LOADS import *
from CPU.InstructionSet__16BITS_LOADS import *
from CPU.InstructionSet__8BITS_ALU import *
from CPU.InstructionSet__16BITS_ARITHMETIC import *
from CPU.InstructionSet__MISCELLANEOUS import *
from CPU.InstructionsSet__ROTATA_SHIFT import *
from CPU.InstructionsSet__BIT_OPCODES import *
from CPU.InstructionsSet__JUMPS import *
from CPU.InstructionsSet__CALLS import *
from CPU.InstructionsSet__RESTARTS import *
from CPU.InstructionsSet__RETURNS import *

class CPU(
    InstructionSet__8BITS_LOADS,
    InstructionSet__16BITS_LOADS,
    InstructionSet__8BITS_ALU,
    InstructionSet__16BITS_ARITHMETIC,
    InstructionSet__MISCELLANEOUS,
    InstructionsSet__ROTATA_SHIFT,
    InstructionsSet__BIT_OPCODES,
    InstructionsSet__JUMPS,
    InstructionsSet__RESTARTS,
    InstructionsSet__RETURNS
    
):

    def __init__(self,hardware):
        self.hardware = hardware
        self.register_A = 0
        self.register_B = 0
        self.register_C = 0
        self.register_D = 0
        self.register_E = 0
        self.register_F = 0
        self.register_H = 0
        self.register_I = 0
        self.register_PC = 0
        self.register_SP = 0

    def execute_instruction(self):
        self.register_PC += 1
        instrucao = self.hardware.addressedMemory[self.register_PC]

    def __str__(self):
        return f'''
        PC:{self.register_PC}
        A: {self.register_A}
        B: {self.register_B}
        C: {self.register_C}
        D: {self.register_D}
        E: {self.register_E}
        F: {self.register_F}
        H: {self.register_H}
        I: {self.register_I}
        '''
