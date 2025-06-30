# TextAnalyzer 클래스 정의
class TextAnalyzer:
    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            # self.text = "hello world hello python world hello"
            self.text = f.read()

    def word_count(self):
        return len(self.text.split())

    def most_common_word(self):
        from collections import Counter
        words = self.text.split()
        return Counter(words).most_common(1)[0]
    
## 1. class 수정하기 - 함수 추가하기
# TextAnalyzer 클래스 상속받아서 단어 숫자세는 함수 추가하기
class NewTextAnalyzer(TextAnalyzer):
    def word_count(self,target_word):
        return self.text.split().count(target_word)


## 1. 위에서 구현했던 TextAnalyzer 상속받아서 AdvancedTextAnalyzer 만들기
class AdvancedTextAnalyzer(TextAnalyzer):
    ## 2. AdvancedTextAnalyzer 클래스에 메서드 longest_word 구현하기
    def longest_word(self):
        words = self.text.split() # list
        longest = max(words, key=len)
        return longest
    

# 1. 기존 AdvancedTextAnalyzer 에서 word_count_with_target 수정하기
class AdvancedTextAnalyzer2(TextAnalyzer):
    # 2. word_count_with_target 수정, target_word 를 받아와야함
    def word_count_with_target(self,target_word):
        # 3. super 를 활용하여 기존 메서드 (word_count) 불러와 수정하기
        total = super().word_count()
        count = self.text.split().count(target_word)
        return total, count