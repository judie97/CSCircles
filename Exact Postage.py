def postalValidate(S):
    S = S.replace(" ", "")
    if len(S) == 6:
       digit = S[::-2]
       alpha = S[::2]
       if alpha.isalpha() and digit.isdigit():
           return S.upper()            
       else:
           return False
    else:
       return False
       
