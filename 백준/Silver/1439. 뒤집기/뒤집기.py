string = input()
new_string = ''

for i in range(len(string)):
  if i == len(string) - 1:
    new_string += string[i]
    break
  if string[i] != string[i + 1]:
    new_string += string[i]

print(min(new_string.count('1'), new_string.count('0')))