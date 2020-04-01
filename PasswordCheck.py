#A string is a valid password if it meets ALL the following
#conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   numbers, and punctuation. For punctuation, the following
#   punctuation marks are acceptable: !@#$%&()-_[]{};':",./<>?
# - It may not contain any characters that do not fit into the
#   four categories above. This includes any punctuation marks
#   not listed in the bullet point above, spaces, and any other
#   character.


#Add your code here!
def password_check(the_string) : 
    f_len = False
    if len(the_string) >= 8 :
        f_len = True
    for s in the_string :
        if ord(s) >= 65 and ord(s) <= 90 :
            f_cap = True
        if ord(s) >= 97 and ord(s) <= 122 :
            f_lower = True
        if s in ''''!@#$%&()-_[]{};':",./<>?''' :
            f_pun = True
        if ord(s) >= 48 and ord(s) <= 57 :
            f_num = True 
    if f_len and f_cap and f_lower and f_num and f_pun :
        return True
    else :
        return False
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))