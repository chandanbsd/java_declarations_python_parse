import re

with open('correct.java', 'w') as outf:
    with open('input.java') as fref:

        lines = fref.readlines()
        
        sflag = 0
        eflag = 0
        count = 1
        
        for line in lines:
            flag = 0 
            count += 1
            
            line2 = line.rstrip()
            if line2 == '':
                continue
            

            if re.match('import [_a-zA-Z]+[._a-zA-Z*]+',line):
                print('Java library or API included')
                flag = 1
                outf.write(line)
                continue
                
            
                
            if re.match('class [a-zA-Z][a-zA-Z_0-9]+{',line):
                print('Beginning of class declarations')
                outf.write(line)
                flag = 1
                sflag = 1

            line = line.strip()

            if(sflag == 0):
                print('***************ERROR : at line {}'.format(count))
                print('***************Class declaration not begun correctly')
                outf.write('class autoCreate {\n')
                sflag = 1
            
            

            if re.search('public',line):
                print('***************ERROR : at line {}'.format(count))
                print('***************Error: Variables Inside Class Must Be Private***',end=" ")
                outf.write('private ')
               
            
            elif re.search('private',line):
                print('Private Acess Specified',end=" ")
                outf.write('private ')
                

            elif re.search('protected',line):
                print('***************ERROR : at line {}'.format(count))
                print('***************Error: Variables Inside Class Must Be Private***',end=" ")
                outf.write('private ')
                

            if re.search('static',line):
                print('Static Declaration',end=" ")
                outf.write('static ')
                

            if re.search('final',line):
                print('Constant Declaration',end=" ")
                outf.write('final ')
                
                
            
            line = line.replace('private','')
            line = line.replace('public','')
            line = line.replace('protected','')
            line = line.replace('final','')
            line = line.replace('static','')
            line = line.strip()

            
            if re.match('int [a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Integer Variable Declared')
                outf.write(re.match('int [a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('int ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Multiple Integer Variables Declared')
                outf.write(re.match('int ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('int [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
                print('Integer Array Declared')
                outf.write(re.match('int [a-zA-Z_][a-zA-Z_0-9]*\[\];',line).group(0) + '\n')
                flag = 1


            if re.match('float [a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Floating Point Variable Declared')
                outf.write(re.match('float [a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('float ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Multiple Floating Point Variables Declared')
                outf.write(re.match('float ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('float [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
                print('Floating Point Array Declared')
                outf.write(re.match('float [a-zA-Z_][a-zA-Z_0-9]*\[\];',line).group(0) + '\n')
                flag = 1



            if re.match('String [a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('String Variable Declared')
                outf.write(re.match('String [a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('String ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('String Variables Declared')
                outf.write(re.match('String ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('String [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
                print('String Array Declared')
                outf.write(re.match('String [a-zA-Z_][a-zA-Z_0-9]*\[\];',line).group(0) + '\n')
                flag = 1


            if re.match('char [a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Character Variable Declared')
                outf.write(re.match('char [a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('char ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line):
                print('Multiple Character Variables Declared')
                outf.write(re.match('char ([a-zA-Z_][a-zA-Z_0-9]*,)+[a-zA-Z_][a-zA-Z_0-9]*;',line).group(0) + '\n')
                flag = 1

            if re.match('char [a-zA-Z_][a-zA-Z_0-9]*\[\];',line):
                print('Character Arary Declared')
                outf.write(re.match('char [a-zA-Z_][a-zA-Z_0-9]*\[\];',line).group(0) + '\n')
                flag = 1
            


            if re.match('}', line):
                print('End of class declaration')
                outf.write(re.match('}', line).group(0) + '\n')
                flag = 1
                break

            if flag == 0 and len(lines) != count:
                print('***************ERROR : at line {}'.format(count))

                print('***************Semicolon missing')
                key_list = ['public', 'private', 'static', 'protected', 'final']
                    
                for item in key_list:
                    line.replace(item,'')
                outf.write(line + ';\n')
            
            if len(lines) == count:
                print('***************ERROR')
                print('***************Class declaration not closed')
                outf.write('}\n')
                break
           
            