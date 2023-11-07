def check(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = len(input_string) - vowel_count
    return vowel_count, consonant_count

sample=input()
vowels, consonants = check(sample)
print("Vowels: %s"%vowels, "Consonants: %s"%consonants)