# ⚙️ CPU 스케줄링 알고리즘

**CPU 스케줄링 알고리즘**의 종류는 매우 다양하며, 운영체제마다 서로 다른 스케줄링 방식을 채택하고 있습니다. 중요한 것은 각각의 알고리즘에서 사용된 **'아이디어'**를 이해하는 것이며, **'용어'**에 집착하지 않는 것이 중요합니다.

---

## 📚 스케줄링 알고리즘의 종류

### 1. 🧱 선입 선처리 스케줄링 (FCFS)
- **First-Come, First-Served (FCFS)**
- 비선점형 스케줄링
- 준비 큐에 **먼저 삽입된 순서대로** CPU 할당
- **호위 현상(Convoy Effect)** 발생 가능:
  - 긴 작업 하나가 앞에 오면 뒤의 짧은 작업들이 오래 기다려야 함

---

### 2. ⏱ 최단 작업 우선 스케줄링 (SJF)
- **Shortest Job First (SJF)**
- CPU 사용 시간이 **가장 짧은 프로세스**부터 실행
- **비선점형**이 기본이지만, 선점형으로도 구현 가능  
  → 선점형 버전은 **최소 잔여 시간 우선 스케줄링(SRT)**  
- **호위 현상 방지**에 효과적

---

### 3. 🔄 라운드 로빈 스케줄링 (RR)
- **선점형** 스케줄링
- 모든 프로세스에게 **타임 슬라이스(time slice)** 부여
- 타임 슬라이스가 끝나면 다음 프로세스로 전환  
  → 작업 미완료 시 **큐 맨 뒤로 이동**
- **타임 슬라이스의 크기**가 성능에 큰 영향
  - 너무 크면 FCFS처럼 작동
  - 너무 작으면 **문맥 교환 비용 증가**

---

### 4. 🧮 최소 잔여 시간 우선 스케줄링 (SRT)
- **Shortest Remaining Time First**
- **SJF의 선점형 버전**
- 현재 실행 중인 프로세스보다 **남은 시간이 짧은 프로세스가 도착**하면 CPU 선점

---

### 5. ⭐ 우선순위 스케줄링
- 각 프로세스에 **우선순위(priority)** 부여
- **가장 높은 우선순위의 프로세스**부터 실행
- **SJF와 SRT도 일종의 우선순위 스케줄링**
- 단점: **기아(starvation)** 현상 발생 가능  
  → 우선순위 낮은 프로세스가 계속 밀릴 수 있음
- 해결책: **에이징(aging)**  
  → 오래 기다린 프로세스의 우선순위를 점차 증가시킴

---

### 6. 🧬 다단계 큐 스케줄링
- **여러 개의 준비 큐** 사용
- 각 큐에 **우선순위 부여**  
  → **우선순위 높은 큐**부터 CPU 할당
- 큐마다 **다른 알고리즘 적용 가능**
- 프로세스는 **특정 큐에 고정**되어 큐 간 이동 없음

---

### 7. 🔁 다단계 피드백 큐 스케줄링
- **다단계 큐 스케줄링의 확장형**
- 프로세스가 **큐 사이를 이동** 가능
- 특징:
  - CPU 사용 시간이 길수록 **낮은 우선순위 큐**로 이동
  - 오래 기다리면 **높은 우선순위 큐로 승격**
- **기아 현상 방지**, **적응형 스케줄링**

---

> 📌 **정리 요약**
>
> | 알고리즘 | 선점 여부 | 주요 특징 |
> |----------|------------|------------|
> | FCFS | ❌ 비선점형 | 단순하지만 호위현상 발생 가능 |
> | SJF | ❌ 비선점형 | 평균 대기 시간 최소, 예측 어려움 |
> | RR | ✅ 선점형 | 응답 시간 개선, 문맥 전환 비용 고려 |
> | SRT | ✅ 선점형 | SJF의 선점형 버전 |
> | 우선순위 | ⭕ 혼합 가능 | 기아 문제 존재, 에이징으로 보완 |
> | 다단계 큐 | ⭕ 혼합 가능 | 프로세스 고정 큐, 분류 편리 |
> | 다단계 피드백 큐 | ✅ 선점형 | 큐 간 이동 가능, 유연한 자원 분배 |

