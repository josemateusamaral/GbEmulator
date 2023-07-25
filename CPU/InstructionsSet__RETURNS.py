class InstructionsSet__RETURNS:

    #1
    def instruction_0xC9(self):
        self.register_PC = self.pop_word_from_stack()


    #2
    def instruction_0xC0(self):
        if not self.get_flag(FLAG_Z):
            self.register_PC = self.pop_word_from_stack()

    def instruction_0xC8(self):
        if self.get_flag(FLAG_Z):
            self.register_PC = self.pop_word_from_stack()

    def instruction_0xD0(self):
        if not self.get_flag(FLAG_C):
            self.register_PC = self.pop_word_from_stack()

    def instruction_0xD8(self):
        if self.get_flag(FLAG_C):
            self.register_PC = self.pop_word_from_stack()


    #3
    def instruction_0xD9(self):
        self.register_PC = self.pop_word_from_stack()
        self.enable_interrupts()

