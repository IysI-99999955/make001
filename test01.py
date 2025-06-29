print("hello My eyes")
print("이하는 과제 task3 소스로 레포용으로 붙여봄")

from task2 import GradedStudent

## 문제 3: 다중 상속을 이용한 운동선수 학생 클래스
class Athlete:
    def __init__(self, sport):
        self.sport = sport
    
    def train(self, hours):
        print(f"{self.sport} 종목에서 {hours}시간 동안 훈련했습니다.")

class StudentAthlete(GradedStudent, Athlete):
    def __init__(self, name, age, grade, sport):
        # GradedStudent와 Athlete의 __init__ 메서드를 모두 호출하세요.
        # YOUR CODE HERE
        super().__init__(name, age, grade)
        Athlete.__init__(self, sport)
    
    def study(self, hours):
        # GradedStudent의 study 메서드를 호출하고, 추가로 train 메서드도 호출하세요. 이때 훈련은 공부시간의 절반만큼 훈련
        # YOUR CODE HERE
        super().study(hours)
        training_hours = hours / 2
        self.train(training_hours)
# StudentAthlete 클래스의 객체를 생성하고 study 메서드를 호출해보세요.
# YOUR CODE HERE
student1 = StudentAthlete("ys", 99, 2, "F1")

print(f"이름: {student1.name}, 종목: {student1.sport}")
# print("-" * 40)
student1.study(10)
student1.study(20)
print(f"\n{student1.name}의 총 점수는 {student1.scores}이며, 평균은 {student1.calculate_average():.2f} 입니다.")
