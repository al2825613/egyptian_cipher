import base64

# قاموس الحروف الهيروغليفية مع الحروف والأرقام
hieroglyphics = {
    "A": "𓄿", "B": "𓃀", "C": "𓍿", "D": "𓂧", "E": "𓇋", "F": "𓆑", "G": "𓎼", "H": "𓎛",
    "I": "𓏏", "J": "𓆓", "K": "𓎡", "L": "𓃭", "M": "𓅓", "N": "𓈖", "O": "𓅱", "P": "𓊪",
    "Q": "𓂋", "R": "𓂋", "S": "𓊖", "T": "𓏏", "U": "𓅱", "V": "𓆑", "W": "𓅯", "X": "𓐍",
    "Y": "𓋴", "Z": "𓍯", "0": "𓏺", "1": "𓏸", "2": "𓏷", "3": "𓏶", "4": "𓏵", "5": "𓏴",
    "6": "𓏳", "7": "𓏲", "8": "𓏱", "9": "𓏰", " ": " "
}

# دالة لتشفير النص باستخدام الهيروغليفية المصرية
def egyptian_cipher(text):
    return ''.join([hieroglyphics.get(char.upper(), char) for char in text])

# دالة لفك تشفير النص
def egyptian_decipher(ciphertext):
    reverse_hieroglyphics = {v: k for k, v in hieroglyphics.items()}
    return ''.join([reverse_hieroglyphics.get(char, char) for char in ciphertext])

# دالة لتشفير النص باستخدام Base64
def base64_encrypt(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

# دالة لفك تشفير النص باستخدام Base64
def base64_decrypt(encoded_text):
    return base64.b64decode(encoded_text).decode('utf-8')

# دالة لتطبيق طبقات التشفير
def multi_layer_encrypt(text):
    encrypted_text = egyptian_cipher(text)
    encrypted_text = base64_encrypt(encrypted_text)
    return encrypted_text

# دالة لفك طبقات التشفير
def multi_layer_decrypt(text):
    decrypted_text = base64_decrypt(text)
    decrypted_text = egyptian_decipher(decrypted_text)
    return decrypted_text

# اختبار الدوال
if __name__ == "__main__":
    sample_text = "Hello World 123"
    encrypted_text = multi_layer_encrypt(sample_text)
    decrypted_text = multi_layer_decrypt(encrypted_text)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
