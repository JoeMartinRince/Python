"""
AUTHOR : JOE MARTIN RINCE
DATE: 29-10-2028
"""
string_input=input("Enter your string: ")
vowels="aeiouAEIOU"
vowel_count=0
for char in string_input:
    if char in vowels:
        vowel_count+=1
print(f"The number of vowels in the string {string_input} is {vowel_count}")