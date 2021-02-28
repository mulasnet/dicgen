#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import os
import math
 
class MainCLS:
 
    total_of_words      = 0
    total_of_characters = 0
    current             = 0
    user_longitude      = 0
    user_use_letters    = False
    user_use_lowercase  = False
    user_use_uppercase  = False
    user_use_numbers    = False
    user_use_specials   = False
    user_filename       = ''
    list_string         = ''
 
 
    def processWord(self, str):
        self.current = self.current + 1
        self.file_handler.write("%s\n" % str)
        sys.stdout.write("\r- Progress: %d/%d (%s)                " % (self.current, self.total_of_words, str))
        sys.stdout.flush()
 
 
    def loop(self, prefix, loops):
        if loops == 0:
            return
 
        last_list = []
        for id_letter in range(0, len(self.list_string)):
            final_str = prefix + self.list_string[id_letter]
            last_list.append(final_str)
            self.processWord(final_str)
 
        for id_array in range(0, len(last_list)):
            self.loop(last_list[id_array], loops - 1)
 
 
    def getInput(self, message, type_inp, default_value):
        inp = raw_input(message)
        inp = inp.strip()
 
        if inp == '':
            inp = default_value
 
        if type_inp == 'int':
            try:
                val = int(inp)
                if val > -1:
                    return val
                else:
                    print '- Esto no es un numero. Prueba otra vez.'
                    return self.getInput(message, type_inp, default_value)
 
            except ValueError:
                print '- Esto no es un numero. Prueba otra vez.'
                return self.getInput(message, type_inp, default_value)
 
        elif type_inp == 'bool':
            if inp.lower() == 'y':
                return True
            elif inp.lower() == 'n':
                return False
            else:
                print '- Por Favor, responde [y][n]. Prueba otra vez.'
                return self.getInput(message, type_inp, default_value)
 
        elif type_inp == 'file':
            if os.path.isfile(inp):
                respond = self.getInput('- Este documento ya existe, Desea remplazarlo? [y/N] : ', 'bool', 'n')
                if respond == False:
                    return self.getInput(message, type_inp, default_value)
                else:
                    return inp
            else:
                return inp
 
        else:
            return inp
 
    def printSummary(self):
        print '                                                       '
        print '  -----------------------------------------------------'
        print '                         SUMARIO                       '
        print '  -----------------------------------------------------'
        print '- Max longitud de palabara                            : ' + '{0:,}'.format(self.user_max_longitude)
        print '- Total de caracteres para usar                       : ' + '{0:,}'.format(len(self.list_string))
        print '- Total de palabras                                   : ' + '{0:,}'.format(self.total_of_words)
 
        if self.user_use_letters == True:
            print '- Usar letras                                         : Yes'
            print '- Usar letras minuculas                               : ' + ('Yes' if self.user_use_lowercase  else 'No')
            print '- Usar letras mayusculas                              : ' + ('Yes' if self.user_use_uppercase  else 'No')
        else:
            print '- Usar letras                                         : No'
 
 
        print '- Usar numeros                                        : ' + ('Yes' if self.user_use_numbers  else 'No')
        print '- Usar caracteres especiales                          : ' + ('Yes' if self.user_use_specials else 'No')
        if os.path.isfile(self.user_filename):
            print '- Nombre del documneto                                : ' + self.user_filename + ' (override)'
        else:
            print '- Nombre del documento                                : ' + self.user_filename
 
        print '- Peso estimado del diccionario                       : ' + self.convertSize(self.total_of_characters)
 
        print '  -----------------------------------------------------'
        return self.getInput('- Quieres proceder?   [Y/n]  : ', 'bool', 'y')
 
 
    def convertSize(self, size, precision=2):
        # size = size + 0.0
        suffixes=['B','KB','MB','GB','TB','PB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
        return ("%.*f%s" % (precision, size, suffixes[suffixIndex]))
 
 
    def __init__(self):

        print '  ------------------------------------------------';
        print '  | Herramienta creado para el uso de PENTESTING |';
        print '  ------------------------------------------------';
        print '          Creado por Mulas y silence.exe ';
        print '         \------------------------------/       ';
        print ' '
        print ' '
        # self.user_min_longitude = self.getInput('- Enter min longitude of word [0]        : ', 'int',  '0')
        self.user_max_longitude = self.getInput('- Inserta la longitud maxima de la palbara            : ', 'int',  '4')
 
        self.user_use_letters   = self.getInput('- Usar letras?                             [Y/n]      : ', 'bool', 'y')
        
        if self.user_use_letters == True:
            self.user_use_lowercase   = self.getInput('- Usar minusculas?                         [Y/n]      : ', 'bool', 'y')
            self.user_use_uppercase   = self.getInput('- Usar mayusculas?                         [y/N]      : ', 'bool', 'n')
 
        self.user_use_numbers   = self.getInput('- Usar numeros?                            [Y/n]      : ', 'bool', 'y')
        self.user_use_specials  = self.getInput('- Usar caracteres especiales?              [y/N]      : ', 'bool', 'n')
        self.user_filename      = self.getInput('- Nombre del documento                  [dict.txt]    : ', 'file', 'dict.txt')
 
        self.list_string = ''
 
        if self.user_use_letters == True:
 
            if self.user_use_lowercase == True:
                self.list_string = self.list_string + 'abcdefghijklmnopqrstuvwxyz'
 
            if self.user_use_uppercase == True:
                self.list_string = self.list_string + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
        if self.user_use_numbers == True:
            self.list_string = self.list_string + '0123456789'
 
        if self.user_use_specials == True:
            self.list_string = self.list_string + '\\/\'"@#$%&/()=?¿!¡+-*_.:,;'
 
 
        self.total_of_words      = 0
        self.total_of_characters = 0
        for n in range(0, self.user_max_longitude):
            total = (len(self.list_string)**(n + 1))
            self.total_of_words      = self.total_of_words + total
            # (word length * count words) + \n
            self.total_of_characters = self.total_of_characters + (total * (n + 1)) + total
 
        # Summary
        response = self.printSummary()
        if response == False:
            return
 
        # Load file
        if os.path.isfile(self.user_filename):
            os.remove(self.user_filename)
        self.file_handler = open(self.user_filename, 'w')
 
        # Execute all
        self.loop('', self.user_max_longitude)
 
        # End
        self.file_handler.close()
        print "\r                                                       \r- End!"
 
if __name__ == '__main__':
    mainCLS = MainCLS()
