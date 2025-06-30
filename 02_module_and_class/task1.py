# 학생 관리 시스템 과제
## 문제 1: 기본 학생 클래스 만들기
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def study(self, hours):
        print(f"{self.name}이(가) {hours}시간 동안 공부했습니다.")

# 아래 코드는 이 파일이 '직접' 실행될 때만 동작합니다.
if __name__ == "__main__":

# 위의 Student 클래스를 사용하여 학생 객체를 생성하고 study 메서드를 호출해보세요.
# 이름, 나이 , 학년 = 홍박사, 15, 2
# YOUR CODE HERE
    dr_hong = Student('홍박사', 15, 2)
    dr_hong.study(24)
