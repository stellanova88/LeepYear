# LeapYear

This is a program to check if a year is a leap year with tests.  

This program uses pytest and runs 2 python test files division_test.py and test_LeapYear.py.
division_test.py test if the division is done correctly.
test_LeapYear.py test if the acceptance requirements for a leap year is meet.
  Year is leap year when:
    - Year is divisible with 4, but not 100.
    - Year is divisible with 400.

   Year is not leap year when:
    - Year is not divisible with 4.
    - Year is divisible with 100, but not 400.

The program is using Github Actions to run these tests on every push to this Github repository.
