import pygame
from CPU.CPU import *

class gbEmulator:
    def __init__(self,gbFile):

        #CPU
        self.CPU = CPU(self)

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
                #self.bootloader.append(read.hex().upper())
                #self.bootloader.append(read)
                self.bootloader.append(int.from_bytes(read, byteorder='big', signed=False))
                read = file.read(1)
        print(self.bootloader)
        #config vram
        self.vram = []

        #adressead memory config
        self.addressedMemory = []
        for i in range(int(2**16)):
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
            self.CPU.cicle()

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


        CPU STATE
        {self.CPU}


        MEMORY MAP
        {memoryMap}
        '''

emulacao = gbEmulator('zelda.gb')
emulacao.emulate()
print(emulacao)
