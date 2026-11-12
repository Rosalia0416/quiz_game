# 🧠 일반상식 & 건강 퀴즈 게임

## 📌 프로젝트 개요
터미널(콘솔)에서 실행하는 Python 퀴즈 게임입니다.
메뉴에서 번호를 선택해 퀴즈를 풀고, 새 퀴즈를 등록하고, 목록과 최고 점수를 확인할 수 있습니다.
추가한 퀴즈와 최고 점수는 `state.json` 파일에 저장되어 프로그램을 종료했다가 다시 실행해도 유지됩니다.

- 언어: Python 3.10 이상 (외부 라이브러리 없이 표준 라이브러리만 사용)
- 구조: `Quiz`(개별 문제) / `QuizGame`(게임 전체 관리) 2개 클래스로 역할 분리

## 💡 퀴즈 주제와 선정 이유
**주제: 일반상식 + 건강**

- 누구나 한 번쯤 들어봤지만 정확히는 헷갈리는 내용(대양의 크기, 정상 체온, 맥박수 등)이라 퀴즈로 풀었을 때 재미와 학습 효과가 모두 있습니다.
- 건강 상식(물 섭취량, 비타민 C 등)은 일상생활에 바로 도움이 되는 정보라서, 게임을 하면서 실용적인 지식도 얻을 수 있도록 골랐습니다.
- 특정 분야 지식이 없어도 풀 수 있어서 가족·친구 등 다양한 사람이 함께 즐길 수 있습니다.

## ▶️ 실행 방법
1. Python 3.10 이상이 설치되어 있는지 확인합니다.
   ```bash
   python --version
   ```
2. 저장소를 내려받습니다.
   ```bash
   git clone https://github.com/Rosalia0416/quiz_game.git
   cd quiz_game
   ```
3. 프로그램을 실행합니다.
   ```bash
   python main.py
   ```

## 🎮 기능 목록
| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 저장된 퀴즈를 **랜덤 순서**로 출제하고, 정답/오답과 최종 점수(100점 만점)를 보여줍니다. 최고 점수보다 높으면 갱신합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력받아 새 퀴즈를 등록하고 파일에 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 모든 퀴즈와 선택지, 정답을 보여줍니다. |
| 4 | 점수 확인 | 최고 점수를 보여줍니다. 아직 풀지 않았다면 안내 메시지를 출력합니다. |
| 5 | 종료 | 데이터를 저장하고 프로그램을 종료합니다. |

**입력/예외 처리**
- 입력 앞뒤 공백 제거, 빈 입력·문자 입력·범위 밖 숫자는 안내 후 다시 입력받습니다.
- `Ctrl+C` 또는 입력 종료(EOF) 시 저장 후 안전하게 종료합니다.
- `state.json`이 없으면 기본 퀴즈로 시작하고, 손상되었으면 안내 후 기본 데이터로 복구합니다.

## 🖼️ 실행 화면

**메뉴 / 미응시 상태 점수 확인**

![메뉴](docs/screenshots/menu.png)

**퀴즈 풀기 (랜덤 출제, 결과 및 최고 점수 갱신)**

![퀴즈 풀기](docs/screenshots/play.png)

**퀴즈 추가**

![퀴즈 추가](docs/screenshots/add_quiz.png)

**퀴즈 목록**

![퀴즈 목록](docs/screenshots/list.png)

**점수 확인**

![점수 확인](docs/screenshots/score.png)

**잘못된 입력 처리 (문자 입력, 빈 입력)**

![잘못된 입력](docs/screenshots/invalid_input.png)

**프로그램 재실행 후 데이터 유지** — 추가한 퀴즈를 포함해 9문제가 출제되고, 89점은 기존 최고 점수(100점)보다 낮아 갱신되지 않음

![재실행](docs/screenshots/reload.png)

![재실행 후 점수](docs/screenshots/reload_score.png)

## 📂 파일 구조
```
quiz_game/
├── main.py       # 게임 전체 코드 (Quiz, QuizGame 클래스 + 기본 퀴즈 데이터)
├── state.json    # 퀴즈·최고 점수 저장 파일 (실행 시 자동 생성, Git 추적 제외)
├── .gitignore    # Git에 올리지 않을 파일 목록
├── README.md     # 프로젝트 설명서
└── docs/
    └── screenshots/  # 실행 화면 및 Git 작업 캡처 이미지
```

**main.py 내부 구성**
| 구성 요소 | 역할 |
|---|---|
| `DEFAULT_QUIZZES` | 기본 퀴즈 8개 (state.json이 없거나 손상됐을 때 사용) |
| `Quiz` 클래스 | 문제 1개 표현 — `display()` 출력, `check_answer()` 정답 확인, `to_dict()` / `from_dict()` 저장용 변환 |
| `QuizGame` 클래스 | 게임 전체 관리 — 메뉴, 퀴즈 풀기/추가/목록/점수, 입력 처리(`input_int`), 파일 저장/불러오기 |

