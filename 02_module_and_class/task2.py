from task1 import Student

## 문제 2: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
        
    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요. 
        # 기본점수 : 60점, 최대 추가 점수 : 40점 
        # 최대 공부시간 8시간으로 시간에 비례해서 점수 추가
        # YOUR CODE HERE
        base_score = 60
        max_add_score = 40
        max_studytime = 8

        add_score_ratio = hours / max_studytime
        calculated_additional_score = max_add_score * add_score_ratio
        total_score = base_score + calculated_additional_score
        self.add_score(total_score)
# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
# 아래 코드는 이 파일이 '직접' 실행될 때만 동작합니다.
if __name__ == "__main__":

    student1 = GradedStudent("홍길동", 16, 3)
    student2 = GradedStudent("김철수", 14, 1)

    student1.add_score(70)
    student1.add_score(100)
    student1.study(1)
    student1.study(5)

    student2.add_score(85)
    student2.add_score(50)
    student2.study(2)
    student2.study(6)

    print(f"{student1.name}의 총 점수는{student1.scores}이며, 평균은 {student1.calculate_average()} 입니다.")
    print(f"{student2.name}의 총 점수는{student2.scores}이며, 평균은 {student2.calculate_average()} 입니다.")
