# Write a program that is able to encode and
# decode messages based on this Salade cipher.
# message = []
def valid_letters():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters


def accept_input():
    mode = input('Enter the mode, encode or decode: ')
    n = int(input("Enter the base shift for each character: "))
    m = int(input("Additional-step shift for the first character: "))
    message = input("Enter the message you want to encode or decode: ")
    return mode, n, m, message


def encode(n, m, message, letters):
    encoded_output = []
    first_shift = m
    for ch in message:
        if ch.islower():
            position = letters.index(ch)
            shifted_position = (first_shift + position + n) % 26
            char = letters[shifted_position]
            encoded_output.append(char)
            first_shift = shifted_position
        else:
            encoded_output.append(ch)
    return encoded_output


def decode(n, m, message, letters):
    decoded_output = []
    previous_shift = m
    for ch in message:
        if ch.islower():
            position = letters.index(ch)
            previous_position = (position - previous_shift - n) % 26
            char = letters[previous_position]
            decoded_output.append(char)
            previous_shift = position
        else:
            decoded_output.append(ch)
    return decoded_output


# --Main Program --#
letters = valid_letters()
mode, n, m, message = accept_input()

if mode == "encode":
    output_encode = encode(n, m, message, letters)
    print(*output_encode, sep="")
else:
    output_decode = decode(n, m, message, letters)
    print(*output_decode, sep="")