## 💾 데이터 파일 설명 (`state.json`)
- **경로:** 프로젝트 루트(`main.py`와 같은 폴더)의 `state.json`
  - 다른 폴더에서 실행해도 항상 이 위치를 사용합니다.
- **역할:** 추가한 퀴즈와 최고 점수를 저장해, 프로그램을 다시 실행해도 데이터가 유지되게 합니다.
- **인코딩:** UTF-8
- **저장 시점:** 퀴즈 풀기 완료, 퀴즈 추가, 종료(또는 `Ctrl+C`) 시
- **Git 추적 제외 이유:** 실행할 때마다 내용이 바뀌는 데이터이므로 `.gitignore`에 등록했습니다. 파일이 없으면 프로그램이 기본 퀴즈로 자동 생성합니다.

**스키마**
```json
{
  "quizzes": [
    {
      "question": "지구에서 가장 큰 대양은?",
      "choices": ["1. 대서양", "2. 인도양", "3. 태평양", "4. 북극해"],
      "answer": 3
    }
  ],
  "best_score": 80,
  "best_correct": 4,
  "best_total": 5
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list[str] | 선택지 4개 |
| `quizzes[].answer` | int | 정답 번호 (1~4) |
| `best_score` | int 또는 null | 최고 점수 (100점 만점). 아직 풀지 않았으면 `null` |
| `best_correct` | int | 최고 점수를 기록했을 때 맞힌 문제 수 |
| `best_total` | int | 최고 점수를 기록했을 때 전체 문제 수 |

**파일 오류 처리**
| 상황 | 동작 |
|---|---|
| 파일 없음 (첫 실행) | 기본 퀴즈 데이터로 시작 |
| JSON 형식이 깨짐 / 구조가 다름 (예: `[]`) | 안내 메시지 출력 후 기본 데이터로 복구하고 파일 다시 저장 |
| 읽기/쓰기 권한 오류 | 안내 메시지 출력 후 계속 실행 |


## 🌿 Git 작업 기록

- **원격 저장소:** https://github.com/Rosalia0416/quiz_game
- **커밋 히스토리:** https://github.com/Rosalia0416/quiz_game/commits/main
- **브랜치:** `main`(배포용), `feature/score`(점수 개선·랜덤 출제 작업용)

### 1) 커밋 히스토리 (`git log --oneline --graph`)
기능 단위로 나눈 의미 있는 커밋 10개 이상, `feature/score` 브랜치가 갈라졌다가 `main`으로 병합된 그래프를 확인할 수 있습니다. 같은 화면에 Python 버전과 Git 사용자 설정도 함께 보입니다.

![git log graph](docs/screenshots/git_log.png)

### 2) 브랜치 생성 → 작업 → 병합
| 순서 | 명령어 | 내용 |
|---|---|---|
| 1 | `git checkout -b feature/score` | `main`에서 작업용 브랜치 생성 후 이동 |
| 2 | `git commit` × 2 | 최고 점수 100점 만점 저장(Fix), 랜덤 출제(Feat) |
| 3 | `git checkout main` | `main` 브랜치로 복귀 |
| 4 | `git merge --no-ff feature/score` | 병합 커밋을 남기며 `main`에 병합 |

**브랜치 생성**

![브랜치 생성](docs/screenshots/git_branch.png)

**병합 결과 그래프**

![브랜치 병합](docs/screenshots/git_merge.png)

### 3) clone / pull 실습
다른 PC에서 작업하는 상황을 가정하여 같은 저장소를 별도 폴더에 복제한 뒤, 변경 사항을 원래 작업 폴더로 가져왔습니다.

| 순서 | 위치 | 명령어 |
|---|---|---|
| 1 | 상위 폴더 | `git clone https://github.com/Rosalia0416/quiz_game.git quiz_game_clone` |
| 2 | `quiz_game_clone` | README에 한 줄 추가 → `git add` → `git commit` → `git push origin main` |
| 3 | `quiz_game` (기존 폴더) | `git pull origin main` → Fast-forward로 변경 사항 반영 확인 |

- clone한 복제 저장소(quiz_game_clone)에서 이 섹션의 원래 내용을 추가하고 push했습니다. (커밋 `b73fc78`)

**복제 저장소(quiz_game_clone)에서 commit → push**

![clone 후 push](docs/screenshots/git_clone_push.png)

**기존 폴더(quiz_game)에서 pull**

![pull](docs/screenshots/git_pull.png)

### 4) Git 기본 명령어 7종 사용 내역
| 명령어 | 사용한 곳 |
|---|---|
| `init` | 프로젝트 최초 생성 시 로컬 저장소 초기화 |
| `add` / `commit` | 기능·수정·문서 작업마다 단위별 커밋 |
| `push` | `main`, `feature/score` 브랜치를 GitHub에 업로드 |
| `pull` | GitHub에서 만든 README 가져오기, clone 실습 변경 사항 가져오기 |
| `checkout` | `feature/score` 브랜치 생성·이동, `main` 복귀 |
| `clone` | `quiz_game_clone` 폴더로 저장소 복제 |
