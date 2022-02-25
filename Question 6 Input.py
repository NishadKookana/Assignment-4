#Question 6

#Here we use anagrams

def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Give George's word= ")
Possible_words=anagram(George_word)
Barbie_word=input("Give Barbie's guess= ")
print("Possible Words-",Possible_words)

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")
