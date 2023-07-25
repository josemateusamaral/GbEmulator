class InstructionsSet__JUMPS:


    #1
    def instruction_0xC3(self):
        # Combine the next two bytes to form the jump address nn
        low_byte = self.fetch()
        high_byte = self.fetch()
        jump_address = (high_byte << 8) | low_byte

        # Set the program counter (PC) to the jump address
        self.register_PC = jump_address


    #2
    def instruction_0xC2(self):
        if not self.get_flag("Z"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.register_PC = jump_address

    def instruction_0xCA(self):
        if self.get_flag("Z"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.register_PC = jump_address

    def instruction_0xD2(self):
        if not self.get_flag("C"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.register_PC = jump_address

    def instruction_0xDA(self):
        if self.get_flag("C"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.register_PC = jump_address


    #3
    def instruction_0xE9(self):
        jump_address = self.combine_registers(self.register_H, self.register_L)
        self.register_PC = jump_address


    #4
    def instruction_0x18(self):
        n = self.get_immediate_signed()
        self.register_PC = (self.register_PC + n) & 0xFFFF


    #5
    def instruction_0x20(self):
        if not self.get_flag('Z'):
            self.register_PC = self.hardware.addressedMemory[self.register_PC+1]

    def instruction_0x28(self):
        if self.get_flag('Z'):
            self.register_PC = self.hardware.addressedMemory[self.register_PC+1]

    def instruction_0x30(self):
        if not self.get_flag('C'):
            self.register_PC = self.hardware.addressedMemory[self.register_PC+1]

    def instruction_0x38(self):
        if self.get_flag('C'):
            self.register_PC = self.hardware.addressedMemory[self.register_PC+1]





