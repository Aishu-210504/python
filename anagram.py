def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Main code
if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if are_anagrams(string1, string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
