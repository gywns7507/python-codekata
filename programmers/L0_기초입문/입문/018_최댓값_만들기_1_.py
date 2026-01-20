# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김효준
# 작성일: 2026. 01. 20. 11:26:00

def solution(numbers):
    answer = numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer