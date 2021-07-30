import string
import inflect
eng= inflect.engine()
from fuzzywuzzy import fuzz
import sys

def preprocess(text):
#     Change to lowercase
    text= text.lower()
    
#     Remove whitspace
    text= " ".join(text.split())
    
#     Remove punctuation
    text= text.translate(text.maketrans('','',string.punctuation)) 
    
#     Convert number to words
    token= text.split(" ")
    dummy= []
    
    for word in token:
        if word.isdigit():
            temp= eng.number_to_words(word)
            dummy.append(temp)
            
        else:
            dummy.append(word)
            
    text= ' '.join(dummy)
    
    return text
	
def similarity_score(text1, text2):

		return fuzz.token_set_ratio(text1, text2)
        
def main():
	txt1= sys.argv[1]
	txt2= sys.argv[2]
	
	print(txt1, txt2)
	
	txt1 = preprocess(txt1)
	txt2 = preprocess(txt2)
	
	print(txt1, txt2)
	
	print(similarity_score(txt1,txt2))
	
if __name__ == "__main__":
	
	main()