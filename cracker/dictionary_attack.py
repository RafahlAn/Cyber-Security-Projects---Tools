import os
import sys
from cracker.hash_utils import hash_word
  
  #  Attempts to crack a hash using a dictionary attack.  
  # Parameters:
  #  - target_hash: the hash to crack
  #  - algorithm: hashing algorithm (md5, sha1, sha256)
  #  - wordlist: path to the wordlist file

def dictionary_attack(target_hash, algorithm, wordlist):
	print("[INFO] Starting dictionary attack...\n")
	total_passwords = sum(1 for _ in open(wordlist, "r", errors="ignore"))
	with open(wordlist, "r", errors="ignore") as file:
		count = 0 
		for line in file :
			word = line.strip() #remove newline characters
			count += 1
			hashed = hash_word(word, algorithm) #hash the curent word
			if hashed == target_hash: # check if hash matches
				return word
		# progress calculation

			percent = (count / total_passwords) * 100
			bar_length = 20 
			filled = int (bar_length * count // total_passwords)
			bar = "#" * filled + "-" * (bar_length - filled)
			sys.stdout.write(f"\r Progress : [{bar}] {percent:.2f}%")
			sys.stdout.flush()
		return None
