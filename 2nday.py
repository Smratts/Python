course = 'python for "beginners"'
#course1 = 'python's for beginners' #single in single cotes will give an error it will accept only first single quotes text
    #course1 = "pythons for "beginners"   #it will consider which is having open and close double quotes as a string and rest it show error
print(course)

multiple_line = '''
we use triple quotes to write multiple lines of string .
in python these quotes can be double quotes or single quotes
'''
print(multiple_line)
indexed = "Python we use square brackets to get a character of a string at a given index we use [0] ti get 1st character it dispaly w"
print(indexed[0]) # Python strings are indexed from zero 0 to so on
print(indexed[-4]) # display l :: -ve index -1, will show last first character of the string (-1,-2,-3....) will display from end of the string based on nagative index
print(indexed[0:3]) # display stating 0 index to 2 (012 characters) excludes character at index 3
print(indexed[0:]) # if we won't supply end index it will show upto end of the string stating based on index given
print(indexed[:4])# it will assume start index as 0 and display upto 4 characters of string
print(indexed[:])# it will display the start to end index of the string assuming as start to end , (we usethis for cloning the string
another = indexed[:]
print(another)
between = indexed[1:-1]
print(between) # exclude 1st and last characters and print the total string
print(2+5)
