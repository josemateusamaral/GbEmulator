from CPU.InstructionsSet__8BITS_LOADS import *
from CPU.InstructionsSet__16BITS_LOADS import *
from CPU.InstructionsSet__8BITS_ALU import *
from CPU.InstructionsSet__16BITS_ARITHMETIC import *
from CPU.InstructionsSet__MISCELLANEOUS import *
from CPU.InstructionsSet__ROTATA_SHIFT import *
from CPU.InstructionsSet__BIT_OPCODES import *
from CPU.InstructionsSet__JUMPS import *
from CPU.InstructionsSet__CALLS import *
from CPU.InstructionsSet__RESTARTS import *
from CPU.InstructionsSet__RETURNS import *

class CPU(
    InstructionsSet__8BITS_LOADS,
    InstructionsSet__16BITS_LOADS,
    InstructionsSet__8BITS_ALU,
    InstructionsSet__16BITS_ARITHMETIC,
    InstructionsSet__MISCELLANEOUS,
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
        
        #flags
        self.register_F = 0
        self.flag_Z = False
        self.flag_N = False
        self.flag_H = False
        self.flag_C = False

        self.register_H = 0
        self.register_I = 0

        self.register_PC = 0
        self.register_SP = 0


    def register_BC(self):
        return ((self.register_B << 8) | self.register_C)
    def register_DE(self):
        return ((self.register_D << 8) | self.register_E)
    def register_HL(self):
        return ((self.register_H << 8) | self.register_L)
        


    def set_flag(self,flag,value):
        if flag == 'Z':
            self.flag_Z = value
        elif flag == 'N':
            self.flag_N = value
        elif flag == 'H':
            self.flag_H = value
        elif flag == 'C':
            self.flag_C = bool(value)

        registerF_Bits = f'{int(self.flag_Z)}{int(self.flag_N)}{int(self.flag_H)}{int(self.flag_C)}0000'
        self.register_F = int(registerF_Bits,2)

    def get_flag(self,flag):
        if flag == 'Z':
            return self.flag_Z
        elif flag == 'N':
            return self.flag_N
        elif flag == 'H':
            return self.flag_H
        elif flag == 'C':
            return self.flag_C

    def cicle(self):

        #pegar instrucao e identificar sua copia
        instrucao = self.hardware.addressedMemory[self.register_PC]
        opcode = str(hex(instrucao))[2:].replace(' ','').upper()
        if len(opcode) == 1:
            opcode = '0' + opcode
        funcao_instrucao = 'instruction_0x' + opcode

        if funcao_instrucao != 'instruction_0x0':
            #verificar se a instrucao identificada ja foi implentada
            
            #verificar se a instrucao é uma instrução CB
            if funcao_instrucao == 'instruction_0xCB':
                self.register_PC += 1
                instrucao = self.hardware.addressedMemory[self.register_PC]
                funcao_instrucao += str(hex(instrucao))[2:].replace(' ','').upper()

            if hasattr(self,funcao_instrucao):
                
                eval('self.' + funcao_instrucao + '()')
                print(funcao_instrucao + ' executada')  

                '''
                try:
                    eval('self.' + funcao_instrucao + '()')
                    print(funcao_instrucao + ' executada')
                except:
                    print('ERRO GRAVE NA INSTRUCAO --> ' + funcao_instrucao)
                '''


            else:
                print(f"A instrucao {funcao_instrucao}() ainda não foi implementada")

        self.register_PC += 1
        return

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
