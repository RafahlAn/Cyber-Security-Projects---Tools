import sys
from cracker.dictionary_attack import dictionary_attack

def print_banner():
	print ("="*40)
	print ("HASH CRACKER v1.0")
	print ("by RaFaHl")
	print ("="*40)
	print ()

def detect_hash_algorithm(hash_value):
	length = len(hash_value)
	if length == 32:
		return "md5"
	elif length == 40:
		return "sha1"
	elif length == 64:
		return "sha256"
	else:
		return None
def main():
	print_banner()
	if len(sys.argv) != 2:
		print ("usage:Python3 hashcracker.py <hash>")
		sys.exit()
	target_hash = sys.argv[1]
	algorithm = detect_hash_algorithm(target_hash)
	if not algorithm : 
		print ("[-] Uknown hash type")
		sys.exit()
	wordlist = "/usr/share/wordlists/rockyou.txt"
	print (f"[INFO] Detected algorithm : {algorithm}")
	print (f"[INFO] Using Wordlist: rockyou.txt")
	result = dictionary_attack(target_hash, algorithm, wordlist)
	if result : 
		print (f"\n [+] Password found : {result}")
	else : 
		print (f"\n [-] Password not found")
if __name__ == "__main__":
	main()


 
