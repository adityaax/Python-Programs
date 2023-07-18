# Insecure password manager-
import sys
import pyperclip
manager={'Bob':'password1',
         'Alice':'password2',
         'kite':'password3'}

account=input('enter your account: ')
if account in manager:
    pyperclip.copy(manager[account])
    print('Password is copied to clipboard')
else:
    print('No account found with the name' +account)


# Insecure password manager with command line arguments-
'''
account=sys.argv[1]
if account in manager:
    pyperclip.copy(manager[account])
    print('Password is copied to clipboard')
else:
    print('No account found with the name' +account)
'''
