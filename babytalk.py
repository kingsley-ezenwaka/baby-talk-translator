# babytalk.py (c) Kingsley Ezenwaka - k3z3nw4k4@gmail.com

from tkinter import *

# The translator function
def translate_to_baby(text):
    # Split input text into bits for parsing
    bits_of_text = text.split()

    # Initialize list to hold translated baby-talk strings
    baby_text = []

    # Loop through and split input text further to catch punctuations
    smaller_bits_of_text = []
    for bit in bits_of_text:
        smaller_bits = parts(bit) # 'ISNOTAWORD' is returned for text bits that contain only numbers & symbols 
        smaller_bits_of_text.append(smaller_bits)

    # Loop through the split text list and translate the words
    for smaller_bit in smaller_bits_of_text:
        
        if smaller_bit[1] == 'ISNOTAWORD':     # Non-alphabetic texts are ignored
            holder = smaller_bit[0] + [' ']

        else:                               # Words are extracted
            word = smaller_bit[1]

            # Parse the word through "baby-brain" functions
            baby_word = formatter(baby_brain(word.lower()), word)

            # Re-combine the word with the initial punctuations
            holder = smaller_bit[0] + [baby_word] + smaller_bit[2] + [' ']

        # Collapse the lists and join words into one continuous string
        for item in holder:
            baby_text.append(item)

    return ''.join(baby_text)

#-------------------------------------
# Baby_brain Translator Functions
#-------------------------------------
# Splits a string into words and punctuations
def parts(word):
    # Initialise lists for punctuations in front or back of word
    front_chars, back_chars = [], []

    # Check if 'word' contains alphabets (a-z, A-Z)
    if not any(c.isalpha() for c in word):
        front_chars = [word]
        word = 'ISNOTAWORD'

    else:
        # Search and capture punctions in front
        while not word[0].isalpha():
            front_chars.append(word[0])
            word = word[1:]

        # Search and capture punctions at back    
        while not word[-1].isalpha():
            back_chars.insert(0,word[-1])
            word = word[:-1]

    return [front_chars, word, back_chars]

# Takes a normal word and returns a "baby-fied" version
def baby_brain(word):
    # Return word unchanged if it is less 3 letters long
    if len(word) < 3:
        return word
    
    baby_common = {'mother':'mama', 'mum': 'mama', 'mom':'mama', 'father':'dada', 'dad':'dada', 
                   'child':'baby', 'brother':'bubba', 'sister':'sissy', 'grandmother':'nana', 
                   'bottom':'bum-bum', 'buttocks':'bum-bum', 'butt':'bum-bum',
                   'grandma':'nana', 'grandfather':'papa', 'granddad':'pa', 'food':'num-num', 
                   'urinate':'pee-pee', 'stomach':'tummy', 'toilet':'poo-poo', 'urinated':'pee-pee',
                   'shit':'poo-poo', 'poop': 'poo-poo', 'pooped':'poo-poo', 'dog':'doggy', 'cat':'kitty', 
                   'horse':'horsie',} # Feel free to add more common baby words

    pain_words = ['injury', 'injured', 'wound', 'wounded', 'hurt', 'bruised', 'bruise', 'gash']
    
    bad_words = ['casualty', 'accident', 'disaster', 'catastrophe', 'mishap',
                 'tragedy', 'mischance', 'misfortune', 'collision', 'crash',
                 'calamity', 'wreck', 'misadventure', 'cataclysm', 'smashup',
                 'deathblow']

    # Checks word against common baby versions            
    if word in baby_common:
        return baby_common[word]
    elif word in pain_words:
        return 'boo-boo'
    elif word in bad_words:
        return 'bada-boo-boo'

    # If word has no common baby versions, run the word
    # Through character switching functions to imitate baby-speech
    else:
        bword = word
        bword = switch_tt(bword)
        bword = switch(bword, 'cks', 'k')
        bword = switch(bword, 'tion', 'shun')
        bword = switch(bword, 'ny', 'mie')
        bword = switch(bword, 'q', 'w')
        bword = switch(bword, 'eou', 'o')
        bword = switch(bword, 'x', 's')
        bword = switch(bword, 'ry', 'wy')
        bword = switch(bword, 'ly', 'wy')
        bword = switch(bword, 'll', 'ww')
        bword = switch(bword, 'rr', 'ww')
        bword = switch_mix(bword)
    
    return bword

# Switches given characters in a string
def switch(string, chars, nchars):
    if chars in string:
        string = string.replace(chars,nchars)
    return string

# Character switching function
# Imitates mispronounciation of words with 'tt' or 'th'
def switch_tt(word):
    if word == 'the':
        return 've'
    
    elif word[:2] == 'th':
        return 'd' + word[2:]
           
    if 'tt' in word and word.index('tt') == 2 and word[0] in 'cfkpr':
        swap = word[0]
        bword = 't' + word[1] + (swap*2) + word[4:]

    elif word[-2:] == 'th':
        bword = word[:-1]
        
    else:
        bword = word

    return bword

