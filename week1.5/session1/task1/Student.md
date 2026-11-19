# Student Class

## Attributes

- `name`: the student's full name (string)
- `student_id`: unique identifier (string)
- `courses`: enrolled course names (list of strings)
- `grades`: mapping of course names to marks (dictionary)
- `email`: contact address (string)

## Behaviour

- `enrol(course)`: add a course to the student's enrolments
- `drop(course)`: remove an enrolled course
- `record_grade(course, grade)`: store a course result
- `average_grade()`: calculate the mean mark, when marks are available
- `has_passed(course)`: determine whether a given course has been passed
- `summary()`: produce a readable summary of student details
