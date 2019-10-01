import csv
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import math
nlp = spacy.load("en_core_web_sm")

def lower_case(text):
	text = text.lower()
	return text

def replace_numbers(words):
	p = inflect.engine()
	new_words = []
	for word in words:
		if word.isdigit():
			new_word = p.number_to_words(word)
			new_words.append(new_word)
		else:
			new_words.append(word)
	return new_words

def tokenization(text):               #Tokenization, POS Tagging
	doc = nlp(text)
	token = []
	for word in doc:
		token.append(word.text)
	return token

def stop_words_removal(token_list):      #Removal of stop words and punctuation
	filtered_sentence =[] 
	for word in token_list:
		lexeme = nlp.vocab[word[0]]
		if lexeme.is_stop == False and lexeme.is_punct == False:
			filtered_sentence.append(word) 
	return filtered_sentence

def html_tags(text):
	flag = False
	temp = ""
	for word in text:
		if(word=="<"):
			flag = True
		if(flag!=True):
			temp = temp+word
		if(word == ">"):
			flag = False
	return temp

def pre_processing(text):
	text = lower_case(text)
	text = html_tags(text)
	token = tokenization(text)
	token = stop_words_removal(token)
	return token

def create_freq_dict(text_token, pmid):
	freq = {}
	for word in text_token:
		freq[word] = freq.get(word,0) + 1
	freq2 = {'PMID':pmid,'freq_dict':freq}
	return freq2

def doc_word_freq(text):
	freq_list = []
	for i in range(len(text)):
		freq_list.append(create_freq_dict(text[i][3],text[i][1]))
	return freq_list

def TextDictionary(scrape):
	textDict = {}
	for i in range(len(scrape)):
		textDict[scrape[i][1]] = scrape[i][3]
	return textDict

def computeTF(text, freq_list):
	TF_scores = []
	for dictt in freq_list:
		id = dictt['PMID']
		for k in dictt['freq_dict']:
			temp = {'PMID':id, 'TF_score':dictt['freq_dict'][k]/len(textDict[id]), 'key':k}
			TF_scores.append(temp)
	return TF_scores

def computeIDF(text, freq_list):
	IDF_scores = []
	for dictt in freq_list:
		for k in dictt['freq_dict']:
			count = sum([k in tempDict['freq_dict'] for tempDict in freq_list])
			temp = {'PMID':dictt['PMID'], 'IDF_score': math.log(len(text)/count), 'key': k}
			IDF_scores.append(temp)
			break
	return IDF_scores

def computeTFIDF(TF_list,IDF_list):
	TFIDF_scores = []
	for j in IDF_list:
		for i in TF_list:
			if j['key']==i['key'] and j['PMID']==i['PMID']:
				temp = {'PMID':i['PMID'], 'TFIDF': j['IDF_score']*i['TF_score'] , 'key': i['key']}
				TFIDF_scores.append(temp)
				break
	return TFIDF_scores

scrape =[]
with open('result3.csv','rt') as f:
  data = csv.reader(f)
  result = open('preprocessing.csv','w',newline="")
  wr = csv.writer(result)
  first_row = next(data)
  for row in data:
    title = pre_processing(row[2])
    abstract = pre_processing(row[3])
    scrape.append([row[0],row[1],title,abstract]) 
    wr.writerows(scrape)
  result.close()
f.close()
temp = doc_word_freq(scrape)
textDict = TextDictionary(scrape)