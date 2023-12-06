# Simple Calculator
## [Video Demo](https://youtu.be/)
### Description:
This program performs mathematical calculations on two or more operands based on the type of input operator

#### How the Program Works?
This program first takes the operator from the user by entering the corresponding letter:
('Enter 'a' for addition
Enter 's' for substraction
Enter 'm' for multiplication
Enter 'd' for division
Enter 'q' to quit ')
Then it takes two numbers from the input and applies mathematical operations on them.
Then it asks the user whether to add another number for the performed mathematical operation or not.(y/n)
If 'y' is entered, the user can enter the next number, and if 'n' is entered, the mathematical calculation ends with the selected operator.

To end the execution of the program, the user must enter the letter 'q'.

[!NOTE] The user can only select one operator in each mathematical operation.

#### Usage
Run the program python script `project.py` with [python](https://www.python.org/).
```
python project.py
```
Test the program python script `test_project.py` with [pytest](https://docs.pytest.org/en/7.2.x/).
```
pytest test_project.py


