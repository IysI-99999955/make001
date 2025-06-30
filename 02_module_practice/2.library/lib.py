# 도서 클래스
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}"
    

# 도서관 클래스

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("✅ 책이 추가되었습니다.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("🗑️ 책이 삭제되었습니다.")
                return
            print("❌ 해당 책을 찾을 수 없습니다.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("🔍 책을 찾았습니다:")
                print(book)
                return
        print("❌ 해당 책이 없습니다.")

    def list_books(self):
        if not self.books:
            print("📚 등록된 책이 없습니다.")
        else:
            print("📚 도서 목록:")
            for book in self.books:
                print(book)


class BaseLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("✅ 책이 추가되었습니다.")

    def remove_book(self, title):
        if title not in [b.title for b in self.books]:
            print("해당 책은 현재 도서관에 없습니다.")
        else:
            self.books = [b for b in self.books if b.title != title]
            print(f"🗑️{title} 삭제 시도 완료")
    

    def search_book(self, title):
        for b in self.books:
            if b.title == title:
                print("🔍 책을 찾았습니다:", b)
                return b # Book 객체 반환
        print("❌ 책이 없습니다.")
        return None

    def list_books(self):
        if not self.books:
            print("📚 등록된 책이 없습니다.")
        for b in self.books:
            print(b)


class User:
    def __init__(self, username, passwrod):
        self.username = username
        self.password = passwrod

# 유저 정보 찾는 함수 만들기(find_user)
class AuthLibrary(BaseLibrary):
    def __init__(self):
        super().__init__()
        self.users = []

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None #모든 유저정보에 대해 매칭이 안될 때
    
    # 유저 등록 함수 만들기
    def register_user(self, username, password):
        if self.find_user(username):
            return False
        self.users.append(User(username, password))
        return True
    
    # Login 함수 만들기
    def login(self, username, password):
        user = self.find_user(username)
        if user and user.password == password:
            return True
        else:
            return False

# 1. 로그인기능이 있는 AuthLibrary 상속받아 대출 기능 추가한 LonLibrary 만들기
class LoanLibrary(AuthLibrary):
    def __init__(self):
        super().__init__()
        self.loans = {}    # {username: [Book, ...]}

    # 2. 책 빌리는 행위를 함수로 만들어주기 : 유저, 책정보
    def borrow_book(self, username, title):
        book = self.search_book(title)
        if book:
            self.books.remove(book)
            self.loans.setdefault(username, []).append(book)
            print("📦 대출 완료")
        else:
            print("❌ 책 없음")

    # 3. 책을 반납받는 행위 함수로 만들어주기 : 유저, 책정보
    def return_book(self, username, title):
        if username not in self.loans:
            print("❌ 대출 기록 없음")
            return None  # 함수 종료 (None 반환)

        for book in self.loans.get(username, []):
            if book.title == title:
                self.loans[username].remove(book)
                self.books.append(book)
                print("📥 반납 완료")
                return None # 함수 종료 (None 반환)
        print("❌ 반납 대상 아님")