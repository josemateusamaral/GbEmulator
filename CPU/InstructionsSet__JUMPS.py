class InstructionsSet__JUMPS:


    #1
    def instruction_C3(self):
        # Combine the next two bytes to form the jump address nn
        low_byte = self.fetch()
        high_byte = self.fetch()
        jump_address = (high_byte << 8) | low_byte

        # Set the program counter (PC) to the jump address
        self.program_counter = jump_address


    #2
    def instruction_C2(self):
        if not self.get_flag("Z"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.program_counter = jump_address

    def instruction_CA(self):
        if self.get_flag("Z"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.program_counter = jump_address

    def instruction_D2(self):
        if not self.get_flag("C"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.program_counter = jump_address

    def instruction_DA(self):
        if self.get_flag("C"):
            low_byte = self.fetch()
            high_byte = self.fetch()
            jump_address = (high_byte << 8) | low_byte
            self.program_counter = jump_address


    #3
    def instruction_E9(self):
        jump_address = self.combine_registers(self.register_H, self.register_L)
        self.program_counter = jump_address


    #4
    def instruction_18(self):
        n = self.get_immediate_signed()
        self.program_counter = (self.program_counter + n) & 0xFFFF


    #5
    def instruction_20(self):
        if not self.test_flag(Flags.Z):
            n = self.get_immediate_signed()
            self.program_counter = (self.program_counter + n) & 0xFFFF

    def instruction_28(self):
        if self.test_flag(Flags.Z):
            n = self.get_immediate_signed()
            self.program_counter = (self.program_counter + n) & 0xFFFF

    def instruction_30(self):
        if not self.test_flag(Flags.C):
            n = self.get_immediate_signed()
            self.program_counter = (self.program_counter + n) & 0xFFFF

    def instruction_38(self):
        if self.test_flag(Flags.C):
            n = self.get_immediate_signed()
            self.program_counter = (self.program_counter + n) & 0xFFFF





