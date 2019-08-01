## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #8 - DATA OBJECTS CREATE
## FUNCTION () #8 - DATA OBJECTS CREATE
## FUNCTION () #8 - DATA OBJECTS CREATE

def fn_DataObjectsCreate(D):
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #8 - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES      
    DL = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES 
    D5 = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES  
    L = [] ## EMPTY LIST TO HOLD LIST OF LETTERS
    ## LengthOfVerse = [] ## EMPTY LIST TO HOLD LENGTH OF EACH STRING IN EACH VERSE
    VerseLetterCounter = 1
    TotalLetterCounter = 1
    
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "D"...
    for key, each in D.items():
        
        ## COUNT LENGTH OF STRING, i.e. HOW MANY LETTERS IN EACH STRING
        LengthOfString = len(each)
        print("Key = ", key)
        print("LengthOfVerse = ", LengthOfString)
        print(each)
        
        ## FOR EACH LETTER IN STRING/VERSE...
        for letter in each:
            
            ## CREATE LIST OF LETTERS
            L.append(letter)
            #print(letter) ## COMPUTATION INTENSIVE
            
            ## EXPAND TUPLE KEY
            key4 = key + (VerseLetterCounter,)
            #print(t) ## COMPUTATION INTENSIVE
            
            ## CREATE DICTIONARY OF LETTERS - 4-DIGIT TUPLE-KEY
            DL[key4] = letter
            
            ## EXPAND TUPLE KEY
            key5 = key + (VerseLetterCounter, TotalLetterCounter,)
            
            ## CREATE DICTIONARY OF LETTERS - 5-DIGIT TUPLE-KEY
            D5[key5] = letter
            
            ## INCREASE LETTER COUNTER
            TotalLetterCounter += 1
            
            ## INCREASE VERSE COUNTER
            VerseLetterCounter += 1
        
        ## RESET VERSE LETTER COUNTER BACK TO 1       
        VerseLetterCounter = 1
        
        ## APPEND LENGTH OF STRING TO LIST OF STRING-LENGTHS
        #LengthOfVerse.append(LengthOfString)
            
            
    ## CREATE STRING-SEQUENCE OF LETTERS FROM LIST OF LETTERS    
    S = ''.join(L)    

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #8 - DATA OBJECTS CREATE")

    ## RETURN VARIABLES TO PROGRAM
    ## RETURN TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS, DICTIONARY OF LETTERS)
    return(S, L, DL, D5)

## END FUNCTION () #8 - DATA OBJECTS CREATE
## END FUNCTION () #8 - DATA OBJECTS CREATE
## END FUNCTION () #8 - DATA OBJECTS CREATE
