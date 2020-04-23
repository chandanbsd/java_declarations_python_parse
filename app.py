import re

with open('test.java') as fref:

    lines = fref.readlines()

    for line in lines:
        if re.match('import [_a-zA-Z]+[._a-zA-Z*]+',line):
            print('Java library or API included')
            
        if re.match('class [a-zA-Z][a-zA-Z_0-9]+{',line):
            print('Beginning of class declarations')

        line = line.strip()

        if re.search('public',line):
            print('Public Acess Specified',end=" ")
        
        if re.search('private',line):
            print('Private Acess Specified',end=" ")

        if re.search('protected',line):
            print('Protected Acess Specified',end=" ")

        if re.search('static',line):
            print('Static Declaration',end=" ")

        if re.search('final',line):
            print('Constant Declaration',end=" ")
            
        if re.match('int [a-zA-Z_][a-zA-Z_0-9]*;',line):
            print('Integer Variable Declared')

        if re.match('int ([a-zA-Z_][a-zA-Z_0-9]*,)+,[a-zA-Z_][a-zA-Z_0-9]* ;',line):
            print('Multiple Integer Variables Declared')

        if re.match('int [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
            print('Integer Array Declared')

        
        if re.match('float [a-zA-Z_][a-zA-Z_0-9]*;',line):
            print('Floating Point Variable Declared')

        if re.match('float ([a-zA-Z_][a-zA-Z_0-9]*,)+,[a-zA-Z_][a-zA-Z_0-9]* ;',line):
            print('Multiple Floating Point Variables Declared')

        if re.match('float [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
            print('Floating Point Array Declared')



        if re.match('String [a-zA-Z_][a-zA-Z_0-9]*;',line):
            print('String Variable Declared')

        if re.match('String ([a-zA-Z_][a-zA-Z_0-9]*,)+,[a-zA-Z_][a-zA-Z_0-9]* ;',line):
            print('String Variables Declared')

        if re.match('String [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
            print('String Array Declared')


        if re.match('char [a-zA-Z_][a-zA-Z_0-9]*;',line):
            print('Character Variable Declared')

        if re.match('char ([a-zA-Z_][a-zA-Z_0-9]*,)+,[a-zA-Z_][a-zA-Z_0-9]* ;',line):
            print('Multiple Character Variables Declared')

        if re.match('char [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
            print('Character Arary Declared')

        if re.match('}', line):
            print('End of class declaration')
            break