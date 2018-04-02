#Implement Hamming Distance Algorithm

#Hamming Function

def hamming_dist(s1, s2):
    a=0
    if len(s1) != len(s2):
        raise ValueError("Provide equal lengh sequences")
    for ch1,ch2 in zip(s1,s2):
         if ch1!=ch2:
            if (s1.index(ch1))==0 and (s2.index(ch2))==0 and ch1.lower()==ch2.lower():
                a=0
            elif ch1.lower()==ch2 or ch2.lower()==ch1:
                a+=0.5
            elif ((ch1=='s' and ch2=='z') or (ch1=='z' and ch2=='s') or (ch1=='S' and ch2=='Z') or (ch1=='Z' and ch2=='S')):
                a+=0
            else:
                a+=1
                if (ch1.islower() and ch2.isupper()) or (ch2.islower() and ch1.isupper()):
                    a+=0.5
                else:
                    a+=0
    return a   


#Execution

hamming_dist("make","Mage")

hamming_dist("MaiSY","MaiZy")

hamming_dist("Eagle","Eager")

hamming_dist("Sentences work too.","Sentences wAke too.")

hamming_dist("data Science","Data Sciency")

hamming_dist("organizing","orGanising")

hamming_dist("AGPRklafsdyweIllIIgEnXuTggzF","AgpRkliFZdiweIllIIgENXUTygSF")


#Results

# First Word                                     Second Word                               Distance Score
# data Science                                   Data Sciency                                   1
# organizing                                     orGanising                                    0.5
# AGPRklafsdyweIllIIgEnXuTggzF                   AgpRkliFZdiweIllIIgENXUTygSF                  8.5
# 
 
