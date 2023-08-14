def remove_character_at_index(input_string, index):
    if index < 0 or index >= len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + input_string[index + 1:]

def replace_character_at_index(input_string, index, new_character):
    if index < 0 or index == len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + new_character + input_string[index + 1:]

def remove_footnotes(input_string):
    i = 0
    removeMode = False
    
    while i < len(input_string):

        i+=1

        if (i == len(input_string)): break
        if (input_string[i] == "["): removeMode = True
        if (input_string[i] == "]"): removeMode = False

        if (removeMode or input_string[i] == "]"):
            input_string = remove_character_at_index(input_string, i)
            i-=1

    return input_string

def capitalize_all(input_string):
    capitalized_string = ""
    for i in range(len(input_string)):
        capitalized_string += input_string[i].upper()
    return capitalized_string
 

def whitelist_symbols(input_string, whitelisted):
    cleaned_string = ""

    i=0
    while i < len(input_string):
        char = input_string[i]
        
        if char.isalnum() or char == " ":
            cleaned_string += char
        else:
            for j in range(len(whitelisted))  :
                if char == whitelisted[j]:
                    cleaned_string += char

        i += 1                

    return cleaned_string 




def remove_spaces_before(input_string, chars):
    cleaned_string = ""

    i=0
    while i < len(input_string) - 1:
        char = input_string[i]
        nextChar = input_string[i+1]
        
        added = False
        for j in range(len(chars)):

            if nextChar == chars[j]:
                if char == " ":
                   added = True
                else:
                    cleaned_string += char
                    added = True

        if not added:
            cleaned_string += char    


        i += 1                

    return cleaned_string 




def remove_space_duplicates(input_string, spaceChar):
    wasAlphaNumeric = False
    cleaned_string = ""

    i=0
    while i < len(input_string):
        char = input_string[i]

        if char != spaceChar:
            wasAlphaNumeric = True
            cleaned_string += char
        else:
            if wasAlphaNumeric:
                cleaned_string += char
                wasAlphaNumeric = False

        i += 1

    # last character cannot be a space
    if (cleaned_string[len(cleaned_string)-1]==spaceChar):
        cleaned_string = cleaned_string[:-1]    

    return cleaned_string




def insert_spaces_between_numbers_and_words(input_string):

    cleaned_string = ""
    wasANumber = False

    i=0
    while i < len(input_string):
        char = input_string[i]

        if char.isnumeric():
            wasANumber = True
            cleaned_string += char

        else:
            if wasANumber and char != " ":
                # insert space
                cleaned_string+= " "

            cleaned_string += char
            wasANumber = False    

        i += 1

    return cleaned_string
