import os
import string


def clean_text(text):
    """
    Removes punctuation and digits, converts to lowercase,
    and keeps spaces for word separation.
    """
    allowed_characters = string.ascii_letters + " "
    cleaned = ""
    for char in text:
        if char in allowed_characters:
            cleaned += char
        else:
            cleaned += " "
    return cleaned.lower()


def main():
    # Ask user for input file name
    input_filename = input("Enter the name of the input file: ")

    # Create output file name
    output_filename = "Analysis-" + input_filename

    # Open input file
    with open(input_filename, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # Basic counts
    line_count = len(lines)
    character_count = sum(len(line) for line in lines)

    # Combine all text into one string
    full_text = "".join(lines)

    # Clean text for word processing
    cleaned_text = clean_text(full_text)
    words = cleaned_text.split()

    word_count = len(words)

    # Word frequency dictionary
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Two-word pair (bigram) frequency
    pair_frequency = {}
    for i in range(len(words) - 1):
        pair = words[i] + " " + words[i + 1]
        pair_frequency[pair] = pair_frequency.get(pair, 0) + 1

    # Open output file
    with open(output_filename, "w", encoding="utf-8") as output_file:
        # Write basic counts
        output_file.write(f"Number of lines: {line_count}\n")
        output_file.write(f"Number of words: {word_count}\n")
        output_file.write(f"Number of characters: {character_count}\n\n")

        # Echo to screen
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {character_count}")

        # Unique words list
        output_file.write("Unique Words and Frequencies\n")
        output_file.write("----------------------------\n")

        for word in sorted(word_frequency):
            output_file.write(f"{word} ({word_frequency[word]})\n")

        # Two-word pairs section
        output_file.write("\nTwo-Word Pairs Appearing More Than Once\n")
        output_file.write("--------------------------------------\n")

        repeated_pairs = {
            pair: count for pair, count in pair_frequency.items() if count > 1
        }

        for pair in sorted(repeated_pairs):
            output_file.write(f"{pair} ({repeated_pairs[pair]})\n")

        # Echo two-word pair info to screen
        print("\nTwo-word pairs appearing more than once:")
        for pair in sorted(repeated_pairs):
            print(f"{pair} ({repeated_pairs[pair]})")

        # Final statistics
        total_letters = sum(len(word) for word in words)
        average_word_length = total_letters / word_count if word_count > 0 else 0

        unique_word_count = len(word_frequency)
        unique_letters = sum(len(word) for word in word_frequency)
        average_unique_word_length = (
            unique_letters / unique_word_count if unique_word_count > 0 else 0
        )

        repeated_pair_count = len(repeated_pairs)

        # Write final statistics
        output_file.write("\nFinal Statistics\n")
        output_file.write("----------------\n")
        output_file.write(f"Total number of words: {word_count}\n")
        output_file.write(f"Average word length: {average_word_length:.2f}\n")
        output_file.write(f"Number of unique words: {unique_word_count}\n")
        output_file.write(
            f"Average length of unique words: {average_unique_word_length:.2f}\n"
        )
        output_file.write(
            f"Number of word pairs with frequency of 2 or more: {repeated_pair_count}\n"
        )

        # Echo final statistics to screen
        print("\nFinal Statistics")
        print(f"Total number of words: {word_count}")
        print(f"Average word length: {average_word_length:.2f}")
        print(f"Number of unique words: {unique_word_count}")
        print(f"Average length of unique words: {average_unique_word_length:.2f}")
        print(
            f"Number of word pairs with frequency of 2 or more: {repeated_pair_count}"
        )


if __name__ == "__main__":
    main()
