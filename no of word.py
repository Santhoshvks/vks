s = input("Enter any string to count word: ");
if s == 'x':
    exit();
else:
    word_length = len(s.split());
    print("\nNumber of words =",word_length);
