s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.replace('.','').replace(',','').upper()
words = s.split(' ')
words_final = list(set(words))
words_final.sort(key=str)

print(words_final)

# key - value 형태
for word in words_final:
    print('{0}:{1}'.format(word,words.count(word)))