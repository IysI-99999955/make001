from analizer import TextAnalyzer, NewTextAnalyzer, AdvancedTextAnalyzer, AdvancedTextAnalyzer2

# test.txt 생성
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("hello world hello python world hello")

# 사용 예시
analyzer = TextAnalyzer('test.txt')
print("총 단어 수:", analyzer.word_count())
print("가장 많이 나온 단어:", analyzer.most_common_word())

## 2. 특정 단어 카운팅하기
new_analyzer = NewTextAnalyzer('test.txt')
new_word = "hello"
print(f"{new_word} 단어 수:", new_analyzer.word_count(new_word))

## 3. 새로운 객체 만들기
analyzer = AdvancedTextAnalyzer('test.txt')

## 4. 가장 긴 단어 찾기
print("가장 긴 단어:", analyzer.longest_word())

    
# 클래스 사용
analyzer = AdvancedTextAnalyzer2('test.txt')
print("전체 단어 수 + 'hello' 횟수:", analyzer.word_count_with_target('hello'))