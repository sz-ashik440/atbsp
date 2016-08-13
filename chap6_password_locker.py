import sys, pyperclip

PASSWORDS = {'email':'AsHik440',
            'blog':'admin321',
            'log':'123456abcd'}
if len(sys.argv) < 2:
    print('Usage: python')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copited to clipboard.')
else:
    print('There is no account named '+ account)