# Another character switching function
# Imitates mispronounciation of some words with 'l','r','s'
def switch_mix(word):
    bword = list(word)
    if bword[0] in ['r', 'l']:
        bword[0] = 'w'

    if bword[1] in ['r']:
        bword[1] = 'w'

    if bword[0] == 's' and bword[1] in 'bcdfgkpqt':
        bword.pop(0)
    
    for i in range(1,len(bword)-1):
        if bword[i] == 'r' and len(bword) > 5:
            bword[i] = 'w'

        if bword[i] == 'l':
            bword[i] = 'w'

    for i in range(1,len(bword)):
        if bword[i] == 'v' and bword[i+1] in 'aeiouy':
            bword[i] = 'b'

    if word[-2:] == 'le' and bword[-2] == 'w':
        bword[-2] = 'l'

    bword = ''.join(bword)

    return bword

# Formats the translated baby-word with reference to original word
def formatter(word, ref_word):
    # Check if reference word is all caps
    if len(ref_word) > 1 and ref_word[1].isupper():
        word = word.upper()
    
    # Check if reference word is title case
    elif ref_word[0].isupper():
        word = word[0].upper() + word[1:]
        #word = word[:2] + word[2:-2].lower() + word[-2:].lower()

    # If none of above conditions met, then word is lower case
    return word

#-------------------------------------
# GUI functions
#-------------------------------------
# Controller function to interface between the GUI and backend translator functions
def translate_controller(source_txt_wdg, target_txt_wdg):
    # Enable the baby-talk text display and clear previous content
    target_txt_wdg.configure(state='normal')
    target_txt_wdg.delete('1.0', 'end')
    
    # Get the source English text to be translated
    lines_of_text =  source_txt_wdg.get('1.0', 'end').split('\n')

    # Translate source text to baby-talk line by line
    for line in lines_of_text:
        baby_talk = translate_to_baby(line)
        target_txt_wdg.insert('end', baby_talk + '\n')

    # Set the baby-talk text display state back to disabled
    target_txt_wdg.configure(state='disabled')    

# Clear the text displays in the GUI
def clear(list_of_normal_wdgs, list_of_disabled_wdgs):
    # Clear for normal textboxes (i.e. state not disabled)
    for wdg in list_of_normal_wdgs:
        wdg.delete('1.0', 'end')

    # Clear for textboxes with disabled state
    for wdg in list_of_disabled_wdgs:
        wdg.configure(state='normal')
        wdg.delete('1.0', 'end')
        wdg.configure(state='disabled')

# Main function, wraps a tkinter GUI around the translator functions
def main():
    # Create root window
    root = Tk()
    root.title("English to Baby-talk Translator")
    
    # Main windown to hold GUI widgets
    mainframe = Frame(root, relief=FLAT, borderwidth=1)
    mainframe.grid(row = 0, column = 0, padx = 8, pady = 8)

    # Label widget
    lbl = Label(mainframe, text='Enter text here:')
    lbl.grid(row=0, column=0)

    # Textbox to receive the input text
    input_textbox = Text(mainframe, width=80, height=10, wrap='word', 
                         relief=SUNKEN, borderwidth=1)
    input_textbox.grid(row=1,column=0)
    # Scrollbar for input textbox   
    in_yscrollbar = Scrollbar(mainframe, orient = 'vertical', 
                             command = input_textbox.yview)
    input_textbox['yscrollcommand'] = in_yscrollbar.set
    in_yscrollbar.grid(row=1, column=1, sticky = 'ns')

    # Button widget (within 'trs_btnframe' window) to activate the translator function
    trs_btnframe = Frame(mainframe, relief=FLAT)
    trs_btnframe.grid(row=2, column=0, pady=4)
    translate_btn = Button(trs_btnframe, text='Translate to Baby-talk', 
                           command= lambda: translate_controller(input_textbox, output_textbox))
    translate_btn.grid()

    # Text widget to display the translated baby speech
    output_textbox = Text(mainframe, state='disabled', width=80, height=15, wrap='word', 
                      relief=SUNKEN, borderwidth=1)
    output_textbox.grid(row=3,column=0)
    # Scrollbar for output textbox   
    out_yscrollbar = Scrollbar(mainframe, orient = 'vertical', 
                             command = output_textbox.yview)
    output_textbox['yscrollcommand'] = out_yscrollbar.set
    out_yscrollbar.grid(row=3, column=1, sticky='ns')

    # Clear button widget (within clr_btnframe) to clear contents of text widgets
    clr_btnframe = Frame(mainframe, relief=FLAT)
    clr_btnframe.grid(row=4, column=0, pady=6)
    clr_btn = Button(clr_btnframe, width=10, text='Clear', 
                     command= lambda: clear([input_textbox], [output_textbox]))
    clr_btn.grid()
    #exit = Button(clr_btnframe, text='Exit')
    #exit.grid()
    
    # Run GUI loop
    root.mainloop()

# Run the program
main()