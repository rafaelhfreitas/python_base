def repeat_vogal(word):
    """Returns the word with vogals repetead"""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâêôéáíó":
            final_word += letter * 2
        else:
            final_word += letter
    return final_word


print(repeat_vogal("banana"))


# Mudar a biblioteca de debuging do SO
# export PYTHONBREAKPOINT=ipdb.set_trace                 
