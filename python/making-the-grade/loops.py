"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    scores = []
    for score in student_scores:
        scores.append(round(score))
    return scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failed = 0

    for student in student_scores:
        if student <= 40:
            failed = failed + 1
    
    return failed
    

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best = []

    for score in student_scores:
        if score >= threshold:
            best.append(score)

    return best 


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """


    bound = (highest - 40) // 4

    D = 41
    C = D + bound
    B = C + bound
    A = B + bound

    return [D, C, B, A]



def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = []

    for i in range(len(student_scores)):
        ranking.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranking




def perfect_score(student_info):

    perfect = []

    for name, score in student_info:
        if score == 100:
            perfect.append(name)
            perfect.append(score)
            break
        else:
            pass
    
    return perfect

