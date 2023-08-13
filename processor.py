def remove_character_at_index(input_string, index):
    if index < 0 or index >= len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + input_string[index + 1:]

def replace_character_at_index(input_string, index, new_character):
    if index < 0 or index == len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + new_character + input_string[index + 1:]

def remove_footnote_brackets(input_string):
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