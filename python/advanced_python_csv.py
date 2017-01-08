email_list = []
fin=open('Preff.txt')
fout = open('emails.csv','w')
line=fin.readline() # skip the headers
for line in fin:
    word=line.strip() # remove EOL character
    base_list = word.split(',') # split csv line and place in list
    email=base_list[3]

    fout.write(email)
    fout.write("\n")
    
fin.close()
fout.close()
