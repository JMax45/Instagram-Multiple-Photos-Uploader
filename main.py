from instapy_cli import client
from os import listdir
from os.path import isfile, join
import time

#login
username = 'username'
password = 'password'

#file da caricare
onlyfiles = [f for f in listdir
             ("files_to_upload") if isfile(join("files_to_upload", f))]
length_code_list2 = len(onlyfiles)
print(length_code_list2)

quantity = 0

with client(username, password) as cli:
    while quantity < length_code_list2:
        file_da_caricare = ("files_to_upload/" + onlyfiles[quantity])
        info_file1 = str(quantity+1)
        info_quantity = str(length_code_list2)
        info_file2 = ("["+info_file1+"/"+info_quantity+"] "+file_da_caricare)
        print(info_file2)
        time.sleep(1)
        cli.upload(file_da_caricare)
        quantity += 1
