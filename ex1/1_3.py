from crypto.cyphers.vigenere import vigenere_decrypt

string = 'evtdwdlgszfepllxdwpktevlgscjgszfevsjecdpsszkpyqcjdetcylboosncmaewzykzcypgsyhvpycyprzpgyzhsljpevpvsj'
key = 'lol'  # Credit: https://www.guballa.de/vigenere-solver

print(vigenere_decrypt(string, key))
