# Assignment 3 part 2

# Q1
* I have modified the json to map parent with id rather than name since id is unique.
* The json file will have one more field for each employee named eid
* The parent will also be mapped with id and not name.
* I have outputed both id and name in appropriate positions.
* I have used dictionaries to map parents, levels and names
* I have removed hardcoded functions and made every function to be operated by loop
* Using that we can include as many arguments as we like.

# Q2
* I have used full gregorian calendar.
* I am first calculating total days in a date and then subtracting the days from the two dates.
* I have mainly changed the validation function to take separate args for day,month and year instead of all at the same time
* By doing the above we have achieved some flexibily on the format of date

# Q3
* I am sorting the intervals and then finding the merged intervals with appropriate duration.
* To sort I am using compare function which calculates different between two times.
* Then I have converted this compare function to key for the sort function
* I am looping all the files of my need i.e "Employee*.txt" and adding them to the buffer.
* Now I have stored every file data as a list element, so that accessing each data is easy.
* By doing the above we have achieved a greater flexibility which will help in solving any number of Files.
* For common slots I am taking two open slots at a time and calculating the merged total open slots now using this result for the next open slots and so on.


## Github link:
[GitHub](https://github.com/ramirocruz/2020201098_Assignment3a)
