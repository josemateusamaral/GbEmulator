class InstructionsSet__BIT_OPCODES:

    #1
    def test_bit(self, value, bit):
        # Testa o bit específico no valor
        return (value >> bit) & 0x1

    def set_flag_bit(self, flag, value):
        # Atualiza o bit do flag com o valor especificado (0 ou 1)
        if value:
            self.set_flag(flag, True)
        else:
            self.set_flag(flag, False)

    def instruction_CB47(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_A, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB40(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_B, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB41(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_C, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB42(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_D, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB43(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_E, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB44(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_H, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB45(self):
        self.set_flag_bit('Z', not self.test_bit(self.register_L, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)

    def instruction_CB46(self):
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        self.set_flag_bit('Z', not self.test_bit(value, 0))
        self.set_flag('N', False)
        self.set_flag('H', True)



    #2
    def set_bit(self, value, bit):
        # Seta o bit específico no valor
        return value | (1 << bit)

    def instruction_CBC7(self):
        self.register_A = self.set_bit(self.register_A, 0)

    def instruction_CBC0(self):
        self.register_B = self.set_bit(self.register_B, 0)

    def instruction_CBC1(self):
        self.register_C = self.set_bit(self.register_C, 0)

    def instruction_CBC2(self):
        self.register_D = self.set_bit(self.register_D, 0)

    def instruction_CBC3(self):
        self.register_E = self.set_bit(self.register_E, 0)

    def instruction_CBC4(self):
        self.register_H = self.set_bit(self.register_H, 0)

    def instruction_CBC5(self):
        self.register_L = self.set_bit(self.register_L, 0)

    def instruction_CBC6(self):
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.set_bit(value, 0)
        self.hardware.write_byte(address, value)


    #3
    def reset_bit(self, value, bit):
        # Reseta o bit específico no valor
        return value & ~(1 << bit)

    def instruction_CB87(self):
        self.register_A = self.reset_bit(self.register_A, 0)

    def instruction_CB80(self):
        self.register_B = self.reset_bit(self.register_B, 0)

    def instruction_CB81(self):
        self.register_C = self.reset_bit(self.register_C, 0)

    def instruction_CB82(self):
        self.register_D = self.reset_bit(self.register_D, 0)

    def instruction_CB83(self):
        self.register_E = self.reset_bit(self.register_E, 0)

    def instruction_CB84(self):
        self.register_H = self.reset_bit(self.register_H, 0)

    def instruction_CB85(self):
        self.register_L = self.reset_bit(self.register_L, 0)

    def instruction_CB86(self):
        address = self.combine_registers(self.register_H, self.register_L)
        value = self.hardware.read_byte(address)
        value = self.reset_bit(value, 0)
        self.hardware.write_byte(address, value)
