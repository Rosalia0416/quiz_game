import json
import os

# ─────────────────────────────────────────
# 기본 퀴즈 데이터 (일반상식 + 건강, 5개 이상)
# ─────────────────────────────────────────
DEFAULT_QUIZZES = [
    {
        "question": "지구에서 가장 큰 대양은?",
        "choices": ["1. 대서양", "2. 인도양", "3. 태평양", "4. 북극해"],
        "answer": 3
    },
    {
        "question": "사람의 정상 체온(℃)으로 가장 적절한 것은?",
        "choices": ["1. 35.0℃", "2. 36.5℃", "3. 38.0℃", "4. 39.5℃"],
        "answer": 2
    },
    {
        "question": "대한민국의 수도는?",
        "choices": ["1. 부산", "2. 인천", "3. 대전", "4. 서울"],
        "answer": 4
    },
    {
        "question": "하루에 권장되는 물 섭취량은?",
        "choices": ["1. 500mL", "2. 1L", "3. 2L", "4. 4L"],
        "answer": 3
    },
    {
        "question": "세계에서 가장 높은 산은?",
        "choices": ["1. 백두산", "2. 에베레스트", "3. 킬리만자로", "4. 알프스"],
        "answer": 2
    },
    {
        "question": "비타민 C가 가장 풍부한 과일은?",
        "choices": ["1. 사과", "2. 바나나", "3. 키위", "4. 포도"],
        "answer": 3
    },
    {
        "question": "올림픽은 몇 년마다 열리는가?",
        "choices": ["1. 2년", "2. 3년", "3. 4년", "4. 5년"],
        "answer": 3
    },
    {
        "question": "심장이 1분에 뛰는 정상 맥박수(성인 기준)는?",
        "choices": ["1. 20~40회", "2. 60~100회", "3. 110~130회", "4. 140~160회"],
        "answer": 2
    },
]

STATE_FILE = "state.json"


# ─────────────────────────────────────────
# Quiz 클래스
# ─────────────────────────────────────────
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 (str)
        self.choices  = choices    # 선택지 리스트 (list[str])
        self.answer   = answer     # 정답 번호 (int, 1~4)

    def display(self, index):
        """문제와 선택지를 출력한다."""
        print(f"\n문제 {index}. {self.question}")
        for choice in self.choices:
            print(f"  {choice}")

    def check_answer(self, user_answer):
        """사용자 답(int)이 정답이면 True 반환."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 dict로 변환."""
        return {
            "question": self.question,
            "choices":  self.choices,
            "answer":   self.answer
        }

    @staticmethod
    def from_dict(data):
        """dict에서 Quiz 객체 생성."""
        return Quiz(data["question"], data["choices"], data["answer"])


# ─────────────────────────────────────────
# QuizGame 클래스
# ─────────────────────────────────────────
class QuizGame:
    def __init__(self):
        self.quizzes    = []   # Quiz 객체 목록
        self.best_score = 0    # 최고 점수
        self.load_state()      # 시작 시 파일 불러오기

    # ── 파일 저장 / 불러오기 ──────────────────
    def load_state(self):
        """state.json 에서 데이터를 불러온다."""
        if not os.path.exists(STATE_FILE):
            # 파일 없음 → 기본 데이터 사용
            self._load_defaults()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes    = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", 0)

            if not self.quizzes:          # 퀴즈가 비어 있으면 기본 데이터 보충
                self._load_defaults()

        except (json.JSONDecodeError, KeyError, TypeError):
            print("⚠️  저장 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            self._load_defaults()

    def _load_defaults(self):
        """기본 퀴즈 데이터를 불러온다."""
        self.quizzes = [Quiz.from_dict(q) for q in DEFAULT_QUIZZES]

    def save_state(self):
        """현재 상태를 state.json 에 저장한다."""
        try:
            data = {
                "quizzes":    [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"⚠️  파일 저장 중 오류가 발생했습니다: {e}")

    # ── 입력 유틸리티 ─────────────────────────
    def input_int(self, prompt, min_val, max_val):
        """
        min_val ~ max_val 범위의 정수를 입력받는다.
        잘못된 입력은 재입력 요청.
        """
        while True:
            try:
                raw = input(prompt).strip()
                if raw == "":
                    print("  ⚠️  값을 입력해주세요.")
                    continue
                value = int(raw)
                if min_val <= value <= max_val:
                    return value
                print(f"  ⚠️  {min_val}~{max_val} 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("  ⚠️  숫자만 입력해주세요.")

    # ── 메뉴 ──────────────────────────────────
    def show_menu(self):
        print("\n" + "="*35)
        print("   📚 일반상식 & 건강 퀴즈 게임")
        print("="*35)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("="*35)

    def run(self):
        """메인 루프."""
        print("\n🎉 퀴즈 게임에 오신 것을 환영합니다!")
        try:
            while True:
                self.show_menu()
                choice = self.input_int("번호를 선택하세요: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    self.quit_game()
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  프로그램이 중단되었습니다. 저장 후 종료합니다.")
            self.save_state()

    # ── 1. 퀴즈 풀기 ──────────────────────────
    def play_quiz(self):
        if not self.quizzes:
            print("\n❌ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print("\n🎯 퀴즈를 시작합니다!\n")
        score = 0
        total = len(self.quizzes)

        for i, quiz in enumerate(self.quizzes, start=1):
            quiz.display(i)
            user_answer = self.input_int("정답 번호를 입력하세요 (1~4): ", 1, 4)

            if quiz.check_answer(user_answer):
                print("  ✅ 정답입니다!")
                score += 1
            else:
                print(f"  ❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

        # 결과 출력
        print("\n" + "="*35)
        print(f"  🏁 최종 점수: {score} / {total}")
        print("="*35)

        # 최고 점수 갱신
        if score > self.best_score:
            self.best_score = score
            print(f"  🏆 새로운 최고 점수! {self.best_score}점")
        
        self.save_state()

    # ── 2. 퀴즈 추가 ──────────────────────────
    def add_quiz(self):
        print("\n📝 새 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("  ⚠️  문제를 입력해야 합니다.")
            return

        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"  선택지 {i}번: ").strip()
                if choice:
                    choices.append(f"{i}. {choice}")
                    break
                print("  ⚠️  선택지를 입력해야 합니다.")

        answer = self.input_int("정답 번호를 입력하세요 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("  ✅ 퀴즈가 추가되었습니다!")

    # ── 3. 퀴즈 목록 ──────────────────────────
    def show_quiz_list(self):
        if not self.quizzes:
            print("\n❌ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 전체 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-"*35)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")
            for choice in quiz.choices:
                print(f"     {choice}")
            print(f"   ✔ 정답: {quiz.answer}번")
            print("-"*35)

    # ── 4. 점수 확인 ──────────────────────────
    def show_best_score(self):
        print("\n" + "="*35)
        if self.best_score == 0:
            print("  아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"  🏆 최고 점수: {self.best_score} / {len(self.quizzes)}")
        print("="*35)

    # ── 5. 종료 ───────────────────────────────
    def quit_game(self):
        self.save_state()
        print("\n👋 퀴즈 게임을 종료합니다. 수고하셨습니다!")


# ─────────────────────────────────────────
# 진입점
# ─────────────────────────────────────────
if __name__ == "__main__":
    game = QuizGame()
    game.run()