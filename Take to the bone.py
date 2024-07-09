import sys
from time import sleep
 
def print_lyric(): 
    quotes = [
        ("There's your presence that grown", 0.07),
        ("Maybe I nurture it more", 0.12),
        ("By saying how I feel", 0.12),
        ("But I did mean it before", 0.11),
        ("I want you to the bone", 0.09),
        ("I want you to", 0.09),
        ("Take me home, I'm falling",0.10),
        ("Love me long, I,m rolling", 0.11),
        ("Losing control, body and soul", 0.09),
    ]
    
    jeda = [0.8,0.9,1,0.6,1,1.2,0.9,0.3,0.6,3]

    for i, (line, char_jeda) in enumerate(quotes):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        print('')
        sleep(jeda[i])

print_lyric()

