class InstructionSet__8BITS_ALU:

'''
    1. ADD A,n
        Description:
            Add n to A.
        Use with:    
            n = A,B,C,D,E,H,L,(HL),#
        Flags affected:
            Z - Set if result is zero.
            N - Reset.
            H - Set if carry from bit 3.
            C - Set if carry from bit 7
'''
    def instruction_0x87(self):  # ADD A, A
        self.add_to_A(self.register_A)

    def instruction_0x80(self):  # ADD A, B
        self.add_to_A(self.register_B)

    def instruction_0x81(self):  # ADD A, C
        self.add_to_A(self.register_C)

    def instruction_0x82(self):  # ADD A, D
        self.add_to_A(self.register_D)

    def instruction_0x83(self):  # ADD A, E
        self.add_to_A(self.register_E)

    def instruction_0x84(self):  # ADD A, H
        self.add_to_A(self.register_H)

    def instruction_0x85(self):  # ADD A, L
        self.add_to_A(self.register_L)

    def instruction_0x86(self):  # ADD A, (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.add_to_A(value)

    def instruction_0xC6(self):  # ADD A, #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.add_to_A(n)

    def add_to_A(self, value):
        carry = 1 if self.get_flag('C') else 0
        result = self.register_A + value + carry

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Set H flag if carry from bit 3
        self.set_flag('H', (self.register_A & 0x0F) + (value & 0x0F) + carry > 0x0F)

        # Set C flag if carry from bit 7
        self.set_flag('C', result > 0xFF)

        self.register_A = result & 0xFF



    #2
    def instruction_0x88(self):  # ADC A, A
        self.add_with_carry_to_A(self.register_A)

    def instruction_0x89(self):  # ADC A, B
        self.add_with_carry_to_A(self.register_B)

    def instruction_0x8A(self):  # ADC A, C
        self.add_with_carry_to_A(self.register_C)

    def instruction_0x8B(self):  # ADC A, D
        self.add_with_carry_to_A(self.register_D)

    def instruction_0x8C(self):  # ADC A, E
        self.add_with_carry_to_A(self.register_E)

    def instruction_0x8D(self):  # ADC A, H
        self.add_with_carry_to_A(self.register_H)

    def instruction_0x8E(self):  # ADC A, L
        self.add_with_carry_to_A(self.register_L)

    def instruction_0x8F(self):  # ADC A, (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.add_with_carry_to_A(value)

    def instruction_0xCE(self):  # ADC A, #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.add_with_carry_to_A(n)

    def add_with_carry_to_A(self, value):
        carry = 1 if self.get_flag('C') else 0
        result = self.register_A + value + carry

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Set H flag if carry from bit 3
        self.set_flag('H', (self.register_A & 0x0F) + (value & 0x0F) + carry > 0x0F)

        # Set C flag if carry from bit 7
        self.set_flag('C', result > 0xFF)

        self.register_A = result & 0xFF



    #3
    def instruction_0x97(self):  # SUB A, A
        self.subtract_from_A(self.register_A)

    def instruction_0x90(self):  # SUB A, B
        self.subtract_from_A(self.register_B)

    def instruction_0x91(self):  # SUB A, C
        self.subtract_from_A(self.register_C)

    def instruction_0x92(self):  # SUB A, D
        self.subtract_from_A(self.register_D)

    def instruction_0x93(self):  # SUB A, E
        self.subtract_from_A(self.register_E)

    def instruction_0x94(self):  # SUB A, H
        self.subtract_from_A(self.register_H)

    def instruction_0x95(self):  # SUB A, L
        self.subtract_from_A(self.register_L)

    def instruction_0x96(self):  # SUB A, (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.subtract_from_A(value)

    def instruction_0xD6(self):  # SUB A, #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.subtract_from_A(n)

    def subtract_from_A(self, value):
        result = self.register_A - value

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Set N flag
        self.set_flag('N', True)

        # Set H flag if no borrow from bit 4
        self.set_flag('H', (self.register_A & 0x0F) < (value & 0x0F))

        # Set C flag if no borrow
        self.set_flag('C', result < 0)

        self.register_A = result & 0xFF



    #4
    def instruction_0x9F(self):  # SBC A, A
        self.subtract_with_carry_from_A(self.register_A)

    def instruction_0x98(self):  # SBC A, B
        self.subtract_with_carry_from_A(self.register_B)

    def instruction_0x99(self):  # SBC A, C
        self.subtract_with_carry_from_A(self.register_C)

    def instruction_0x9A(self):  # SBC A, D
        self.subtract_with_carry_from_A(self.register_D)

    def instruction_0x9B(self):  # SBC A, E
        self.subtract_with_carry_from_A(self.register_E)

    def instruction_0x9C(self):  # SBC A, H
        self.subtract_with_carry_from_A(self.register_H)

    def instruction_0x9D(self):  # SBC A, L
        self.subtract_with_carry_from_A(self.register_L)

    def instruction_0x9E(self):  # SBC A, (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.subtract_with_carry_from_A(value)

    def instruction_0xDE(self):  # SBC A, #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.subtract_with_carry_from_A(n)

    def subtract_with_carry_from_A(self, value):
        carry = 1 if self.get_flag('C') else 0
        result = self.register_A - value - carry

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Set N flag
        self.set_flag('N', True)

        # Set H flag if no borrow from bit 4
        self.set_flag('H', (self.register_A & 0x0F) < ((value + carry) & 0x0F))

        # Set C flag if no borrow
        self.set_flag('C', result < 0)

        self.register_A = result & 0xFF




    #5
    def instruction_0xA7(self):  # AND A
        self.logical_and_with_A(self.register_A)

    def instruction_0xA0(self):  # AND B
        self.logical_and_with_A(self.register_B)

    def instruction_0xA1(self):  # AND C
        self.logical_and_with_A(self.register_C)

    def instruction_0xA2(self):  # AND D
        self.logical_and_with_A(self.register_D)

    def instruction_0xA3(self):  # AND E
        self.logical_and_with_A(self.register_E)

    def instruction_0xA4(self):  # AND H
        self.logical_and_with_A(self.register_H)

    def instruction_0xA5(self):  # AND L
        self.logical_and_with_A(self.register_L)

    def instruction_0xA6(self):  # AND (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.logical_and_with_A(value)

    def instruction_0xE6(self):  # AND #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.logical_and_with_A(n)

    def logical_and_with_A(self, value):
        self.register_A &= value

        # Set Z flag if result is zero
        self.set_flag('Z', self.register_A == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Set H flag
        self.set_flag('H', True)

        # Reset C flag
        self.set_flag('C', False)



    #6
    def instruction_0xB7(self):  # OR A
        self.logical_or_with_A(self.register_A)

    def instruction_0xB0(self):  # OR B
        self.logical_or_with_A(self.register_B)

    def instruction_0xB1(self):  # OR C
        self.logical_or_with_A(self.register_C)

    def instruction_0xB2(self):  # OR D
        self.logical_or_with_A(self.register_D)

    def instruction_0xB3(self):  # OR E
        self.logical_or_with_A(self.register_E)

    def instruction_0xB4(self):  # OR H
        self.logical_or_with_A(self.register_H)

    def instruction_0xB5(self):  # OR L
        self.logical_or_with_A(self.register_L)

    def instruction_0xB6(self):  # OR (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.logical_or_with_A(value)

    def instruction_0xF6(self):  # OR #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.logical_or_with_A(n)

    def logical_or_with_A(self, value):
        self.register_A |= value

        # Set Z flag if result is zero
        self.set_flag('Z', self.register_A == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Reset H flag
        self.set_flag('H', False)

        # Reset C flag
        self.set_flag('C', False)


    #7
    def instruction_0xAF(self):  # XOR A
        self.logical_xor_with_A(self.register_A)

    def instruction_0xA8(self):  # XOR B
        self.logical_xor_with_A(self.register_B)

    def instruction_0xA9(self):  # XOR C
        self.logical_xor_with_A(self.register_C)

    def instruction_0xAA(self):  # XOR D
        self.logical_xor_with_A(self.register_D)

    def instruction_0xAB(self):  # XOR E
        self.logical_xor_with_A(self.register_E)

    def instruction_0xAC(self):  # XOR H
        self.logical_xor_with_A(self.register_H)

    def instruction_0xAD(self):  # XOR L
        self.logical_xor_with_A(self.register_L)

    def instruction_0xAE(self):  # XOR (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.logical_xor_with_A(value)

    def instruction_0xEE(self):  # XOR *
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.logical_xor_with_A(n)

    def logical_xor_with_A(self, value):
        self.register_A ^= value

        # Set Z flag if result is zero
        self.set_flag('Z', self.register_A == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Reset H flag
        self.set_flag('H', False)

        # Reset C flag
        self.set_flag('C', False)



    #8
    def instruction_0xBF(self):  # CP A
        self.compare_with_A(self.register_A)

    def instruction_0xB8(self):  # CP B
        self.compare_with_A(self.register_B)

    def instruction_0xB9(self):  # CP C
        self.compare_with_A(self.register_C)

    def instruction_0xBA(self):  # CP D
        self.compare_with_A(self.register_D)

    def instruction_0xBB(self):  # CP E
        self.compare_with_A(self.register_E)

    def instruction_0xBC(self):  # CP H
        self.compare_with_A(self.register_H)

    def instruction_0xBD(self):  # CP L
        self.compare_with_A(self.register_L)

    def instruction_0xBE(self):  # CP (HL)
        value = self.hardware.addressedMemory[(self.register_H << 8) | self.register_L]
        self.compare_with_A(value)

    def instruction_0xFE(self):  # CP #
        self.register_PC += 1
        n = self.hardware.addressedMemory[self.register_PC]
        self.compare_with_A(n)

    def compare_with_A(self, value):
        result = self.register_A - value

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Set N flag
        self.set_flag('N', True)

        # Set H flag if no borrow from bit 4
        self.set_flag('H', (self.register_A & 0x0F) < (value & 0x0F))

        # Set C flag for no borrow (A < n)
        self.set_flag('C', result < 0)


    #9
    def instruction_0x3C(self):  # INC A
        self.register_A = self.increment(self.register_A)

    def instruction_0x04(self):  # INC B
        self.register_B = self.increment(self.register_B)

    def instruction_0x0C(self):  # INC C
        self.register_C = self.increment(self.register_C)

    def instruction_0x14(self):  # INC D
        self.register_D = self.increment(self.register_D)

    def instruction_0x1C(self):  # INC E
        self.register_E = self.increment(self.register_E)

    def instruction_0x24(self):  # INC H
        self.register_H = self.increment(self.register_H)

    def instruction_0x2C(self):  # INC L
        self.register_L = self.increment(self.register_L)

    def instruction_0x34(self):  # INC (HL)
        address = (self.register_H << 8) | self.register_L
        value = self.hardware.addressedMemory[address]
        incremented_value = self.increment(value)
        self.hardware.addressedMemory[address] = incremented_value

    def increment(self, value):
        result = (value + 1) & 0xFF

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Reset N flag
        self.set_flag('N', False)

        # Set H flag if carry from bit 3
        self.set_flag('H', (value & 0x0F) == 0x0F)

        return result



    #10
    def instruction_0x3D(self):  # DEC A
        self.register_A = self.decrement(self.register_A)

    def instruction_0x05(self):  # DEC B
        self.register_B = self.decrement(self.register_B)

    def instruction_0x0D(self):  # DEC C
        self.register_C = self.decrement(self.register_C)

    def instruction_0x15(self):  # DEC D
        self.register_D = self.decrement(self.register_D)

    def instruction_0x1D(self):  # DEC E
        self.register_E = self.decrement(self.register_E)

    def instruction_0x25(self):  # DEC H
        self.register_H = self.decrement(self.register_H)

    def instruction_0x2D(self):  # DEC L
        self.register_L = self.decrement(self.register_L)

    def instruction_0x35(self):  # DEC (HL)
        address = (self.register_H << 8) | self.register_L
        value = self.hardware.addressedMemory[address]
        decremented_value = self.decrement(value)
        self.hardware.addressedMemory[address] = decremented_value

    def decrement(self, value):
        result = (value - 1) & 0xFF

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Set N flag
        self.set_flag('N', True)

        # Set H flag if no borrow from bit 4
        self.set_flag('H', (value & 0x0F) == 0)

        return result