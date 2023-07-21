class InstructionsSet__RETURNS:

    #1
    def instruction_C9(self):
        self.program_counter = self.pop_word_from_stack()


    #2
    def instruction_C0(self):
        if not self.get_flag(FLAG_Z):
            self.program_counter = self.pop_word_from_stack()

    def instruction_C8(self):
        if self.get_flag(FLAG_Z):
            self.program_counter = self.pop_word_from_stack()

    def instruction_D0(self):
        if not self.get_flag(FLAG_C):
            self.program_counter = self.pop_word_from_stack()

    def instruction_D8(self):
        if self.get_flag(FLAG_C):
            self.program_counter = self.pop_word_from_stack()


    #3
    def instruction_D9(self):
        self.program_counter = self.pop_word_from_stack()
        self.enable_interrupts()

