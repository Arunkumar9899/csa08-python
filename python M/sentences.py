def remove_commom_words(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    unique_words1 = set(words1)
    unique_words2 = set(words2)
    unique_s1 = ' '.join(word for word in words1 if word not in unique_words2)
    unique_s2 = ' '.join(word for word in words2 if word not in unique_words1)
    return unique_s1, unique_s2
sentence1 = input("enter the first sentence: ")
sentence2 = input("enter the second sentance: ")

    
