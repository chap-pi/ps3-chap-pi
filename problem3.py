"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    numbers = []
    while True:
        entry=input("Enter a number or 'Done': ")
        if entry=="Done":
            break
        try:
            entry=float(entry)
            numbers.append(entry)
        except ValueError:
            print("Enter a valid number")
    return numbers


def analyze_numbers(numbers):
    if not numbers:
        return None
    analysis = {}
    analysis["count"]=len(numbers)
    analysis["sum"]=sum(numbers)
    analysis["average"]=sum(numbers)/len(numbers)
    analysis["minimum"]=min(numbers)
    analysis["maximum"]=max(numbers)
    analysis["even_count"]=sum(1 for n in numbers if n%2==0)
    analysis["odd_count"]=sum(1 for n in numbers if n%2!=0)
    return analysis


def display_analysis(analysis):

    if not analysis:
        return
    print("\nAnalysis Results:")
    print("-" * 20)
    for key in analysis:
        print(key,":",analysis[key])
    return



def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()