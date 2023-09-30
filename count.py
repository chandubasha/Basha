# Function to count word occurrences in a text file
def count_word_occurrences(file_path):
    word_count = {}  # Dictionary to store word counts

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Split the line into words
                words = line.strip().split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    cleaned_word = word.strip('.,!?-()[]{}":;').lower()
                    if cleaned_word:
                        # Update word count in the dictionary
                        if cleaned_word in word_count:
                            word_count[cleaned_word] += 1
                        else:
                            word_count[cleaned_word] = 1

        # Sort the dictionary by word for better readability
        sorted_word_count = sorted(word_count.items())

        # Print the unique words and their counts
        for word, count in sorted_word_count:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input file path
file_path = "sample.txt"  # Replace with the path to your text file

# Call the function to count word occurrences
count_word_occurrences(file_path)