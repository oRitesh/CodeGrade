# Lees deze code en volg wat het doet
def i_understand_the_following_code(user_input: str) -> bool:
    if user_input.lower() == 'yes' or user_input.lower() == 'ja':
        return True
    else:
        return False
    
def i_have_installed_vscode(user_input: str) -> bool:
    if user_input.lower() == 'yes' or user_input.lower() == 'ja':
        return True
    else:
        return False
    
def i_installed_handy_extensions(user_input: str) -> bool:
    if user_input.lower() == 'yes' or user_input.lower() == 'ja':
        return True
    else:
        return False
    
if not i_understand_the_following_code(input('Begrijp je het lezen van deze code?')):
    # Dan loop je nog conceptueel een beetje achter. Kijk nog een keer goed door Week 2 Step 01 en Step 02
    print("Booleans and conditionals are still difficult")
else:
    print("Theory of booleans and branching programs is already here") # Dan beheers je conditionals en de basics van functions

if i_have_installed_vscode(input('Heb je VSC al geïnstalleerd?')):
    print('Lekker gewerkt') # Lekker bezig!
else:
    print("google (Installing visual studio code for python)") # Nog ff doen dan.