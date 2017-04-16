# Name: Maha Alidrisi
# This program convert singular words to plural

def plural(text):
    PluralText=""
    text= text.split()
    for word in text:
        if word.endswith(("ay","ey","iy","oy","uy")):
            PluralText= PluralText + word + "s "
        elif word.endswith("y"):
            word=word[:-1]
            PluralText= PluralText + word + "ies "
        elif word.endswith(("o","ch","s","sh","x","z")):
            PluralText= PluralText + word + "es "
        else:
            PluralText= PluralText + word + "s "             
    return PluralText


s = raw_input("Please enter your text! ")
print "\nThe plural form of your text is:", plural(s)

