# === main.py ===
from Classes.book import Book, PrintedBook, EBook
from Classes.catalog_entry import CatalogEntry
from Classes.genre import Genre
from Classes.publisher import Publisher
from Classes.reader import Reader, Student, Teacher
from Classes.librarian import Librarian
from Classes.library_branch import LibraryBranch
from Classes.loan import Loan
from Classes.reservation import Reservation
from Classes.fine import Fine
from Classes.library_system import LibrarySystem
from Classes.repository import Repository


def main():
    print("=== Демонстрация ООП: Наследование, Полиморфизм, Композиция ===\n")

    # 1. Базовые сущности (Композиция)
    genre = Genre("Антиутопия")
    publisher = Publisher("АСТ", "Россия")

    print("1. Базовые сущности:")
    print(f"   Жанр: {genre.get_name()}")
    print(f"   Издательство: {publisher.get_info()}")
    print()

    # 2. Наследование Book + Переопределение методов
    book1 = PrintedBook("Бегущий в лабиринте", "Джеймс Дэшнер", 2015, 328)
    book2 = EBook("Python Guide", "Гвидо", 2020, 5)

    book1.set_genre(genre)
    book1.set_publisher(publisher)

    print("2. Наследование и переопределение (Book):")
    print(f"   Печатная книга: {book1.get_info()}")
    print(f"   Электронная книга: {book2.get_info()}")
    print()

    # 3. Полиморфизм подтипов (позднее связывание)
    print("3. Полиморфизм подтипов (позднее связывание):")
    books: list[Book] = [book1, book2]
    for book in books:
        print(f"   {type(book).__name__}: {book.get_info()}")
    print()

    # 4. Наследование Reader + Переопределение
    student = Student("Иван Петров")
    teacher = Teacher("Мария Иванова")

    print("4. Наследование и переопределение (Reader):")
    print(f"   Студент {student.get_name()} может взять {student.get_books_limit()} книг")
    print(f"   Преподаватель {teacher.get_name()} может взять {teacher.get_books_limit()} книг")
    print()

    # 5. Полиморфизм подтипов (Reader коллекция)
    print("5. Полиморфизм подтипов (Reader коллекция):")
    readers: list[Reader] = [student, teacher]
    for reader in readers:
        print(f"   {type(reader).__name__} {reader.get_name()}: лимит {reader.get_books_limit()} книг")
    print()

    # 6. Выдача книги
    librarian = Librarian("Анна Сергеевна")
    librarian.enable_issue()

    print("6. Выдача книги:")
    success = librarian.issue_book(book1, student)
    print(f"   Библиотекарь {librarian.get_name()} выдала книгу: {'Успешно' if success else 'Ошибка'}")
    print()

    # 7. Loan (Композиция: has-a Book + Reader)
    loan = Loan(book1, student)
    print("7. Композиция (Loan):")
    print(f"   {loan.get_summary()}")
    print(f"   Статус выдачи: {loan.get_status()}")
    print()

    # 8. CatalogEntry (Композиция: has-a Book + Shelf)
    print("8. Композиция (CatalogEntry):")
    catalog_entry = CatalogEntry(book1, "A-13")
    print(f"   {catalog_entry.get_location()}")
    print()

    # 9. Reservation
    reservation = Reservation(book2, teacher)
    print("9. Бронирование:")
    print(f"   {reservation.get_info()}")
    print(f"   Статус: {reservation.get_status()}")
    reservation.cancel()
    print(f"   После отмены: {reservation.get_status()}")
    print()

    # 10. Ad hoc полиморфизм (Fine)
    fine = Fine(10)

    print("10. Ad hoc полиморфизм (Fine):")
    print(f"   Базовый штраф: {fine.calculate()} руб.")
    print(f"   Штраф за 3 дня просрочки: {fine.calculate(3)} руб.")
    
    fine2 = fine + 5          
    fine3 = fine + fine2      
    print(f"   Штраф 10 руб. + 5 руб. = {fine2}")
    print(f"   Штраф 10 руб. + 15 руб. = {fine3}")
    print()

    # 11. Композиция (LibrarySystem)
    branch = LibraryBranch("Центральная библиотека")
    branch.add_book(book1)
    branch.add_book(book2)

    system = LibrarySystem(branch)
    system.add_librarian(librarian)
    system.add_loan(loan)
    system.add_reservation(reservation)

    print("11. Композиция (LibrarySystem):")
    print(f"   {system.get_summary()}")
    print(f"   Всего книг в филиале: {branch.get_books_count()}")
    print()

    # 12. Параметрический полиморфизм (Repository Generic)
    book_repo: Repository[Book] = Repository()
    reader_repo: Repository[Reader] = Repository()
    loan_repo: Repository[Loan] = Repository()

    book_repo.add(book1)
    book_repo.add(book2)
    reader_repo.add(student)
    reader_repo.add(teacher)
    loan_repo.add(loan)

    print("12. Параметрический полиморфизм (Repository[T]):")
    print("   Книги в репозитории:")
    for b in book_repo.get_all():
        print(f"       {b.get_info()}")
    print("   Читатели в репозитории:")
    for r in reader_repo.get_all():
        print(f"       {r.get_name()}")
    print("   Выдачи в репозитории:")
    for l in loan_repo.get_all():
        print(f"       {l.get_summary()}")
    print()

    print("========== Конец демонстрации ==========")


if __name__ == "__main__":
    main()