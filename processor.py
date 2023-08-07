def remove_character_at_index(input_string, index):
    if index < 0 or index >= len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + input_string[index + 1:]

def replace_character_at_index(input_string, index, new_character):
    if index < 0 or index >= len(input_string):
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
