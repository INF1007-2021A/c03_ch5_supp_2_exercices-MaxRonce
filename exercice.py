#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	sum = 0
	for i in text:
		if i.isalnum():
			sum+=1
	return sum

def get_word_length_histogram(text):
	word_list = text.split()
	histo = [0]
	len_words = []
	for word in word_list : 
		len_words.append(get_num_letters(word))

	for i in range(max(len_words)):
		histo.append(0)

	for k in len_words:
		histo[k] = len_words.count(k)
	

	return histo

def format_histogram(histogram):
	ROW_CHAR = "*"
	for i in range(1,len(histogram)) : 
		print(i, ROW_CHAR*histogram[i], '\n')
	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	maxi = max(histogram)
	array = []
	k = 0
	while k <3:
		array = []
		for i in range(len(histogram)):
			if histogram[i] == maxi:
				array.append(BLOCK_CHAR)
				histogram[i] -=1
			else : 
				array.append(" ")
		maxi -=1
		for i in range(len(array)):
			print(array[i], end='')
		print('\n')
		k+=1
	print(len(histogram) * LINE_CHAR)

		
	
	
	
	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(get_num_letters(spam), '\n')
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
