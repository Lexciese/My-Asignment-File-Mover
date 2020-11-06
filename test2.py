import os

p = "C:/Users/ZAKI/Google Drive/High School/X MIPA/TUGAS/Bahasa/Falah Naufal Zaki(13)_X MIPA 4 - eswfswedg - Bahasa.txt"
Bahasa = -6



print(p[Bahasa-4:-4])
print(len(os.path.splitext(p)[-1]))

if p[Bahasa-5:-5] == "Bahasa" or p[Bahasa-4:-4] == "Bahasa":
    print('Redirected')

