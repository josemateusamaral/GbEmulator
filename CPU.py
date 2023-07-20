class CPU:

    register_A = 0
    register_B = 0
    register_C = 0
    register_D = 0
    register_E = 0
    register_F = 0
    register_H = 0
    register_I = 0
    register_PC = 0
    register_SP = 0

    def execute_instruction(self,instruction):
        pass




    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    X                                                                 X
    X  8 - BITS LOADS                                                 X
    X      As instruções contidas neste bloco servem para realizar    X
    X  operações relacionadas com o transporte de dados de 8 bits.    X     
    X                                                                 X
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    '''
    1. LD nn,n
        Description:
            Put value nn into n.
        Use with:    
            nn = B,C,D,E,H,L,BC,DE,HL,SP
            n = 8 bit immediate value
    '''
    def instruction_LD8_1(self,data):
        print('running instruction_LD8_1')

    '''
    2. LD r1,r2
        Description:
            Put value r2 into r1
        Use with:    
            r1,r2 = A,B,C,D,E,H,L,(HL)
    '''
    def instruction_LD8_2(self,data):
        print('running instruction_LD8_2')

    '''
    3. LD A,n
        Description:
            Put value n into A.
        Use with:    
            n = A,B,C,D,E,H,L,(BC),(DE),(HL),(nn),#
            nn = two byte immediate value. (LS byte first.
    '''
    def instruction_LD8_3(self,data):
        print('running instruction_LD8_3')
    
    '''
    4. LD n,A
        Description:
            Put value A into n
        Use with:    
            n = A,B,C,D,E,H,L,(BC),(DE),(HL),(nn)
            nn = two byte immediate value. (LS byte first.
    '''
    def instruction_LD8_4(self,data):
        print('running instruction_LD8_4')

    '''
    5. LD A,(C)
        Description:
            Put value at address $FF00 + register C into A.
            Same as: LD A,($FF00+C)
    '''
    def instruction_LD8_5(self,data):
        print('running instruction_LD8_5')
    
    '''
    6. LD (C),A
        Description:
            Put A into address $FF00 + register C.
    '''
    def instruction_LD8_6(self,data):
        print('running instruction_LD8_6')
    
    '''
    7. LD A,(HLD)
        Description:
            Same as: LDD A,(HL)
    '''
    def instruction_LD8_7(self,data):
        print('running instruction_LD8_7')
    
    '''
    8. LD A,(HL-)
        Description:
            Same as: LDD A,(HL)
    '''
    def instruction_LD8_8(self,data):
        print('running instruction_LD8_8')

    '''
    9. LDD A,(HL)
        Description:
            Put value at address HL into A. Decrement HL.
            Same as: LD A,(HL) - DEC HL
    '''
    def instruction_LD8_9(self,data):
        print('running instruction_LD8_9')
    
    '''
    10. LD (HLD),A
        Description:
            Same as: LDD (HL),A
    '''
    def instruction_LD8_10(self,data):
        print('running instruction_LD8_10')

    '''
    11. LD (HL-),A
        Description:
            Same as: LDD (HL),A
    '''
    def instruction_LD8_11(self,data):
        print('running instruction_LD8_11')
    
    '''
    12. LDD (HL),A
        Description:
            Put A into memory address HL. Decrement HL.
            Same as: LD (HL),A - DEC HL
    '''
    def instruction_LD8_12(self,data):
        print('running instruction_LD8_12')

    '''
    13. LD A,(HLI)
        Description:
            Same as: LDI A,(HL)
    '''
    def instruction_LD8_3(self,data):
        print('running instruction_LD8_3')
    
    '''
    14. LD A,(HL+)
        Description:
            Same as: LDI A,(HL)
    '''
    def instruction_LD8_14(self,data):
        print('running instruction_LD8_14')

    '''
    15. LDI A,(HL)
        Description:
            Put value at address HL into A. Increment HL.
            Same as: LD A,(HL) - INC HL
    '''
    def instruction_LD8_15(self,data):
        print('running instruction_LD8_15')

    '''
    16. LD (HLI),A
        Description:
            Same as: LDI (HL),A
    '''
    def instruction_LD8_16(self,data):
        print('running instruction_LD8_16')

    '''
    17. LD (HL+),A
        Description:
            Same as: LDI (HL),A
    '''
    def instruction_LD8_17(self,data):
        print('running instruction_LD8_17')

    '''
    18. LDI (HL),A
        Description:
            Put A into memory address HL. Increment HL.
            Same as: LD (HL),A - INC HL
    '''
    def instruction_LD8_18(self,data):
        print('running instruction_LD8_18')

    '''
    19. LDH (n),A
        Description:
            Put A into memory address $FF00+n.
        Use with:    
            n = one byte immediate value
    '''
    def instruction_LD8_19(self,data):
        print('running instruction_LD8_19')

    '''
    20. LDH A,(n)
        Description:
            ut memory address $FF00+n into A.
        Use with:    
            n = one byte immediate value.
    '''
    def instruction_LD8_20(self,data):
        print('running instruction_LD8_20')







    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    X                                                                 X
    X  16 - BITS LOADS                                                X
    X      As instruções contidas neste bloco servem para realizar    X
    X  operações relacionadas com o transporte de dados de 16 bits.   X     
    X                                                                 X
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    '''
    1. LD n,nn
        Description:
            Put value nn into n
        Use with:    
            n = BC,DE,HL,SP
            nn = 16 bit immediate value
    '''
    def instruction_LD16_1(self,data):
        print('running instruction_LD16_1')

    '''
    2. LD SP,HL
        Description:
            Put HL into Stack Pointer (SP)
    '''
    def instruction_LD16_2(self,data):
        print('running instruction_LD16_2')

    '''
    3. LD HL,SP+n
        Description:
            Same as: LDHL SP,n
    '''
    def instruction_LD16_3(self,data):
        print('running instruction_LD16_3')

    '''
    4. LDHL SP,n
        Description:
           Put SP + n effective address into HL
        Use with:    
            n = one byte signed immediate value.
        Flags affected:
            Z - Reset.
            N - Reset.
            H - Set or reset according to operation.
            C - Set or reset according to operation
    '''
    def instruction_LD16_4(self,data):
        print('running instruction_LD16_4')

    '''
    5. LD (nn),SP
        Description:
            Put Stack Pointer (SP) at address 
        Use with:    
            nn = two byte immediate address
    '''
    def instruction_LD16_1(self,data):
        print('running instruction_LD16_1')

    '''
    6. PUSH nn
        Description:
            Push register pair nn onto stack.
            Decrement Stack Pointer (SP) twice.
        Use with:    
            n = AF,BC,DE,HL
    '''
    def instruction_LD16_6(self,data):
        print('running instruction_LD16_6')

    '''
    7. POP nn
        Description:
            Pop two bytes off stack into register pair nn. 
            Increment Stack Pointer (SP) twice.
        Use with:    
            n = AF,BC,DE,HL
    '''
    def instruction_LD16_7(self,data):
        print('running instruction_LD16_7')