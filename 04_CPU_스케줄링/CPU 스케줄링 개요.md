# 🧠 CPU 스케줄링 개요

운영체제가 **프로세스들에게 공정하고 효율적으로 CPU 자원을 배분**하는 것을 **CPU 스케줄링**이라 합니다. 이는 컴퓨터 성능에 매우 큰 영향을 미치는 핵심 요소입니다.

---

## 🔢 프로세스 우선순위

- 프로세스마다 **우선순위(priority)** 존재
- **입출력 집중 프로세스**: 입출력 작업 비중이 큼  
  → 주로 **대기 상태**에 머무름
- **CPU 집중 프로세스**: 연산 중심, CPU 작업 비중이 큼  
  → 주로 **실행 상태**에 머무름

> 💡 모든 프로세스에게 동일하게 CPU를 배분하기보다는,  
> **성격(입출력/CPU 집중)에 맞게 자원을 분배하는 것이 더 효율적**

운영체제는 각 프로세스의 **PCB(Process Control Block)**에 우선순위를 명시하고,  
**우선순위가 높은 프로세스**를 더 빠르게, 더 자주 실행시킴.

---

## 📋 스케줄링 큐

운영체제는 각 자원(CPU, 메모리, I/O 등)에 대해 **대기열(큐)**을 관리함.

### 대표적인 큐
| 큐 이름     | 설명 |
|------------|------|
| **준비 큐** | CPU를 사용하려고 기다리는 프로세스들이 줄 서는 곳 |
| **대기 큐** | 입출력 장치 사용을 기다리는 프로세스들이 줄 서는 곳 |

- 준비 상태 프로세스는 준비 큐에 삽입되어 **CPU 사용을 기다림**
- 대기 상태 프로세스는 입출력 완료 후 준비 상태로 바뀌며 **준비 큐로 이동**

---

## ⚖️ 선점형 vs 비선점형 스케줄링

| 구분 | 선점형 스케줄링 | 비선점형 스케줄링 |
|------|----------------|------------------|
| 자원 회수 | 가능 (운영체제가 강제로 회수) | 불가능 (프로세스가 스스로 반납할 때까지 기다림) |
| 장점 | 자원 독점 방지, 응답성 향상 | 문맥 교환 비용 적음 |
| 단점 | 문맥 교환 비용 발생 | 급한 프로세스도 대기 필요 |
| 사용 예시 | 실시간 시스템, 다중 사용자 환경 | 배치 작업, 단순 시스템 |

- **선점형**: 자원을 사용 중인 프로세스에게서 운영체제가 **자원을 강제로 회수**
- **비선점형**: 자원을 사용 중인 프로세스를 **끝까지 기다림**

> ⚠️ 선점형은 더 유연하지만 문맥 교환 오버헤드가 있고,  
> 비선점형은 자원 효율은 떨어지지만 단순하고 예측 가능함.

---
