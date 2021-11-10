
WORDS_BANK = []

def load_Data() :
    with open("words_bank.txt" , 'r') as f: 
        big_text = f.read()
        words = big_text.split('\n')
    
    for i in range(0, len(words), 2) :
        WORDS_BANK.append({'english' : words[i] , 'persian' : words[i+1]})       

def Save_new_word():
    new_eng_word = input("type english word to add new word")
    new_fa_word = input("type farsi word to add new word")
    WORDS_BANK.append({'english' : new_eng_word , 'persian' : new_fa_word})
    f = open('words_bank.txt', 'w')
    f.write(WORDS_BANK)       
    
def Translate_En2fa():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['english']:
                output_text += word['persian'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text)    
    
    
def Translate_Fa2en():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['persian']:
                output_text += word['english'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text)    

        
    
load_Data()        
while True:
    print('1.Translate English to Persian')
    print('2.Translate Persian to English')
    print('3.Add new words ')
    print('4.exit')
    choice= input('Enter a number from menu: ')
    if choice == '1' :
        Translate_En2fa()
    elif choice == '2': 
        Translate_Fa2en()
    elif choice == '3' :
        Save_new_word()
    elif choice == '4': 
        exit()
    else:
        print('command not found')

        