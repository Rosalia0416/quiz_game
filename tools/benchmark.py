"""
퀴즈 개수가 많아졌을 때(1,000개 / 10,000개)의 성능을 측정하는 스크립트.

- 실제 state.json은 건드리지 않고, 임시 폴더에 테스트용 파일을 만들어 측정한다.
- 실행: 프로젝트 루트에서  python tools/benchmark.py
"""
import json
import os
import random
import sys
import tempfile
import time
import tracemalloc

# 프로젝트 루트의 main.py를 불러오기 위해 경로 추가
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import main  # noqa: E402


def make_dummy_data(n):
    """n개의 테스트용 퀴즈 데이터를 만든다."""
    quizzes = []
    for i in range(n):
        quizzes.append({
            "question": f"테스트 문제 {i}번: 다음 중 올바른 것은?",
            "choices": [f"{k}. 선택지{k}" for k in range(1, 5)],
            "answer": (i % 4) + 1,
        })
    return {"quizzes": quizzes, "best_score": None,
            "best_correct": 0, "best_total": 0}


def measure(n, folder):
    path = os.path.join(folder, f"state_{n}.json")
    main.STATE_FILE = path          # 임시 파일을 쓰도록 경로 교체

    with open(path, "w", encoding="utf-8") as f:
        json.dump(make_dummy_data(n), f, ensure_ascii=False, indent=2)
    size_kb = os.path.getsize(path) / 1024

    # 불러오기 시간 + 메모리
    tracemalloc.start()
    start = time.perf_counter()
    game = main.QuizGame()
    load_ms = (time.perf_counter() - start) * 1000
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 저장 시간
    start = time.perf_counter()
    game.save_state()
    save_ms = (time.perf_counter() - start) * 1000

    # 랜덤 출제용 섞기 시간
    start = time.perf_counter()
    questions = game.quizzes[:]
    random.shuffle(questions)
    shuffle_ms = (time.perf_counter() - start) * 1000

    # 문제 검색(순차 탐색) 시간
    start = time.perf_counter()
    _ = [q for q in game.quizzes if "9999" in q.question]
    search_ms = (time.perf_counter() - start) * 1000

    print(f"{n:>6}개 | 파일 {size_kb:>6.0f}KB | 불러오기 {load_ms:6.1f}ms | "
          f"저장 {save_ms:6.1f}ms | 섞기 {shuffle_ms:5.2f}ms | "
          f"검색 {search_ms:5.2f}ms | 메모리 {peak / 1024 / 1024:5.2f}MB")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        for n in (1000, 10000):
            measure(n, folder)
