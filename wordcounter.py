# def word_counter(*words,the_sentence):
#     counter = 0
#     display = {}
#     total_words = the_sentence
#     for word in words:
#         if word in total_words:
#            counter += 1
#            word_count = total_words.count(word)
#            print(f"{word} - {word_count}")
#            display[word] = word_count
#         else:
#             continue
#         if counter == 0:
#             print("the word is not in the sentence!")
#     return display

def word_counter(*words,the_sentence):
    counter = 0
    dict = {}
    splited = the_sentence.split(" ")
    print(splited)
  
    for word in splited:
        if "," in word:
            new_word = word.strip(",")
        splited.append(new_word)
    print(splited)

# chatgpt version
# def word_counter(the_sentence, *words):
#     word_count = {}  # Dictionary to store word counts
#     splited = the_sentence.replace(",", "").split(" ")  # Remove commas and split by spaces
#     print("Sentence split into words:", splited)
    
#     # Initialize the dictionary with the words we want to count
#     for word in words:
#         word_count[word] = splited.count(word)  # Count occurrences of each word
    
#     print("Word counts:", word_count)
#     return word_count

        
            
        
            
      
  
word_counter("mikedean","henry","aloh",the_sentence="henry, henry, is loved my mikedean, and there are very close")
 