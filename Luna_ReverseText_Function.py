# text reversal

print("Hello! It's reversing words time! Enter your desired word below!\n")

def reverse_test():
    while True:
        user_input = input("Please put text!!: ")

        if user_input.isalpha():
            reversed_text = user_input[::-1]
            print("Here is the Output: ", reversed_text)
            break
        else:
            print("Error Reported Kiddo!! Didn't you read the instructions well? Enter text only.\n")

reverse_test()
