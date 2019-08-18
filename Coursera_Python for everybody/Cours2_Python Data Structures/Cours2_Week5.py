
# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.


# a program to read through the mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
counts = dict()
list2 = list()

# The program looks for 'From ' lines
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = (line.rstrip()).split(" ")

# and takes the second word of those lines as the person who sent the mail.
        list2.append(line[1])

# The program creates a Python dictionary that maps
# the sender's mail address to a count of the number of
# times they appear in the file.
for word in list2:
    counts[word] = counts.get(word, 0) + 1

# After the dictionary is produced, the program
# reads through the dictionary using a maximum
# loop to find the most prolific committer.
maximum = None
for sender, number in counts.items():
    if maximum is None:
        maximum = number
    else:
        if number > maximum:
            maximum = number
for sender, number in counts.items():
    if maximum == number:
        print(sender, number)
