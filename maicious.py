#!/python3

# DISCLAIMER - DON'T RUN ON YOUR COMPUTER YOUR DATA MAY BE DESTROYED #

#malicious.py - Removes every file from the C drive having extension `rxt`
import os
os.chdir('C:\\')
for file in os.listdir():
    if file.endswith('.rxt'):
        #os.unlink(file)
        
#Removes users folder
for folder in os.listdir():
    if folder == users:
        #os.rmdir(folder)
