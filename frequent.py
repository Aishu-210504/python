from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None
    counter = Counter(lst)
    most_common = counter.most_common(1)[0]
    return most_common[0], most_common[1]

# Main code
if __name__ == "__main__":
    elements = input("Enter list elements separated by space: ").split()
    result = most_frequent_element(elements)
    
    if result:
        print(f"The most frequent element is '{result[0]}' which appears {result[1]} times.")
    else:
        print("The list is empty.")
