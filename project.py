import random
import re

a=('welcome in the coding or decoding' '\n')
print(a.upper())
coding=int(input('FOR CODING PRESS 1 AND FOR DECODING PRESS 2:' '\n'))
if coding==1:
    print('you choose coding')
    code=input('enter your text:')

    code1=code[::-1]
    f1='sopejfcfoojcoddfje'
    f2='thgorjvvkwkpe'
    f3=f1+f2
    length=12
    lord="".join(random.sample(f3, length))
    f4='ssdmmdocmspcdd'
    f5='dmspdemoeeoceo'
    f6=f4+f5
    length=12
    lord1="".join(random.sample(f6,length))
    add=(lord+code1+lord1)

    add2= add.split(" ")
    add3=[]
    dot_pos=0
    for l in add2:
        add3.append(add2[dot_pos])
        add3.append("°")
        
        dot_pos=dot_pos+1
    add4="".join(add3)

    symbol = ("= ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ = ≠ ≈ > < ≥ ≤ ^ & | ~ ! ? : ; , @ $ \' ` ∞ π Σ ∆ √ ∫ ∏ ∩ ⊂ ⊃ ⊆ ⊇ ؟ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﮖ ﮗ ﮘ ﮙ ﮚ ﮛ ﮜ ﮝ ﮞ ﮟ ﮠ ﮡ ﮢ ﮣ ﮥ ") 
    symb1= symbol.split(" ")
    symb_rand= random.sample(symb1,len(symb1))
    re=[]
    j=0
    for i in add4:
        re.append(i)
        re.append(symb_rand[j])
        j=j+1
    hht= "".join(re)
    print("\n",hht)

else:
    print('you choose decoding')
    gojo=input("enter your code to decode:")
    csd1=re.sub("[°]", "_", gojo)
    csd2=re.sub("[=≠≈><≥≤^&|~!?:;,@$\'`∞πΣ∆√∫∏∩⊂⊃⊆⊇؟ﮐﮑﮒﮓﮔﮕﮖﮗﮘﮙﮚﮛﮜﮝﮞﮟﮠﮡﮢﮣﮥ]","",csd1)
    reverse=(csd2[::-1])
    slicing=reverse[13:-12]
    print(slicing)

    



    
    
    


