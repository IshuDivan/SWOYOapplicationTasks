 
# "A word" we define for the purpose of this exercise as a string of only kirillic and/or latin letters(numbers don't count as letters). 
# All letters will be stored as non-capitalized. Request vocab['A'] wouldn't work, only vocab['a']. The reason is aestetics


import os
def in_russian_alphabet(s):
    alphabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    flag=False
    for i in alphabet:
        if i==s:
            flag=True
    return flag
def in_english_alphabet(s):
    alphabet="abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
    flag=False
    for i in alphabet:
        if i==s:
            flag=True
    return flag
def make_it_index(c):
    smal1="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in range(len(smal1)):
        if c==smal1[i]:
            return smal1[i]
    big1="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in range(len(smal1)):
        if c==big1[i]:
            return smal1[i]
    smal2="abcdefghijklmnopqrstuwxyz"
    for i in range(len(smal2)):
        if c==smal2[i]:
            return smal2[i]
    big2="ABCDEFGHIJKLMNOPQRSTUWXYZ"
    for i in range(len(smal2)):
        if c==big2[i]:
            return smal2[i]


def text_stat(filename):
    if(not(os.path.isfile(filename))):
        return {"error":"File with such name does not exist"}
    
    if(os.path.getsize(filename) <= 0):
        return {"error":"File is empty"}
    number_of_words=0
    paragraph_amount=1
    bilingual_word_amount=0
    truealphabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuwxyz"
    flag_for_letters = {l: 0 for i, l in enumerate(truealphabet)}
    frequency_of_letters = {l: 0 for i, l in enumerate(truealphabet)} 
    number_of_letters = {l: 0 for i, l in enumerate(truealphabet)} 
    
    txt = open(filename, "r", encoding='utf-8')
    not_empty_paragraph_flag=0
    current_char='a'
    current_state=0
#    current_word=""
    while(current_char!=''):
        current_char=txt.read(1)
        if(current_char!='\n')and(current_char!=' '):
            not_empty_paragraph_flag=1
        if(current_char=='\n'):
            if(not_empty_paragraph_flag==1):
                paragraph_amount+=1
            not_empty_paragraph_flag=0

        if(current_state==0):
            russian_flag=0
            english_flag=0
#            current_word=""

            if(in_russian_alphabet(current_char))or(in_english_alphabet(current_char)):
                for i in flag_for_letters:
                    flag_for_letters[i]=0
                current_state=1
#                current_word+=current_char

                flag_for_letters[make_it_index(current_char)]=1
                number_of_letters[make_it_index(current_char)]+=1

                if(in_russian_alphabet(current_char)):
                    russian_flag=1
                if(in_english_alphabet(current_char)):
                    english_flag=1

        elif(current_state==1):
            if(in_russian_alphabet(current_char))or(in_english_alphabet(current_char)):

                flag_for_letters[make_it_index(current_char)]=1
                number_of_letters[make_it_index(current_char)]+=1
#                current_word+=current_char

                if(in_russian_alphabet(current_char)):
                    russian_flag=1
                if(in_english_alphabet(current_char)):
                    english_flag=1
            else:
                current_state=0
                for i in flag_for_letters:
                    if(flag_for_letters[i]==1):
                        frequency_of_letters[i]+=1
                if(english_flag==1)and(russian_flag==1):
                    bilingual_word_amount+=1
                number_of_words+=1
#                print(current_word)
    for i in frequency_of_letters:
        if(number_of_words>0):
            frequency_of_letters[i]=frequency_of_letters[i]/number_of_words
        else:
            frequency_of_letters[i]=0
    final_vocabulary={}


    final_vocabulary['word_amount']=number_of_words
    final_vocabulary['paragraph_amount']=paragraph_amount
    final_vocabulary['bilingual_word_amount']=bilingual_word_amount
    
    for i in frequency_of_letters:
        final_vocabulary[i]=(number_of_letters[i],frequency_of_letters[i])

    return final_vocabulary
        
    
vocab=text_stat('text.txt')
print(vocab)
