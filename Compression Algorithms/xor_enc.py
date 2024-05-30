def xor_encode(data, key):
    encoded = []
    for i in range(len(data)):
        encoded.append(data[i] ^ key)  # XOR işlemi uygulanıyor
    return encoded

def xor_decode(encoded, key):
    return xor_encode(encoded, key)  # Şifre çözme, şifreleme ile aynı işlemdir

# Örnek Kullanım:
data = [10, 15, 20, 28, 35]
key = 123  # Şifreleme anahtarı

encoded_data = xor_encode(data, key)
print("Encoded:", encoded_data)
decoded_data = xor_decode(encoded_data, key)
print("Decoded:", decoded_data)
