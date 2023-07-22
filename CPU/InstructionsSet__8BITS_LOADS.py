'''
8 - BITS LOADS                                                 
        As instruções contidas neste bloco servem para realizar    
    operações relacionadas com o transporte de dados de 8 bits.  
'''

class InstructionsSet__8BITS_LOADS:

    '''
    1. LD nn,n
        Description:
            Put value nn into n.
        Use with:    
            nn = B,C,D,E,H,L,BC,DE,HL,SP
            n = 8 bit immediate value
    '''
    def instruction_0x06(self):  # LD B,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_B = n

    def instruction_0x0E(self):  # LD C,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_C = n

    def instruction_0x16(self):  # LD D,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_D = n

    def instruction_0x1E(self):  # LD E,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_E = n

    def instruction_0x26(self):  # LD H,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_H = n

    def instruction_0x2E(self):  # LD L,n
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_I = n


    '''
    2. LD r1,r2
        Description:
            Put value r2 into r1.
        Use with:    
            r1,r2 = A,B,C,D,E,H,L,(HL)
    '''
    def instruction_0x7F(self):  # LD A, A
        pass

    def instruction_0x78(self):  # LD A, B
        self.register_A = self.register_B

    def instruction_0x79(self):  # LD A, C
        self.register_A = self.register_C

    def instruction_0x7A(self):  # LD A, D
        self.register_A = self.register_D

    def instruction_0x7B(self):  # LD A, E
        self.register_A = self.register_E

    def instruction_0x7C(self):  # LD A, H
        self.register_A = self.register_H

    def instruction_0x7D(self):  # LD A, L
        self.register_A = self.register_L

    def instruction_0x7E(self):  # LD A, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_A = self.hardware.addressedMemory[address]

    def instruction_0x40(self):  # LD B, B
        pass

    def instruction_0x41(self):  # LD B, C
        self.register_B = self.register_C

    def instruction_0x42(self):  # LD B, D
        self.register_B = self.register_D

    def instruction_0x43(self):  # LD B, E
        self.register_B = self.register_E

    def instruction_0x44(self):  # LD B, H
        self.register_B = self.register_H

    def instruction_0x45(self):  # LD B, L
        self.register_B = self.register_L

    def instruction_0x46(self):  # LD B, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_B = self.hardware.addressedMemory[address]

    def instruction_0x48(self):  # LD C, B
        self.register_C = self.register_B

    def instruction_0x49(self):  # LD C, C
        pass

    def instruction_0x4A(self):  # LD C, D
        self.register_C = self.register_D

    def instruction_0x4B(self):  # LD C, E
        self.register_C = self.register_E

    def instruction_0x4C(self):  # LD C, H
        self.register_C = self.register_H

    def instruction_0x4D(self):  # LD C, L
        self.register_C = self.register_L

    def instruction_0x4E(self):  # LD C, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_C = self.hardware.addressedMemory[address]

    def instruction_0x50(self):  # LD D, B
        self.register_D = self.register_B

    def instruction_0x51(self):  # LD D, C
        self.register_D = self.register_C

    def instruction_0x52(self):  # LD D, D
        pass

    def instruction_0x53(self):  # LD D, E
        self.register_D = self.register_E

    def instruction_0x54(self):  # LD D, H
        self.register_D = self.register_H

    def instruction_0x55(self):  # LD D, L
        self.register_D = self.register_L

    def instruction_0x56(self):  # LD D, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_D = self.hardware.addressedMemory[address]

    def instruction_0x58(self):  # LD E, B
        self.register_E = self.register_B

    def instruction_0x59(self):  # LD E, C
        self.register_E = self.register_C

    def instruction_0x5A(self):  # LD E, D
        self.register_E = self.register_D

    def instruction_0x5B(self):  # LD E, E
        pass

    def instruction_0x5C(self):  # LD E, H
        self.register_E = self.register_H

    def instruction_0x5D(self):  # LD E, L
        self.register_E = self.register_L

    def instruction_0x5E(self):  # LD E, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_E = self.hardware.addressedMemory[address]

    def instruction_0x60(self):  # LD H, B
        self.register_H = self.register_B

    def instruction_0x61(self):  # LD H, C
        self.register_H = self.register_C

    def instruction_0x62(self):  # LD H, D
        self.register_H = self.register_D

    def instruction_0x63(self):  # LD H, E
        self.register_H = self.register_E

    def instruction_0x64(self):  # LD H, H
        pass

    def instruction_0x65(self):  # LD H, L
        self.register_H = self.register_L

    def instruction_0x66(self):  # LD H, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_H = self.hardware.addressedMemory[address]

    def instruction_0x68(self):  # LD L, B
        self.register_L = self.register_B

    def instruction_0x69(self):  # LD L, C
        self.register_L = self.register_C

    def instruction_0x6A(self):  # LD L, D
        self.register_L = self.register_D

    def instruction_0x6B(self):  # LD L, E
        self.register_L = self.register_E

    def instruction_0x6C(self):  # LD L, H
        self.register_L = self.register_H

    def instruction_0x6D(self):  # LD L, L
        pass

    def instruction_0x6E(self):  # LD L, (HL)
        address = self.register_H << 8 | self.register_L
        self.register_L = self.hardware.addressedMemory[address]

    def instruction_0x70(self):  # LD (HL), B
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_B

    def instruction_0x71(self):  # LD (HL), C
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_C

    def instruction_0x72(self):  # LD (HL), D
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_D

    def instruction_0x73(self):  # LD (HL), E
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_E

    def instruction_0x74(self):  # LD (HL), H
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_H

    def instruction_0x75(self):  # LD (HL), L
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = self.register_L

    def instruction_0x36(self):  # LD (HL), n

        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        address = self.register_H << 8 | self.register_L
        self.hardware.addressedMemory[address] = n

    
    '''
    3. LD A,n
        Description:
            Put value n into A.
        Use with:    
            n = A,B,C,D,E,H,L,(BC),(DE),(HL),(nn),#
            nn = two byte immediate value. (LS byte first.
    '''
    def instruction_0x7F(self):  # LD A, A
        pass

    def instruction_0x78(self):  # LD A, B
        self.register_A = self.register_B

    def instruction_0x79(self):  # LD A, C
        self.register_A = self.register_C

    def instruction_0x7A(self):  # LD A, D
        self.register_A = self.register_D

    def instruction_0x7B(self):  # LD A, E
        self.register_A = self.register_E

    def instruction_0x7C(self):  # LD A, H
        self.register_A = self.register_H

    def instruction_0x7D(self):  # LD A, L
        self.register_A = self.register_L

    def instruction_0x0A(self):  # LD A, (BC)
        address = (self.register_B << 8) | self.register_C
        self.register_A = self.hardware.addressedMemory[address]

    def instruction_0x1A(self):  # LD A, (DE)
        address = (self.register_D << 8) | self.register_E
        self.register_A = self.hardware.addressedMemory[address]

    def instruction_0x7E(self):  # LD A, (HL)
        address = (self.register_H << 8) | self.register_L
        self.register_A = self.hardware.addressedMemory[address]

    def instruction_0xFA(self):  # LD A, (nn)
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        address = (ms_byte << 8) | ls_byte
        self.register_A = self.hardware.addressedMemory[address]

    def instruction_0x3E(self):  # LD A, #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.register_A = n


    
    '''
    4. LD n,A
        Description:
            Put value A into n.
        Use with:    
            n = A,B,C,D,E,H,L,(BC),(DE),(HL),(nn)
            nn = two byte immediate value. (LS byte first.
    '''
    def instruction_0x7F(self):  # LD A, A
        pass

    def instruction_0x47(self):  # LD B, A
        self.register_B = self.register_A

    def instruction_0x4F(self):  # LD C, A
        self.register_C = self.register_A

    def instruction_0x57(self):  # LD D, A
        self.register_D = self.register_A

    def instruction_0x5F(self):  # LD E, A
        self.register_E = self.register_A

    def instruction_0x67(self):  # LD H, A
        self.register_H = self.register_A

    def instruction_0x6F(self):  # LD L, A
        self.register_L = self.register_A

    def instruction_0x02(self):  # LD (BC), A
        address = (self.register_B << 8) | self.register_C
        self.hardware.addressedMemory[address] = self.register_A

    def instruction_0x12(self):  # LD (DE), A
        address = (self.register_D << 8) | self.register_E
        self.hardware.addressedMemory[address] = self.register_A

    def instruction_0x77(self):  # LD (HL), A
        address = (self.register_H << 8) | self.register_L
        self.hardware.addressedMemory[address] = self.register_A

    def instruction_0xEA(self):  # LD (nn), A
        self.register_PC += 1
        ls_byte = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        ms_byte = self.hardware.addressedMemory[self.register_PC]
        address = (ms_byte << 8) | ls_byte
        self.hardware.addressedMemory[address] = self.register_A


    '''
    5. LD A,(C)
        Description:
            Put value at address $FF00 + register C into A.
        Same as: LD A,($FF00+C)
    '''
    def instruction_0xF2(self):  # LD A, (C)
        address = 0xFF00 + self.register_C
        self.register_A = self.hardware.addressedMemory[address]


    '''
    6. LD (C),A
        Description:
            Put A into address $FF00 + register C
    '''
    def instruction_0xE2(self):  # LD (C), A
        address = 0xFF00 + self.register_C


    '''
    7. LD A,(HLD)
        Description: Same as: LDD A,(HL)
    
    8. LD A,(HL-)
        Description: Same as: LDD A,(HL)
    '''


    '''
    9. LDD A,(HL)
        Description:
            Put value at address HL into A. Decrement HL.
        Same as: LD A,(HL) - DEC HL
    '''
    def instruction_0x3A(self):  # LDD A, (HL)
        address = (self.register_H << 8) | self.register_L
        self.register_A = self.hardware.addressedMemory[address]
        address -= 1
        self.register_H = (address >> 8) & 0xFF
        self.register_L = address & 0xFF


    '''
    10. LD (HLD),A
        Description: Same as: LDD (HL),A
    11. LD (HL-),A
        Description: Same as: LDD (HL),A
    '''

    '''
    12. LDD (HL),A
        Description:
            Put A into memory address HL. Decrement HL.
        Same as: LD (HL),A - DEC HL
    '''
    def instruction_0x32(self):  # LDD (HL), A
        address = (self.register_H << 8) | self.register_L
        self.hardware.addressedMemory[address] = self.register_A
        address -= 1
        self.register_H = (address >> 8) & 0xFF
        self.register_L = address & 0xFF


    '''
    13. LD A,(HLI)
    Description: Same as: LDI A,(HL)
    14. LD A,(HL+)
    Description: Same as: LDI A,(HL)
    '''


    '''
    15. LDI A,(HL)
        Description:
            Put value at address HL into A. Increment HL.
        Same as: LD A,(HL) - INC HL
    '''
    def instruction_0x2A(self):  # LDI A, (HL)
        address = (self.register_H << 8) | self.register_L
        self.register_A = self.hardware.addressedMemory[address]
        address += 1
        self.register_H = (address >> 8) & 0xFF
        self.register_L = address & 0xFF


    '''
    16. LD (HLI),A
    Description: Same as: LDI (HL),A
    17. LD (HL+),A
    Description: Same as: LDI (HL),A
    '''


    '''
    18. LDI (HL),A
        Description:
            Put A into memory address HL. Increment HL.
        Same as: LD (HL),A - INC HL
    '''
    def instruction_0x22(self):  # LDI (HL), A
        address = (self.register_H << 8) | self.register_L
        self.hardware.addressedMemory[address] = self.register_A
        address += 1
        self.register_H = (address >> 8) & 0xFF
        self.register_L = address & 0xFF


    '''
    19. LDH (n),A
        Description:
            Put A into memory address $FF00+n.
        Use with:    
            n = one byte immediate value.
    '''
    def instruction_0xE0(self):  # LDH (n), A
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        address = 0xFF00 + n
        self.hardware.addressedMemory[address] = self.register_A


    '''
    20. LDH A,(n)
        Description:
            Put memory address $FF00+n into A.
        Use with:    
            n = one byte immediate value.
    '''
    def instruction_0xF0(self):  # LDH A, (n)
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        address = 0xFF00 + n
        self.register_A = self.hardware.addressedMemory[address]

