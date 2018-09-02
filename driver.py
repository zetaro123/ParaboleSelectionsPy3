import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer



def get_subject_from_sentence(sentence):
	words = word_tokenize(str(sentence))
	string = ""
	for i in range (0,len(words)):
		list1 = nltk.pos_tag(nltk.word_tokenize(words[i]))
		if(list1[0][1] != 'VBZ' and list1[0][1] != 'NNS' ):
			string = string + words[i] + " "
		else:
			break
	return string



def get_object_from_sentence(sentence):
	words = word_tokenize(str(sentence))
	length = len(words)
	if length != 0:
		return words[length-2]
	else:
		return ""


def  get_verb_from_sentence(sentence):
	words = word_tokenize(str(sentence))
	string = ""
	for term in words:
		list1 = nltk.pos_tag(nltk.word_tokenize(term))
		if(list1[0][1] == 'VBZ' or list1[0][1] == 'NNS' or list1[0][1] == 'IN'):
			string = string + term + " "
	return string



def get_subject_from_sentences(list_of_sentences):
	list_subject = []
	for sentence in list_of_sentences:
		words = word_tokenize(str(sentence))
		string = ""
		for i in range (0,len(words)):
			list1 = nltk.pos_tag(nltk.word_tokenize(words[i]))
			if(list1[0][1] != 'VBZ' and list1[0][1] != 'NNS' ):
				string = string + words[i] + " "
			else:
				break;
		list_subject.append(string)
				

	return list_subject


def get_object_from_sentences(list_of_sentences):
	list_object = []
	#list_subject = get_subject_from_sentences(list_of_sentences)
	for sentence in list_of_sentences:
		words = word_tokenize(str(sentence))
		length = len(words)
		if length != 0:
			if words[length-2] not in list_object:
				list_object.append(words[length-2])
	return list_object



def get_verb_part_from_sentences(list_of_sentences):
	list_subject = get_subject_from_sentences(list_of_sentences)
	list_object = get_object_from_sentences(list_of_sentences)
	list_verbs = []
	for sentence in list_of_sentences:
		string = ""
		words = word_tokenize(str(sentence))
		for term in words:
			list1 = nltk.pos_tag(nltk.word_tokenize(term))
			if(list1[0][1] == 'VBZ' or list1[0][1] == 'NNS' or list1[0][1] == 'IN'):
				string = string + term + " "
		if(string not in list_verbs):
			list_verbs.append(string)
	return list_verbs



def different_conclusions_from_sentences(list_sentences, list_subject, list_object, list_verb):
	my_file = open(input_file,'w')
	answer = []
	for sentence in list_sentences:
		sub = get_subject_from_sentence(sentence)
		ver = get_verb_from_sentence(sentence)
		obj = get_object_from_sentence(sentence)
		answer.append([sub,ver,obj])

	for i in range(0,len(answer)):
		for j in range(0, len(answer)):
			if(answer[i][1] == answer[j][1] and i != j):
				a = [answer[j][0], answer[i][1], answer[i][2]]
				if(a not in answer):
					answer.append(a)

	for lst in answer:
		my_file.write(str(lst[0])+","+str(lst[1])+","+str(lst[2])+"\n")

	my_file.close()



input_sentences = []
subject_list = []
object_list = []
verb_list = []

print("Enter name of input text file: ")
input_file = str(input())

with open(input_file,'r') as my_file:
	input_sentences = [line.strip() for line in my_file]


subject_list = get_subject_from_sentences(input_sentences)
object_list = get_object_from_sentences(input_sentences)
verb_list = get_verb_part_from_sentences(input_sentences)

# print(subject_list)
# print(object_list)
# print(verb_list)
different_conclusions_from_sentences(input_sentences, subject_list, object_list, verb_list)

