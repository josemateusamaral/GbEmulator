'''
16 - BITS LOADS                                                 
        As instruções contidas neste bloco servem para realizar    
    operações relacionadas com o transporte de dados de 16 bits.  
'''

class InstructionSet__16BITS_LOADS:
    

    '''
    1. LD n,nn
        Description:
            Put value nn into n.
        Use with:    
            n = BC,DE,HL,SP
            nn = 16 bit immediate value
    '''
    def instruction_0x01(self):  # LD BC, nn
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_B = ms_byte
        self.register_C = ls_byte

    def instruction_0x11(self):  # LD DE, nn
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_D = ms_byte
        self.register_E = ls_byte

    def instruction_0x21(self):  # LD HL, nn
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_H = ms_byte
        self.register_L = ls_byte

    def instruction_0x31(self):  # LD SP, nn
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_SP = (ms_byte << 8) | ls_byte


    '''
    2. LD SP,HL
        Description:
            Put HL into Stack Pointer (SP).
    '''
    def instruction_0xF9(self):  # LD SP, HL
        self.register_SP = (self.register_H << 8) | self.register_L


    '''
    3. LD HL,SP+n 
        Description: Same as: LDHL SP,n
    '''


    '''
    4. LDHL SP,n
        Description:
            Put SP + n effective address into HL.
        Use with:    
            n = one byte signed immediate value.
        Flags affected:
            Z - Reset.
            N - Reset.
            H - Set or reset according to operation.
            C - Set or reset according to operation.
    '''
    def instruction_0xF8(self):  # LDHL SP, n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]

        # If the signed value of n is negative, convert it to a positive 16-bit value
        if n & 0x80:  # Check if the 7th bit is set (indicating a negative number)
            n = -(0x100 - n)  # Convert to positive value in 16-bit signed representation

        result = self.register_SP + n

        # Check if the low byte of SP + n overflows (0xFF) or underflows (0x00)
        self.set_flag('H', (self.register_SP & 0x0F) + (n & 0x0F) > 0x0F)

        # Check if the 16-bit result overflows (0xFFFF) or underflows (0x0000)
        self.set_flag('C', result > 0xFFFF or result < 0x0000)

        # Reset Z and N flags
        self.set_flag('Z', False)
        self.set_flag('N', False)

        self.register_H = (result >> 8) & 0xFF
        self.register_L = result & 0xFF


    '''
    5. LD (nn),SP
        Description:
            Put Stack Pointer (SP) at address n.
        Use with:    
            nn = two byte immediate address.
    '''
    def instruction_0x08(self):  # LD (nn), SP
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        address = (ms_byte << 8) | ls_byte
        self.hardware.addressedMemory[address] = self.register_SP & 0xFF
        address += 1
        self.hardware.addressedMemory[address] = (self.register_SP >> 8) & 0xFF


    '''
    6. PUSH nn
        Description:
            Push register pair nn onto stack.
            Decrement Stack Pointer (SP) twice.
        Use with:    
            nn = AF,BC,DE,HL
    '''
    def instruction_0xF5(self):  # PUSH AF
        self.push_stack(self.register_A, self.register_F)

    def instruction_0xC5(self):  # PUSH BC
        self.push_stack(self.register_B, self.register_C)

    def instruction_0xD5(self):  # PUSH DE
        self.push_stack(self.register_D, self.register_E)

    def instruction_0xE5(self):  # PUSH HL
        self.push_stack(self.register_H, self.register_L)

    def push_stack(self, ms_byte, ls_byte):
        self.register_SP -= 1
        self.hardware.addressedMemory[self.register_SP] = ms_byte
        self.register_SP -= 1
        self.hardware.addressedMemory[self.register_SP] = ls_byte


    '''
    7. POP nn
        Description:
            Pop two bytes off stack into register pair nn. 
            Increment Stack Pointer (SP) twice.
        Use with:    
            nn = AF,BC,DE,HL
    '''
    def instruction_0xF1(self):  # POP AF
        self.register_F = self.pop_stack()
        self.register_A = self.pop_stack()

    def instruction_0xC1(self):  # POP BC
        self.register_C = self.pop_stack()
        self.register_B = self.pop_stack()

    def instruction_0xD1(self):  # POP DE
        self.register_E = self.pop_stack()
        self.register_D = self.pop_stack()

    def instruction_0xE1(self):  # POP HL
        self.register_L = self.pop_stack()
        self.register_H = self.pop_stack()

    def pop_stack(self):
        ls_byte = self.hardware.addressedMemory[self.register_SP]
        self.register_SP += 1
        ms_byte = self.hardware.addressedMemory[self.register_SP]
        self.register_SP += 1
        return (ms_byte << 8) | ls_byte