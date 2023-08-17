def remove_character_at_index(input_string, index):
    if index < 0 or index >= len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + input_string[index + 1:]

def replace_character_at_index(input_string, index, new_character):
    if index < 0 or index == len(input_string):
        raise ValueError("Index out of bounds")
    
    return input_string[:index] + new_character + input_string[index + 1:]

def remove_footnotes(input_string):
    result = []
    i = 0

    while i < len(input_string):
        if input_string[i] == "[":
            while i < len(input_string) and input_string[i] != "]":
                i += 1
        else:
            result.append(input_string[i])
        i += 1

    return ''.join(result)

def capitalize_all(input_string):
    return input_string.upper()
 

def whitelist_characters(input_string, whitelisted):
    cleaned_chars = [char for char in input_string if char in whitelisted]
    return ''.join(cleaned_chars)




def remove_spaces_before(input_string, chars):

    cleaned_chars = []

    i=0
    while i < len(input_string) - 1:
        char = input_string[i]
        nextChar = input_string[i+1]
        
        if not (char == " " and nextChar in chars):
            cleaned_chars.append(char)

        i += 1     

    cleaned_chars.append(input_string[len(input_string)-1])              
    return ''.join(cleaned_chars)


def remove_spaces_after(input_string, chars):
    cleaned_chars = []

    cleaned_chars.append(input_string[0])

    i=1
    while i < len(input_string) - 1:
        char = input_string[i]
        lastChar = input_string[i+-1]
        
        if not (char == " " and lastChar in chars):
            cleaned_chars.append(char)

        i += 1     

    cleaned_chars.append (input_string[len(input_string)-1])          
    return ''.join(cleaned_chars)


def remove_spaces_between_numbers(input_string):

    # include first character 
    cleaned_chars = []
    cleaned_chars.append(input_string[0])

    i=1
    while i < len(input_string) -1:
        lastChar = input_string[i-1]
        char = input_string[i]
        nextChar = input_string[i+1]

        if not (lastChar.isnumeric() and nextChar.isnumeric() and char == " "):
            cleaned_chars.append(char)

        i += 1   

    # include last character 
    cleaned_chars.append (input_string[len(input_string)-1])              
    return ''.join(cleaned_chars)




def remove_space_duplicates(input_string, spaceChar):
    cleaned_chars = []
    for char in input_string:
        if char != spaceChar:
            cleaned_chars.append(char)
        elif cleaned_chars and cleaned_chars[-1] != spaceChar:
            cleaned_chars.append(char)
    if cleaned_chars and cleaned_chars[-1] == spaceChar:
        cleaned_chars.pop()
    return ''.join(cleaned_chars)


def insert_spaces_between_numbers_and_words(input_string):

    cleaned_chars = []

    i=0
    while i < len(input_string) -1:

        char = input_string[i]
        nextChar = input_string[i+1]

        cleaned_chars.append(char)

        if (char.isnumeric() and nextChar.isalpha() or char.isalpha() and nextChar.isnumeric()):
            cleaned_chars.append(" ")


        i += 1

    # append last char
    cleaned_chars.append(input_string[len(input_string)-1])    

    return ''.join(cleaned_chars)



def insert_spaces_before(input_string, chars):
    
    cleaned_chars = []

    i=0
    while i < len(input_string) - 1:
        char = input_string[i]
        nextChar = input_string[i+1]
        
        cleaned_chars.append(char)

        if char != " " and nextChar in chars:
            cleaned_chars.append(" ")

        i += 1     

    cleaned_chars.append(input_string[len(input_string)-1])              
    return ''.join(cleaned_chars)



def insert_spaces_after(input_string, chars):
    
    cleaned_chars = []

    i=0
    while i < len(input_string) - 1:
        char = input_string[i]
        nextChar = input_string[i+1]
        
        cleaned_chars.append(char)

        if char in chars and nextChar != " ":
            cleaned_chars.append(" ")

        i += 1     

    cleaned_chars.append(input_string[len(input_string)-1])              
    return ''.join(cleaned_chars)


def remove_verse_numbers(input_text):
    output_text = ""
    current_verse = 0
    i = 0
    
    while i < len(input_text):
        if input_text[i].isdigit():
            verse_number = ""
            while i < len(input_text) and input_text[i].isdigit():
                verse_number += input_text[i]
                i += 1
            verse_number = int(verse_number)
            
            if verse_number == current_verse + 1:
                while i < len(input_text) and input_text[i].isdigit():
                    i += 1
                current_verse = verse_number
            else:
                output_text += str(verse_number)
        else:
            output_text += input_text[i]
            i += 1
    
    return output_text


def format_numbers_with_commas(input_string):

    cleaned_chars = []

    cleaned_chars.append(input_string[0])

    i=1
    while i < len(input_string) - 1:
        
        char = input_string[i]
        nextChar = input_string[i+1]
        lastChar = input_string[i+-1]
        
        if not(lastChar.isnumeric() and char == "," and nextChar.isnumeric()):
            cleaned_chars.append(char)


        i += 1  

    cleaned_chars.append(input_string[len(input_string)-1])                   
    return ''.join(cleaned_chars)

