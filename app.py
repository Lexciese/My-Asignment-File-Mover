from __future__ import print_function, unicode_literals
# import cProfile
# import re
from PyInquirer import prompt
from pprint import pprint
from PyInquirer import prompt, Separator
import os
import time
import sys
# cProfile.run('re.compile("foo|bar")')



tiga = -3
empat = -4
lima = -5
enam = -6
tujuh = -7
delapan = -8
sembilan = -9


class Filename:
    formatF = "Falah Naufal Zaki(13)_X MIPA 4"
    src = []
    kosong = True
    same = True
    # default len from file extention
    ffile = -5


    def __init__(self):
        questions = [
            {
            'type': 'list',
            'name': 'class',
            'message': 'Choose Your Class',
            'default': 2,
            'choices': [
                'X MIPA',
                'XI MIPA',
                'XII MIPA'
            ]}]
        answers = prompt(questions)
        if answers['class'] == "X MIPA":
            self.src = ["C:/Users/ZAKI/Google Drive/High School/X MIPA/TMP/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/If not, maybe in here/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Bahasa/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Biologi/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/English/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Fisika/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Geografi/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Jawa/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Kimia/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/MTK Minat/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/MTK Wajib/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/PAI/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/PJOK/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/PPKn/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Pramuka/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Sejarah/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Senbud/", 
            "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Sosiologi/"]
            print('aye')

        elif answers['class'] == "XI MIPA":
            self.src = ["C:/Users/ZAKI/Google Drive/High School/XI MIPA/TMP/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/If not, maybe in here/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Bahasa/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Biologi/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/English/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Fisika/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Geografi/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Jawa/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Kimia/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/MTK Minat/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/MTK Wajib/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/PAI/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/PJOK/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/PPKn/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Pramuka/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Sejarah/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Senbud/", 
            "C:/Users/ZAKI/Google Drive/High School/XI MIPA/TUGAS/Sosiologi/"]

        elif answers['class'] == "XII MIPA":
            self.src = ["C:/Users/ZAKI/Google Drive/High School/XII MIPA/TMP/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/If not, maybe in here/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Bahasa/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Biologi/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/English/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Fisika/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Geografi/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Jawa/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Kimia/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/MTK Minat/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/MTK Wajib/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/PAI/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/PJOK/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/PPKn/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Pramuka/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Sejarah/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Senbud/", 
            "C:/Users/ZAKI/Google Drive/High School/XII MIPA/TUGAS/Sosiologi/"]


    def checkFile(self):
        File = os.listdir(self.src[0])
        if len(File) == 0:
            print("-----Your TMP/ Directory is Empty-----\nTry to Put Something in It ^_^\nTry Again After You Did It!!\n")
            print("Exiting Progam in 5s")
            time.sleep(5)
            exit()
        else:
            self.kosong = False

        
    def isSame(self):
        for file in os.listdir(self.src[0]):
            print(file)
            if file[:30] != self.formatF: # To check if the file already named
                self.same = False

    
    def rename(self):
        for file in os.listdir(self.src[0]):
            print(file)
            # if file[:30] != self.formatF: # To check if the file already named
            # Rename all the Files
            os.rename(self.src[0] + file, self.src[0] + self.formatF + ' - ' + file)


    def redirect(self):
        # Iterate all the files from src Folder
        for file in os.listdir(self.src[0]):
            # print(file)
            # if file[:30] != self.formatF: # To check if the file already named
            # Rename all the Files
            # self.Nama = os.rename(self.src[0] + file, self.src[0] + self.formatF + ' - ' + file)

            x = 0
            y = os.listdir(self.src[0])[x]
            self.ffile = len(os.path.splitext(y)[-1]) * -1
            x += 1
            # print(os.listdir(self.src[0]))
            print(y)
            
            
            if y[enam + self.ffile: self.ffile] == "Bahasa":
                os.replace(self.src[0] + y, self.src[3] + y)
                print('Redirected')
            elif y[tujuh + self.ffile: self.ffile] == "Biologi":
                os.replace(self.src[0] + y, self.src[4] + y)
                print('Redirected')
            elif y[tujuh + self.ffile: self.ffile] == "English":
                os.replace(self.src[0] + y, self.src[5] + y)
                print('Redirected')
            elif y[enam + self.ffile: self.ffile] == "Fisika":
                os.replace(self.src[0] + y, self.src[6] + y)
                print('Redirected')
            elif y[delapan + self.ffile: self.ffile] == "Geografi":
                os.replace(self.src[0] + y, self.src[7] + y)
                print('Redirected')
            elif y[empat + self.ffile: self.ffile] == "Jawa":
                os.replace(self.src[0] + y, self.src[8] + y)
                print('Redirected')
            elif y[lima + self.ffile: self.ffile] == "Kimia":
                os.replace(self.src[0] + y, self.src[9] + y)
                print('Redirected')
            elif y[sembilan + self.ffile: self.ffile] == "MTK Minat":
                os.replace(self.src[0] + y, self.src[10] + y)
                print('Redirected')
            elif y[sembilan + self.ffile: self.ffile] == "MTK Wajib":
                os.replace(self.src[0] + y, self.src[11] + y)
                print('Redirected')
            elif y[tiga + self.ffile: self.ffile] == "PAI":
                os.replace(self.src[0] + y, self.src[12] + y)
                print('Redirected')
            elif y[empat + self.ffile: self.ffile] == "PJOK":
                os.replace(self.src[0] + y, self.src[13] + y)
                print('Redirected')
            elif y[empat + self.ffile: self.ffile] == "PPKn":
                os.replace(self.src[0] + y, self.src[14] + y)
                print('Redirected')
            elif y[tujuh + self.ffile: self.ffile] == "Pramuka":
                os.replace(self.src[0] + y, self.src[15] + y)
                print('Redirected')
            elif y[tujuh + self.ffile: self.ffile] == "Sejarah":
                os.replace(self.src[0] + y, self.src[16] + y)
                print('Redirected')
            elif y[enam + self.ffile: self.ffile] == "Senbud":
                os.replace(self.src[0] + y, self.src[17] + y)
                print('Redirected')
            elif y[sembilan + self.ffile: self.ffile] == "Sosiologi":
                os.replace(self.src[0] + y, self.src[18] + y)
                print('Redirected')
            else:
                os.replace(self.src[0] + y, self.src[2] + y)
                print('Redirected to "If not, maybe in here" folder')

    def StartRedirect(self):

        self.checkFile()
        self.isSame()
        
        if self.kosong == True:
            pass # SUDAH di handle sama checkFile()
        elif self.same == True and self.kosong == False:
            print(f"Found {str(len(os.listdir(self.src[0])))} Item/s")
            question = [
                {
                    'type' : 'confirm',
                    'message' : 'Do you want to redirecting your Assignment?',
                    'name' : 'Confirm',
                    'default' : True
                }]
            Confirm = prompt(question)
            if Confirm['Confirm'] == True:
                self.redirect()
                time.sleep(2)
                print("Completed...")
                time.sleep(3)

            else:
                question1 = [
                {
                    'type' : 'confirm',
                    'message' : 'Try Again',
                    'name' : 'Confirm',
                    'default' : True
                }]
                Confirm = prompt(question)
                if Confirm['Confirm'] == True:
                    self.StartRedirect()
                else:
                    print("Good bye!!!")
                    time.sleep(5)
                    exit()

        elif self.same == False and self.kosong == False:
            print(f"Found {str(len(os.listdir(self.src[0])))} Item/s")
            question = [
                {
                    'type' : 'confirm',
                    'message' : 'Do you want to redirecting your Assignment?',
                    'name' : 'Confirm',
                    'default' : True
                }
            ]
            Confirm = prompt(question)
            # Confirm = input("Do you want to redirecting your Assignment :\nPress Y/N to Confirm - ").lower()

            if Confirm['Confirm'] == True:
                self.rename()
                self.redirect()
                time.sleep(2)
                print("Completed...")
                time.sleep(3)
            else:
                question1 = [
                {
                    'type' : 'confirm',
                    'message' : 'Try Again',
                    'name' : 'Confirm',
                    'default' : True
                }]
                Confirm = prompt(question)
                if Confirm['Confirm'] == True:
                    self.StartRedirect()
                else:
                    print("Good bye!!!")
                    time.sleep(5)
                    exit()



Redirect = Filename()
Redirect.StartRedirect()
