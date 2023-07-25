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
        bitsSequence = []
        with open('bootloader.gb','rb') as file:
            read = file.read(1)
            while read:
                #self.bootloader.append(read.hex().upper())
                #self.bootloader.append(read)
                self.bootloader.append(int.from_bytes(read, byteorder='big', signed=False))
                bitsSequence.append(hex(int.from_bytes(read, byteorder='big', signed=False)))
                read = file.read(1)
        #print(self.bootloader)
        print(bitsSequence)
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
        for address in range(0x0000, 0xFFFF + 1, 8):
            if '6kB ROM bank' not in memoryMap:
                memoryMap += '\n\n6kB ROM bank'
            if '6kB switchable ROM bank' not in memoryMap and address > 0x4000:
                memoryMap += '\n\n6kB switchable ROM bank'
            if '8kB Video RAM' not in memoryMap and address > 0x8000:
                memoryMap += '\n\n8kB Video RAM'
            if '8kB switchable ROM bank' not in memoryMap and address > 0xA000:
                memoryMap += '\n\n8kB switchable ROM bank'
            if '8kB Internal RAM' not in memoryMap and address > 0xC000:
                memoryMap += '\n\n8kB Internal RAM'
            if 'Echo of 8kB Internal RAM' not in memoryMap and address > 0xE000:
                memoryMap += '\n\nEcho of 8kB Internal RAM'
            if 'Sprite Attrib Memory (OAM)' not in memoryMap and address > 0xFE00:
                memoryMap += '\n\nSprite Attrib Memory (OAM)'
            if 'Empty but unusable for I/O' not in memoryMap and address > 0xFEA0:
                memoryMap += '\n\nEmpty but unusable for I/O'
            if 'I/O ports' not in memoryMap and address > 0xFF00:
                memoryMap += '\n\nI/O ports'
            if 'Empty but unusable for I/O' not in memoryMap and address > 0xFF4C:
                memoryMap += '\n\nEmpty but unusable for I/O'
            if 'Internal RAM' not in memoryMap and address > 0xFF80:
                memoryMap += '\n\nInternal RAM'
            if 'Interrupt Enable Register' not in memoryMap and address > 0xFFFF:
                memoryMap += '\n\nInterrupt Enable Register'

            memoryMap += '\n' + str(hex(address)) + ' : '
            for i in range(8):
                memoryMap += str(self.addressedMemory[address + i]) + '\t'

        with open('memory_map.txt','w') as file:
            file.write(memoryMap)

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
