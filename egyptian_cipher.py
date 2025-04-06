import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# خريطة من الرموز الهيروغليفية إلى الحروف اللاتينية
hieroglyphics_map = {
    '𓄿': 'a', '𓃀': 'b', '𓍿': 'c', '𓆓': 'd', '𓇋': 'e', '𓆑': 'f', '𓎼': 'g', '𓎛': 'h',
    '𓇋': 'i', '𓆸': 'j', '𓎡': 'k', '𓃭': 'l', '𓈖': 'm', '𓈖': 'n', '𓍯': 'o', '𓏛': 'p',
    '𓎼': 'q', '𓂋': 'r', '𓋴': 's', '𓏏': 't', '𓅱': 'u', '𓂋𓅱': 'v', '𓅱': 'w', '𓎧': 'x',
    '𓇋𓅱': 'y', '𓆩': 'z', ' ': ' '
}

# دالة للتشفير الهيروغليفي
def egyptian_encrypt(plain_text):
    encrypted_text = ''
    for char in plain_text:
        encrypted_text += hieroglyphics_map.get(char.lower(), char)
    return encrypted_text

# دالة للتشفير باستخدام XOR
def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

# دالة للتشفير باستخدام Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                encrypted_text += shifted.upper()
            else:
                encrypted_text += shifted
        else:
            encrypted_text += char
    return encrypted_text

# دالة للتشفير باستخدام AES
def aes_encrypt(plain_text, password):
    key = hashlib.sha256(password.encode()).digest()  # توليد مفتاح AES
    iv = base64.b64encode(AES.new(key, AES.MODE_CBC).iv)  # توليد الـ IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = plain_text + (16 - len(plain_text) % 16) * ' '  # إضافة padding
    encrypted_text = cipher.encrypt(padded_text.encode())
    return base64.b64encode(iv + encrypted_text).decode()

# دالة للتشفير باستخدام RSA
def rsa_encrypt(plain_text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_text = cipher.encrypt(plain_text.encode())
    return base64.b64encode(encrypted_text).decode()

# دالة للتشفير باستخدام كل الطرق المتاحة
def multi_layer_encrypt(plain_text, caesar_shift, xor_key, password, public_key):
    # أولاً التشفير باستخدام الهيروغليفية
    encrypted_text = egyptian_encrypt(plain_text)
    # ثم التشفير باستخدام XOR
    encrypted_text = xor_encrypt(encrypted_text, xor_key)
    # ثم التشفير باستخدام Caesar Cipher
    encrypted_text = caesar_encrypt(encrypted_text, caesar_shift)
    # ثم التشفير باستخدام AES
    encrypted_text = aes_encrypt(encrypted_text, password)
    # ثم التشفير باستخدام RSA
    encrypted_text = rsa_encrypt(encrypted_text, public_key)
    return encrypted_text

# اختبار الكود:
plain_text = "Hello World! 123"
password = "my_secure_password"
caesar_shift = 3  # الإزاحة في التشفير Caesar
xor_key = 42  # مفتاح XOR

# توليد مفتاح RSA (للاختبار فقط - استخدم مفاتيح حقيقية في التطبيق الفعلي)
public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxE0+MxxAqzqYATZgxFx2
...
-----END PUBLIC KEY-----"""

# تشفير النص باستخدام الطبقات المختلفة
multi_encrypted = multi_layer_encrypt(plain_text, caesar_shift, xor_key, password, public_key)

# عرض النص المشفر
print(f"النص المشفر متعدد الطبقات: {multi_encrypted}")
