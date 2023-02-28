from random import randint,choice,shuffle
from string import ascii_lowercase,ascii_uppercase


class SavePass:
    L_LETTERS_LIST= [letter for letter in ascii_lowercase]
    U_LETTERS_LIST =[letter for letter in ascii_uppercase]
    NUMBERS_LIST = [str(num) for num in range(0,10)]
    SYMBOLS_LIST = ['!','@','#','$','%','&','*','(',')']
    
        

    def savepassword(self,web,user,pasw):
        text_to_write = f"{web}  |  {user}  |  {pasw}\n"
        with open('passwords.txt','a') as file:
            file.write(text_to_write)
    
    def readpassword(self):
        with open('passwords.txt','r') as file:
            pass_texts = file.readlines()
        text = "".join(pass_texts)
        return text
    
    def generate_pass_complex(self):
        final_password = []
        lower_letters = randint(4,6)
        upper_letters = randint(4,6)
        numbers = randint(2,4)
        symbols = randint(2,4)

        for i in range(lower_letters):
            final_password.append(choice(self.L_LETTERS_LIST))
            
        for i in range(upper_letters):
            final_password.append(choice(self.U_LETTERS_LIST))
        
        for i in range(numbers):
            final_password.append(choice(self.NUMBERS_LIST))
        
        for i in range(symbols):
            final_password.append(choice(self.SYMBOLS_LIST))
        shuffle(final_password)
        final_password = "".join(final_password)
        return final_password
    
    def generate_pass_numbers(self):
        final_pass =[choice(self.NUMBERS_LIST) for i in range(12)]
        final_pass = "".join(final_pass)
        return final_pass
    
    def generate_pass_letters(self):
        l_letters =[choice(self.L_LETTERS_LIST) for i in range(7)]
        u_letters = [choice(self.U_LETTERS_LIST) for i in range(7)]
        final_pass = l_letters + u_letters
        shuffle(final_pass)
        final_pass = "".join(final_pass)
        return final_pass
        
