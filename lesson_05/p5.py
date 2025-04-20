# finding the first non-repeating character
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        # jahan pr character count 1 aaya h vaha pr repeat kr diya
        print("Char is: ", char)
        break
