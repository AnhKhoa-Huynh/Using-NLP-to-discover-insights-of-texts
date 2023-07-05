from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

text = open("dorian_gray.txt",encoding='utf-8').read().lower()

# Sentence and word tokenize text 
word_tokenized_text = word_sentence_tokenize(text)

# store and print word tokenized sentence
single_word_tokenized_sentence = word_tokenized_text[69]
print(single_word_tokenized_sentence)
print('\n----------\n')

# Create a list to hold part-of-speech tagged sentences 
pos_tagged_text = []

for word_tokenized_sentence in word_tokenized_text:
  pos_tagged_text.append(pos_tag(word_tokenized_sentence))
single_pos_sentence = pos_tagged_text[100]
print(single_pos_sentence)
print('\n----------\n')
np_chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'
np_chunk_parser = RegexpParser(np_chunk_grammar)

vp_chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}'
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# Empty lists to hold the chunked sentences
np_chunked_text = []
vp_chunked_text = []

for chunked in pos_tagged_text:
  np_chunked_text.append(np_chunk_parser.parse(chunked))
  vp_chunked_text.append(vp_chunk_parser.parse(chunked))

# Analyze Chunks
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print('Most common NP chunks:\n', most_common_np_chunks, '\n')

most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print('Most common VP chunks:\n', most_common_vp_chunks, '\n')




