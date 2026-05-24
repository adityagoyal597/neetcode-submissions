from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    topper_name=scores[0][0]
    topper_score=scores[0][1]
    for name,score in scores: 
        if score>topper_score:
            topper_score=score
            topper_name=name
    return topper_name
# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
