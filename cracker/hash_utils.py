import hashlib 

def hash_word(word, algorithm):
	word = word.encode()

	if algorithm == "md5":
		return hashlib.md5(word).hexdigest()
	elif algorithm == "sha1":
		return hashlib.sha1(word).hexdigest()
	elif algorithm == "sha256":
		return hashlib.sha256(word).hexdigest()
	else :
		raise ValueError("Unsupported hash algorithm")
