def autokey(plaintext, keyphrase):
	key = list(keyphrase.upper())
	message = list(plaintext.upper())
	for i in range(0, len(message) - len(key)):
		key.append(message[i])
	ciphertext = []
	for j in range(0, len(key)):
		codepoint = ord(key[j]) + ord(message[j]) - 65
		if codepoint > 90:
			codepoint -= 26
		ciphertext.append(chr(codepoint))
	return ''.join(ciphertext)