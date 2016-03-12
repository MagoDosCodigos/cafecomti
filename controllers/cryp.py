
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

class CryptKey():
    def __init__(self, password):
        self.password = password
        self.cipher_text = ""
        self.plain_text = ""
        self.iv = Random.new().read(AES.block_size)

    def encryption(self):
    # Encryption
        passwordSHA = SHA256.new(self.password).hexdigest()
        encryption_suite = AES.new('This is a key123', AES.MODE_CBC, self.iv)
        self.cipher_text = encryption_suite.encrypt(passwordSHA)
        return self.cipher_text.encode('utf-8')

    def decryption(self):
        # Decryption
        decryption_suite = AES.new('This is a key123', AES.MODE_CBC, self.iv)
        self.plain_text = decryption_suite.decrypt(self.cipher_text)
        return SHA256.new(self.password).hexdigest() == self.plain_text


a = CryptKey("tiago")
a.encryption()