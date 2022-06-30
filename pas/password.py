def password(pwd):
    import time
    user = pwd
    with open('pwdlist.txt', 'w') as _pas_:
        _pas_.write (f'{user}12345\n{user}1234\n{user}123\n{user}123456\n{user}123456789\n{user}1234567\n{user}0\n{user}0123\n{user}0123456789\n{user}{user}\n{user}987654321\n{user}{user}0\n{user}123\n{user}\n{user}321\nadmin123\n12345\n123456\n1234567\n12345678\n123456789\n12345678910\npassword\npassword123')
        time.sleep(0.5)
        print ('\n\n\033[31m[*]\033[36m PasswordList \033[31m[pwdlist.txt] \033[36m<Created>\n\n')
        time.sleep(0.5)
        
