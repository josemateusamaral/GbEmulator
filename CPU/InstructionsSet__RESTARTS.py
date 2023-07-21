class InstructionsSet__RESTARTS:

    #1
    def instruction_C7(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0000

    def instruction_CF(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0008

    def instruction_D7(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0010

    def instruction_DF(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0018

    def instruction_E7(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0020

    def instruction_EF(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0028

    def instruction_F7(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0030

    def instruction_FF(self):
        self.push_word_to_stack(self.program_counter)
        self.program_counter = 0x0038
