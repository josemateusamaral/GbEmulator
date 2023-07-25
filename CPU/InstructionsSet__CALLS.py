class InstructionsSet__CALLS:

    #1
    def instruction_0xCD(self):
        address = self.get_immediate_word()
        self.push_word_to_stack(self.register_PC)
        self.register_PC = address


    #2
    def instruction_0xC4(self):
        address = self.get_immediate_word()
        if not self.zero_flag:
            self.push_word_to_stack(self.register_PC)
            self.register_PC = address

    def instruction_0xCC(self):
        address = self.get_immediate_word()
        if self.zero_flag:
            self.push_word_to_stack(self.register_PC)
            self.register_PC = address

    def instruction_0xD4(self):
        address = self.get_immediate_word()
        if not self.carry_flag:
            self.push_word_to_stack(self.register_PC)
            self.register_PC = address

    def instruction_0xDC(self):
        address = self.get_immediate_word()
        if self.carry_flag:
            self.push_word_to_stack(self.register_PC)
            self.register_PC = address


