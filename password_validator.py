
from colorama import Fore, Back, Style
import sys

def password_lengthcheck(passwd:str) -> None :
    """
    function checks the lenght of the password - the password should include minimum of 10 characters. 
    for example if password is "123" it will give error massage 
    :param passwd: str example - > "MyP@ssw0rd!"
    :return: None
    """
    global val
    if len(passwd) < 10 :
        print(Fore.RED +'length should be at least 10 characters')
        val = 1
        
    else:
        val = 0
def password_digitcheck(passwd:str) -> None:
    """
    function checks that the password at least 1 number. 
    for example if password is "mypaSSword1" it will give error massage 
    :param passwd: str example - > "MyP@ssw0rd!1"
    :return: None
    """ 
    global val1    
    if not any(char.isdigit() for char in passwd):
        print(Fore.RED + 'Password should have at least one number')
        val1 = 1
    else:
        val1 = 0
def password_uppercheck(passwd:str) -> None:
    """
    function checks that the password at least 1 upper case letter. 
    for example if password is "mypassword1" it will give error massage 
    :param passwd: str example - > "MyP@ssw0rd!1"
    :return: val2 None
    """ 
    global val2        
    if not any(char.isupper() for char in passwd):
        print(Fore.RED + 'Password should have at least one capital letter')
        val2 = 1
    else:
        val2 = 0 
def password_lowercheck(passwd:str) -> None:
    """
    function checks that the password at least 1 lower case letter. 
    for example if password is "MYPASSWORD1" it will give error massage 
    :param passwd: str example - > "MyP@ssw0rd!1"
    :return: None
    """
    global val3          
    if not any(char.islower() for char in passwd):
        print(Fore.RED + 'Password should have at least one small letter')
        val3 = 1
    else:
        val3 = 0
def runcode(passwd) -> sys.exit : 
 """
    function checks the password 
    for example if password is "MYPAssWORD1" it print that the password is valid
    :param passwd: str example - > "MyP@ssw0rd!1"
    :return: sys.exit(0),sys.exit(1)
    """
 password_lengthcheck(passwd)
 password_digitcheck(passwd)
 password_uppercheck(passwd)
 password_lowercheck(passwd)
 if val == 0  and val1 ==0 and val2 == 0 and val3 == 0:
   print(Fore.GREEN + "Password is valid")
   return sys.exit(0)
 else:
    print(Fore.RED + "Password is not valid")
    return sys.exit(1)

def main():
 passwd = sys.argv[1]
 print(runcode(passwd))
 
             
if __name__ == '__main__':
    main()