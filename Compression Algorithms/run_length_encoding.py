def run_length_encode(text):
    encoded_text = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_text += str(count) + text[i - 1]
            count = 1
    encoded_text += str(count) + text[-1]
    return encoded_text

def run_length_decode(encoded_text):
    decoded_text = ''
    for i in range(0, len(encoded_text), 2):
        count = int(encoded_text[i])
        char = encoded_text[i + 1]
        decoded_text += char * count
    return decoded_text

# Example Usage
original_text = "AAAABBBCCDAA"
encoded_text = run_length_encode(original_text)
print("Encoded:", encoded_text)
decoded_text = run_length_decode(encoded_text)
print("Decoded:", decoded_text)
