class InstructionsSet__CALLS:

    #1
    def instruction_CD(self):
        address = self.get_immediate_word()
        self.push_word_to_stack(self.program_counter)
        self.program_counter = address


    #2
    def instruction_C4(self):
        address = self.get_immediate_word()
        if not self.zero_flag:
            self.push_word_to_stack(self.program_counter)
            self.program_counter = address

    def instruction_CC(self):
        address = self.get_immediate_word()
        if self.zero_flag:
            self.push_word_to_stack(self.program_counter)
            self.program_counter = address

    def instruction_D4(self):
        address = self.get_immediate_word()
        if not self.carry_flag:
            self.push_word_to_stack(self.program_counter)
            self.program_counter = address

    def instruction_DC(self):
        address = self.get_immediate_word()
        if self.carry_flag:
            self.push_word_to_stack(self.program_counter)
            self.program_counter = address


