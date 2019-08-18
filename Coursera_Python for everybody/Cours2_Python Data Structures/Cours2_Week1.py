# Week 1

x = 'From marquard@uct.ac.za'
print(x[14:17])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos: pos + 3])

# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
a = text.find(' ')
word = text[a:]
word = (word.strip())
word = float(word)
print(word)
