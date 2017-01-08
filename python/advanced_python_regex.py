faculty_dict = dict()
email_list = []
domain_list = []
fin=open('Preff.txt')
line=fin.readline() # skip the headers
for line in fin:
    word=line.strip() # remove EOL character
    base_list = word.split(',') # split csv line and place in list
    # extract degree, remove blanks and '.'
    degree=base_list[1].strip().translate(None,'.')
    # extract faculty
    faculty_tup=base_list[2].strip().partition(' of ')
    faculty_2=faculty_tup[0]
    faculty_tup2=faculty_2.partition(' is ')
    faculty=faculty_tup2[0]
    # extract email ids and add to list
    email_list.append(base_list[3])
    # extract unique email domains and add to list
    domain_tup=base_list[3].strip().partition('@')

    if domain_tup[2] not in domain_list:
        domain_list.append(domain_tup[2])
        
    # build degree dictionary       
    if degree not in degree_dict:
        degree_dict[degree]=1
    else:
        degree_dict[degree] +=1

    # build faculty dictionary
    if faculty not in faculty_dict:
        faculty_dict[faculty]=1
    else:
        faculty_dict[faculty] +=1
        
print degree_dict
print faculty_dict
print email_list
print domain_list
