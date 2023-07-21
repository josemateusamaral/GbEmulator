class InstructionsSet__ROTATA_SHIFT:

    #1
    def instruction_0x07(self):  # RLCA
        # Rotaciona o registrador A para a esquerda
        # Old bit 7 para o Carry flag
        old_bit_7 = (self.register_A & 0b10000000) >> 7
        self.register_A = ((self.register_A << 1) & 0xFF) | old_bit_7

        # Define os flags afetados
        self.set_flag('Z', self.register_A == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)
        self.set_flag('C', bool(old_bit_7))



    #2
    def instruction_0x17(self):  # RLA
        # Rotaciona o registrador A para a esquerda através do Carry flag
        carry_bit = 1 if self.get_flag('C') else 0

        # Armazena o bit mais significativo de A no Carry flag
        old_bit_7 = (self.register_A & 0b10000000) >> 7
        self.set_flag('C', bool(old_bit_7))

        # Realiza a rotação do registrador A
        self.register_A = ((self.register_A << 1) & 0xFF) | carry_bit

        # Define os flags afetados
        self.set_flag('Z', self.register_A == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)



    #3
    def instruction_0x0F(self):  # RRCA
        # Rotaciona o registrador A para a direita
        # e armazena o bit menos significativo no Carry flag
        old_bit_0 = self.register_A & 0b00000001
        self.set_flag('C', bool(old_bit_0))

        # Realiza a rotação do registrador A
        self.register_A = ((self.register_A >> 1) & 0xFF) | (old_bit_0 << 7)

        # Define os flags afetados
        self.set_flag('Z', self.register_A == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)


    #4
    def instruction_0x1F(self):  # RRA
        # Rotaciona o registrador A para a direita através do Carry flag
        # e armazena o bit menos significativo no Carry flag
        old_carry = self.get_flag('C')
        new_carry = self.register_A & 0b00000001
        self.set_flag('C', bool(new_carry))

        # Realiza a rotação do registrador A através do Carry flag
        self.register_A = ((self.register_A >> 1) & 0xFF) | (old_carry << 7)

        # Define os flags afetados
        self.set_flag('Z', self.register_A == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)


    #5
    def rotate_left_carry(self, value):
        # Realiza a rotação do valor para a esquerda através do Carry flag
        carry = (value >> 7) & 0b1  # Obtém o bit mais significativo (bit 7)
        value = ((value << 1) & 0xFF) | carry  # Rotação para a esquerda
        self.set_flag('C', bool(carry))  # Define o Carry flag

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB07(self):  # RLC A
        self.register_A = self.rotate_left_carry(self.register_A)

    def instruction_0xCB00(self):  # RLC B
        self.register_B = self.rotate_left_carry(self.register_B)

    def instruction_0xCB01(self):  # RLC C
        self.register_C = self.rotate_left_carry(self.register_C)

    def instruction_0xCB02(self):  # RLC D
        self.register_D = self.rotate_left_carry(self.register_D)

    def instruction_0xCB03(self):  # RLC E
        self.register_E = self.rotate_left_carry(self.register_E)

    def instruction_0xCB04(self):  # RLC H
        self.register_H = self.rotate_left_carry(self.register_H)

    def instruction_0xCB05(self):  # RLC L
        self.register_L = self.rotate_left_carry(self.register_L)

    def instruction_0xCB06(self):  # RLC (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.rotate_left_carry(value)
        self.hardware.write_byte(address, value)



    #6
    def rotate_left_through_carry(self, value):
        # Realiza a rotação do valor para a esquerda através do Carry flag
        carry = self.get_flag('C')  # Obtém o valor do Carry flag
        new_carry = (value >> 7) & 0b1  # Obtém o bit mais significativo (bit 7)
        value = ((value << 1) & 0xFF) | carry  # Rotação para a esquerda com Carry

        # Define o novo Carry flag com o valor do bit mais significativo antes da rotação
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB17(self):  # RL A
        self.register_A = self.rotate_left_through_carry(self.register_A)

    def instruction_0xCB10(self):  # RL B
        self.register_B = self.rotate_left_through_carry(self.register_B)

    def instruction_0xCB11(self):  # RL C
        self.register_C = self.rotate_left_through_carry(self.register_C)

    def instruction_0xCB12(self):  # RL D
        self.register_D = self.rotate_left_through_carry(self.register_D)

    def instruction_0xCB13(self):  # RL E
        self.register_E = self.rotate_left_through_carry(self.register_E)

    def instruction_0xCB14(self):  # RL H
        self.register_H = self.rotate_left_through_carry(self.register_H)

    def instruction_0xCB15(self):  # RL L
        self.register_L = self.rotate_left_through_carry(self.register_L)

    def instruction_0xCB16(self):  # RL (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.rotate_left_through_carry(value)
        self.hardware.write_byte(address, value)


    #7
    def rotate_right_through_carry(self, value):
        # Realiza a rotação do valor para a direita através do Carry flag
        carry = self.get_flag('C')  # Obtém o valor do Carry flag
        new_carry = value & 0b1  # Obtém o bit menos significativo (bit 0)
        value = ((value >> 1) & 0x7F) | (carry << 7)  # Rotação para a direita com Carry

        # Define o novo Carry flag com o valor do bit menos significativo antes da rotação
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB0F(self):  # RRC A
        self.register_A = self.rotate_right_through_carry(self.register_A)

    def instruction_0xCB08(self):  # RRC B
        self.register_B = self.rotate_right_through_carry(self.register_B)

    def instruction_0xCB09(self):  # RRC C
        self.register_C = self.rotate_right_through_carry(self.register_C)

    def instruction_0xCB0A(self):  # RRC D
        self.register_D = self.rotate_right_through_carry(self.register_D)

    def instruction_0xCB0B(self):  # RRC E
        self.register_E = self.rotate_right_through_carry(self.register_E)

    def instruction_0xCB0C(self):  # RRC H
        self.register_H = self.rotate_right_through_carry(self.register_H)

    def instruction_0xCB0D(self):  # RRC L
        self.register_L = self.rotate_right_through_carry(self.register_L)

    def instruction_0xCB0E(self):  # RRC (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.rotate_right_through_carry(value)
        self.hardware.write_byte(address, value)




    #8
    def rotate_right_through_carry(self, value):
        # Realiza a rotação do valor para a direita através do Carry flag
        carry = self.get_flag('C')  # Obtém o valor do Carry flag
        new_carry = value & 0b1  # Obtém o bit menos significativo (bit 0)
        value = ((value >> 1) & 0x7F) | (carry << 7)  # Rotação para a direita com Carry

        # Define o novo Carry flag com o valor do bit menos significativo antes da rotação
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB1F(self):  # RR A
        self.register_A = self.rotate_right_through_carry(self.register_A)

    def instruction_0xCB18(self):  # RR B
        self.register_B = self.rotate_right_through_carry(self.register_B)

    def instruction_0xCB19(self):  # RR C
        self.register_C = self.rotate_right_through_carry(self.register_C)

    def instruction_0xCB1A(self):  # RR D
        self.register_D = self.rotate_right_through_carry(self.register_D)

    def instruction_0xCB1B(self):  # RR E
        self.register_E = self.rotate_right_through_carry(self.register_E)

    def instruction_0xCB1C(self):  # RR H
        self.register_H = self.rotate_right_through_carry(self.register_H)

    def instruction_0xCB1D(self):  # RR L
        self.register_L = self.rotate_right_through_carry(self.register_L)

    def instruction_0xCB1E(self):  # RR (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.rotate_right_through_carry(value)
        self.hardware.write_byte(address, value)



    #9
    def shift_left_arithmetic(self, value):
        # Realiza o shift left aritmético do valor
        new_carry = (value >> 7) & 0x1  # Obtém o bit mais significativo (bit 7)
        value = (value << 1) & 0xFE  # Shift left com LSB (bit 0) definido para 0

        # Define o novo Carry flag com o valor do bit mais significativo antes do shift
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB27(self):  # SLA A
        self.register_A = self.shift_left_arithmetic(self.register_A)

    def instruction_0xCB20(self):  # SLA B
        self.register_B = self.shift_left_arithmetic(self.register_B)

    def instruction_0xCB21(self):  # SLA C
        self.register_C = self.shift_left_arithmetic(self.register_C)

    def instruction_0xCB22(self):  # SLA D
        self.register_D = self.shift_left_arithmetic(self.register_D)

    def instruction_0xCB23(self):  # SLA E
        self.register_E = self.shift_left_arithmetic(self.register_E)

    def instruction_0xCB24(self):  # SLA H
        self.register_H = self.shift_left_arithmetic(self.register_H)

    def instruction_0xCB25(self):  # SLA L
        self.register_L = self.shift_left_arithmetic(self.register_L)

    def instruction_0xCB26(self):  # SLA (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.shift_left_arithmetic(value)
        self.hardware.write_byte(address, value)




    #10
    def shift_right_arithmetic(self, value):
        # Realiza o shift right aritmético do valor
        new_carry = value & 0x1  # Obtém o bit menos significativo (bit 0)
        msb = value & 0x80  # Obtém o bit mais significativo (bit 7)

        value = (value >> 1) | msb  # Shift right, mantendo o valor do MSB

        # Define o novo Carry flag com o valor do bit menos significativo antes do shift
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB2F(self):  # SRA A
        self.register_A = self.shift_right_arithmetic(self.register_A)

    def instruction_0xCB28(self):  # SRA B
        self.register_B = self.shift_right_arithmetic(self.register_B)

    def instruction_0xCB29(self):  # SRA C
        self.register_C = self.shift_right_arithmetic(self.register_C)

    def instruction_0xCB2A(self):  # SRA D
        self.register_D = self.shift_right_arithmetic(self.register_D)

    def instruction_0xCB2B(self):  # SRA E
        self.register_E = self.shift_right_arithmetic(self.register_E)

    def instruction_0xCB2C(self):  # SRA H
        self.register_H = self.shift_right_arithmetic(self.register_H)

    def instruction_0xCB2D(self):  # SRA L
        self.register_L = self.shift_right_arithmetic(self.register_L)

    def instruction_0xCB2E(self):  # SRA (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.shift_right_arithmetic(value)
        self.hardware.write_byte(address, value)


    #11
    def shift_right_logical(self, value):
        # Realiza o shift right lógico do valor
        new_carry = value & 0x1  # Obtém o bit menos significativo (bit 0)

        value = value >> 1  # Shift right, setando o bit mais significativo como 0

        # Define o novo Carry flag com o valor do bit menos significativo antes do shift
        self.set_flag('C', bool(new_carry))

        # Define os flags afetados
        self.set_flag('Z', value == 0)
        self.set_flag('N', False)
        self.set_flag('H', False)

        return value

    def instruction_0xCB3F(self):  # SRL A
        self.register_A = self.shift_right_logical(self.register_A)

    def instruction_0xCB38(self):  # SRL B
        self.register_B = self.shift_right_logical(self.register_B)

    def instruction_0xCB39(self):  # SRL C
        self.register_C = self.shift_right_logical(self.register_C)

    def instruction_0xCB3A(self):  # SRL D
        self.register_D = self.shift_right_logical(self.register_D)

    def instruction_0xCB3B(self):  # SRL E
        self.register_E = self.shift_right_logical(self.register_E)

    def instruction_0xCB3C(self):  # SRL H
        self.register_H = self.shift_right_logical(self.register_H)

    def instruction_0xCB3D(self):  # SRL L
        self.register_L = self.shift_right_logical(self.register_L)

    def instruction_0xCB3E(self):  # SRL (HL)
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.shift_right_logical(value)
        self.hardware.write_byte(address, value)


    