import pygame
from CPU import *

class gbEmulator (CPU):
    def __init__(self,gbFile):

        #cartrige configue
        self.emulando = False
        self.cartrige = []
        with open(gbFile,'rb') as file:
            read = file.read(1)
            while read:
                self.cartrige.append(int.from_bytes(read, byteorder='big'))
                read = file.read(1)

        #config bootloader
        self.bootloader = []
        with open('bootloader.gb','rb') as file:
            read = file.read(1)
            while read:
                self.bootloader.append(int.from_bytes(read, byteorder='big'))
                read = file.read(1)
        
        #config vram
        self.vram = []

        #adressead memory config
        self.addressedMemory = []
        for i in range(64000):
            self.addressedMemory.append(0)

        #config display
        pygame.init()

        #configurar display
        self.display = pygame.display.set_mode((160,144))
        self.displayBackgroundColor = (255, 255, 255)

        #mapear os pixels
        self.pixels = []
        for x in range(160):
            for y in range(144):
                self.pixels.append([x,y,[0,0,0]])

    def emulate(self):
        self.emulando = True

        #passing bootloader to the ram
        for index,bootData in enumerate(self.bootloader):
            self.addressedMemory[index] = bootData

        # Loop principal do jogo
        while self.emulando:
            self.display.fill((255,0,0))
            
            # executar instrucao
            instrucao = self.addressedMemory[self.register_PC]
            self.execute_instruction(instrucao)
            self.register_PC += 1

            # teclas
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.emulando = False

            # renderizar
            for pixel in self.pixels:
                pygame.draw.rect(self.display,pixel[2], (pixel[0], pixel[1],1,1))
            
            pygame.display.flip()
        # Encerrando o Pygame
        pygame.quit()

    def __str__(self):
        memoryMap = ''
        for index,i in enumerate(self.addressedMemory):
            memoryMap += str(i) + ' '
            if index % 64 == 0:
                memoryMap += '\n'
        memoryMap = ''

        return f'''
        running: {self.emulando}
        cartrige size: {len(self.cartrige)} bytes
        bootloader size: {len(self.bootloader)} bytes

        PC: {self.register_PC}
        A: {self.register_A}
        B: {self.register_B}
        C: {self.register_C}
        D: {self.register_D}
        E: {self.register_E}
        F: {self.register_F}
        H: {self.register_H}
        I: {self.register_I}

        MEMORY MAP
        {memoryMap}
        '''

emulacao = gbEmulator('zelda.gb')
emulacao.emulate()
print(emulacao)
