class InstructionSet__MISCELLANEOUS:

    #1
    def instruction_0xCB37(self):  # SWAP A
        self.register_A = self.swap_nibbles(self.register_A)

    def instruction_0xCB30(self):  # SWAP B
        self.register_B = self.swap_nibbles(self.register_B)

    def instruction_0xCB31(self):  # SWAP C
        self.register_C = self.swap_nibbles(self.register_C)

    def instruction_0xCB32(self):  # SWAP D
        self.register_D = self.swap_nibbles(self.register_D)

    def instruction_0xCB33(self):  # SWAP E
        self.register_E = self.swap_nibbles(self.register_E)

    def instruction_0xCB34(self):  # SWAP H
        self.register_H = self.swap_nibbles(self.register_H)

    def instruction_0xCB35(self):  # SWAP L
        self.register_L = self.swap_nibbles(self.register_L)

    def instruction_0xCB36(self):  # SWAP (HL)
        address = self.register_HL()
        value = self.hardware.addressedMemory[address]
        swapped_value = self.swap_nibbles(value)
        self.hardware.addressedMemory[address] = swapped_value

    def swap_nibbles(self, value):
        upper_nibble = (value & 0xF0) >> 4
        lower_nibble = (value & 0x0F) << 4
        result = upper_nibble | lower_nibble

        # Set Z flag if result is zero
        self.set_flag('Z', result == 0)

        # Reset N, H, and C flags
        self.set_flag('N', False)
        self.set_flag('H', False)
        self.set_flag('C', False)

        return result


    #2
    def instruction_0x27(self):  # DAA
        correction = 0
        if self.get_flag('H') or (self.register_A & 0x0F) > 9:
            correction = 0x06
        if self.get_flag('C') or self.register_A > 0x9F:
            correction |= 0x60

        if self.get_flag('N'):
            self.register_A -= correction
        else:
            self.register_A += correction

        self.set_flag('Z', self.register_A == 0)
        self.set_flag('H', False)

        # Set or reset C flag according to operation
        self.set_flag('C', (correction & 0x60) != 0)

    #3
    def instruction_0x2F(self):  # CPL
        self.register_A = ~self.register_A & 0xFF

        # Set N and H flags
        self.set_flag('N', True)
        self.set_flag('H', True)


    #4
    def instruction_0x3F(self):  # CCF
        self.set_flag('N', False)
        self.set_flag('H', False)
        self.set_flag('C', not self.get_flag('C'))


    #5
    def instruction_0x37(self):  # SCF
        self.set_flag('N', False)
        self.set_flag('H', False)
        self.set_flag('C', True)


    #6
    def instruction_0x00(self):  # NOP
        pass  # No operation


    #7
    def instruction_0x76(self):  # HALT
        # Implementação específica para colocar a CPU em estado de baixo consumo
        # de energia até que ocorra uma interrupção.
        # Lembre-se de implementar a lógica para lidar com interrupções para sair do modo de espera.
        pass


    #8
    def instruction_0x10_00(self):  # STOP
        # Implementação específica para colocar a CPU e o display LCD em modo de espera
        # até que um botão seja pressionado.
        # Lembre-se de implementar a lógica para sair do modo de espera quando um botão for pressionado.
        pass


    #9
    def instruction_0xF3(self):  # DI
        # Desabilita as interrupções após a próxima instrução.
        self.interrupts_enabled = False


    #10
    def instruction_0xFB(self):  # EI
        # Habilita as interrupções após a próxima instrução.
        self.interrupts_enabled = True