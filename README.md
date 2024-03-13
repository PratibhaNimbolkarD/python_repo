### **find_percentage**

* Defined a function find_percentage(n) to calculate the percentage of scores for a given student.
* Collected user input for the number of students and their corresponding scores.
* Stored the student names and their scores in a dictionary student_marks.
* Queried the name of the student whose percentage is to be calculated.
* Calculated and printed the percentage of scores for the queried student using the find_percentage function.

### **find_runnerup_score**
* Defined a function runner_up() to find the runner-up score from a list of scores provided as input.
* Collected user input for the number of scores and the scores themselves.
* Stored the scores in a list and passed it to the runner_up() function.
* The runner_up(arr) function removes duplicates from the list of scores, finds the maximum score, removes it from 
  the set, and then prints the maximum score remaining in the set, which is the runner-up score.

### **mutations**
* The function mutate_string() takes three user input : string (the original string), position (the index at which the character needs to be replaced), and character (the new character to be placed at the specified position).
* A new string newString is created by slicing the original string and replacing the character at the specified position.
* The modified string newString is then returned from the function.
* In the __main__ block, user input is collected for the original string s and the position i and character c for mutation.
* The mutate_string() function is called with the provided parameters to obtain the modified string s_new.
* Finally, the modified string s_new is printed.