def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = {}

    for ch in text:
        ch = ch.lower()
        if ch not in counts:
            counts[ch] = 0
        
        counts[ch] += 1
        
    return counts

def sort_on(items):
    return items["num"]

def sort_chars_dict(chars_dict):
    chars_dict_list = []
    
    for k, v in chars_dict.items():
        chars_dict_list.append({
            "char": k,
            "num": v,
        })
        
    chars_dict_list.sort(reverse=True, key=sort_on)
    return chars_dict_list
    