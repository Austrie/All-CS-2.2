from collections import deque

def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    courses = [[] for i in range(numCourses)]
    for course_with_pre_req in prerequisites:
        courses[course_with_pre_req[1]].append(
            course_with_pre_req[0]
        )

    answer = []
    global visited
    visited = [0] * numCourses
    for course_number in range(numCourses):
        if visited[course_number] == 0 and check(course_number, visited, courses, answer):
            return []
    answer.reverse()
    return answer
        
def check(course_number, visited, courses, answer):
    visited[course_number] = 1
    for req in courses[course_number]:
        if visited[req] == 1:
            return True
        if visited[req] == 0 and check(req, visited, courses, answer):
            return True
    visited[course_number] = 2
    answer.append(course_number)
    return False

# Test Cases
courses1 = [ [1,0] ]
assert courseOrder(2, courses1) == [0, 1]

courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
assert courseOrder(4, courses2) in possibleSchedules
