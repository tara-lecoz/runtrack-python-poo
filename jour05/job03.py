def nb_caractere(ch_caractere, caractere):
    n = ch_caractere[caractere]
    if n == ch_caractere[-1]:
        caractere += 1
        pass   
    else:
        caractere = nb_caractere(ch_caractere, caractere + 1)
    
    return caractere

print(nb_caractere("Hello", 0))