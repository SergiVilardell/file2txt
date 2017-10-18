import nltk
from nltk.corpus import cess_esp


def word_check(out_pdf, out_img):
	words_pdf = nltk.word_tokenize(out_pdf)
	words_img = nltk.word_tokenize(out_img)

	pdf_count=0
	img_count=0
	for i in range(len(words_pdf)):
		if((words_pdf[i] in cess_esp.words())):
			pdf_count+=1

	for j in range(len(words_img)):
		if((words_img[j] in cess_esp.words())):
			img_count+=1

	print("Checked words in processed pdf: "+pdf_count)
	print("Checked words in processed image: "+img_count)
