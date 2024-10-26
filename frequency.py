def count_word_frequency(file_path):
    # Initialize an empty dictionary to store word counts
    word_count = {}
    
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file contents
            text = file.read()
            # Split the text into words
            words = text.split()
            
            # Count the frequency of each word
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?";()').lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        # Print the word frequency
        for word, count in word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

# Specify the path to your text file
file_path = input("Enter the path to the text file: ")
count_word_frequency(file_path)
