def largest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    
    return max(words, key=len)

if __name__ == "_main_":
    sentence = input("Enter a sentence: ")
    print("Largest word:", largest_word(sentence))