# Function to convert binary string to characters
def binary_to_text(binary_string):
    binary_values = binary_string.split()
    text = ''.join(chr(int(char, 2)) for char in binary_values if len(char) <= 16)  # Limit conversion to 16 bits
    return text

# XOR function
def xor_strings(str1, str2):
    result = ''
    for char1, char2 in zip(str1, str2):
        if char1 == ' ' and char2 == ' ':
            result += ' '
        elif char1 == char2 or char2 == ' ':
            result += '0'
        else:
            result += '1'
    return result

# Output of the original code
xor_result = input("Enter XOR result: ")

# The binary representation of "I", "T", and "6" with spaces
binary_IT6 = ("1001001", "1010100", "0000110")

# Split the xor_result into chunks of 7 characters (bits)
binary_chunks = xor_result.split()

# Print out the binary chunks
print("Binary Chunks:", binary_chunks)

# XOR each chunk with the corresponding part of the binary representation of "IT6"
deciphered_chunks = []
for i, chunk in enumerate(binary_chunks):
    it6_part = binary_IT6[i % len(binary_IT6)]  # Get the corresponding part of "IT6"
    xor_result = xor_strings(chunk, it6_part)
    deciphered_chunks.append(xor_result)

# Print out the XOR results
print("XOR Results:", deciphered_chunks)

# Convert deciphered binary chunks back to text
deciphered_text = binary_to_text(' '.join(deciphered_chunks))  # Add space when joining chunks

print("Deciphered Text:", deciphered_text)
