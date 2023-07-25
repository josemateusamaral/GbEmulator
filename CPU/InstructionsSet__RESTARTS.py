class InstructionsSet__RESTARTS:

    #1
    def instruction_0xC7(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0000

    def instruction_0xCF(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0008

    def instruction_0xD7(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0010

    def instruction_0xDF(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0018

    def instruction_0xE7(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0020

    def instruction_0xEF(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0028

    def instruction_0xF7(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0030

    def instruction_0xFF(self):
        self.push_word_to_stack(self.register_PC)
        self.register_PC = 0x0038
