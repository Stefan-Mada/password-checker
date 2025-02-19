#!/usr/bin/env python3

intervals = (
    ('years', 604800*52),
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=2):
    result = []
    
    if seconds < 1:
      return "Under a second."

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

print("This is a password strength checker. The time it takes to crack will be listed assuming 100 billion attempts a second (shown to be a realistic figure).")
print("Enter 'exit' to exit.")

inputStr = ""

numPerSec = 100000000000

while inputStr != "exit":
  inputStr = input("Enter a password: ")
  
  if inputStr.isalpha():
    if inputStr.islower() or inputStr.isupper():
      print(f"{display_time((26**len(inputStr))/numPerSec)}")
    else:
      print(f"{display_time((52**len(inputStr))/numPerSec)}")
  elif inputStr.isdigit():
    print(f"{display_time((10**len(inputStr))/numPerSec)}")
  elif inputStr.isalnum():
    if inputStr.islower() or inputStr.isupper():
      print(f"{display_time((36**len(inputStr))/numPerSec)}")
    else:
      print(f"{display_time((62**len(inputStr))/numPerSec)}")
  else: # has special characters
    if (inputStr.islower() or inputStr.isupper()) and not has_numbers(inputStr):
      print(f"{display_time((58**len(inputStr))/numPerSec)}")
    elif (inputStr.islower() or inputStr.isupper()) and has_numbers(inputStr):
      print(f"{display_time((68**len(inputStr))/numPerSec)}")
    elif not has_numbers(inputStr):
      print(f"{display_time((84**len(inputStr))/numPerSec)}")
    else:
      print(f"{display_time((94**len(inputStr))/numPerSec)}")
