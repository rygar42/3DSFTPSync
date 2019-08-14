'''
Program to sync 3DS game saves to your PC
Files are copied over from FTP to a folder you control

'''
import os
import getpass


from ftplib import FTP

ftp = FTP()
ftp.connect('192.168.1.X', 5000)

ftp.login()               # user anonymous, passwd anonymous@

ftp.retrlines('LIST')     # list directory contents

#change directory to folder I care about

gamedir = "/roms/snes"
ftp.cwd(gamedir) #changing to /roms/snes

currentuser = getpass.getuser()

filenames = ftp.nlst()

for filename in filenames:

    file_name = filename

    file_name = file_name.replace(gamedir + "/","")

    if '.frz' in file_name or '.sav' in file_name or '.sfc' in file_name or '.srm' in file_name:
        #script_dir = os.path.dirname(os.path.abspath(__file__))
        dest_dir = '/users/' + currentuser + '/documents/3DS Backup/Save Games'
        try:
            os.makedirs(dest_dir)
        except OSError:
            pass  # already exists
        path = os.path.join(dest_dir, file_name)


        with open( path, 'wb' ) as file :
            ftp.retrbinary('RETR %s' % filename, file.write)

            file.close()

ftp.quit()