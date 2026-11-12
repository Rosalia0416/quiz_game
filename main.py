print("퀴즈 게임을 시작합니다!")

# 퀴즈 문제 목록
questions = [
    {
        "question": "파이썬에서 출력할 때 사용하는 함수는?",
        "options": ["1. input()", "2. print()", "3. output()", "4. show()"],
        "answer": "2"
    },
    {
        "question": "파이썬에서 주석을 달 때 사용하는 기호는?",
        "options": ["1. //", "2. /*", "3. #", "4. --"],
        "answer": "3"
    },
    {
        "question": "파이썬 파일의 확장자는?",
        "options": ["1. .java", "2. .txt", "3. .exe", "4. .py"],
        "answer": "4"
    }
]

# 점수 변수
score = 0

# 문제 출력 및 답변 받기
for i, q in enumerate(questions):
    print(f"\n문제 {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    user_answer = input("답을 입력하세요 (1~4): ")
    
    if user_answer == q["answer"]:
        print("정답입니다! ✓")
        score += 1
    else:
        print(f"틀렸습니다. 정답은 {q['answer']}번입니다.")

# 최종 점수 출력
print(f"\n최종 점수: {score}/{len(questions)}")