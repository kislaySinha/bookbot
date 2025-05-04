


def count_words(filepath):
    file_content=""
    with open(filepath) as f:
        file_content = f.read()
    all_words=file_content.split()
    return len(all_words)

def count_chars(filepath):
    file_content=""
    with open(filepath) as f:
        file_content = f.read()
    
    char_dict={}
    for l in file_content:
        each_char = l.lower()
        if each_char in char_dict:
            char_dict[each_char]+=1
        else:
            char_dict[each_char]=1
    return char_dict

def sort_on(dict):
    return dict["num"]

def count_dict(char_dict):
    list_of_dicts=[]
    for key in char_dict:
        small_dict={}
        if key.isalpha():
            small_dict.update({"char": key, "num": char_dict[key]})
            list_of_dicts.append(small_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

        
