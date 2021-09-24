import os
import random

def OpenData(filepath):
    Data=[]
    with open(filepath,"r",encoding="UTF-8") as f:
        for line in f:
            Data.append(line.strip().upper())
    return Data

def run():
    data=OpenData("./archivo/data.txt")
    chosen_word=random.choice(data) ##Escoge una palabra al azar de data
    chosen_word_list=[letter for letter in chosen_word]
    chosen_word_list_underscores=["_"] * len(chosen_word_list)
    
    
    letter_index_dict={}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter]=[]
        letter_index_dict[letter].append(idx)
    while True:
        os.system("cls")
        print("Adivina la palabra")
        for element in chosen_word_list_underscores:
            print(element+"",end="")
        print("\n")
        letter=input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(),"Solo puede ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx]=letter

        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("Ganastes la palabra era", chosen_word)
            break

if __name__=='__main__':
    run()
