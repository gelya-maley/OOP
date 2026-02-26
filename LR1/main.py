from Classes.genre import Genre
from Classes.publisher import Publisher
from Classes.book import Book
from Classes.reader import Reader
from Classes.librarian import Librarian
from Classes.loan import Loan
from Classes.reservation import Reservation
from Classes.fine import Fine
from Classes.library_branch import LibraryBranch
from Classes.catalog_entry import CatalogEntry


def main():
    print("=== Демонстрация ООП: Инкапсуляция ===")
    print()

    # 1. Создание базовых сущностей
    print("1. Создание базовых сущностей:")
    genre = Genre("Антиутопия")
    print(f"   Жанр: {genre.get_name()}")

    publisher = Publisher("АСТ", "Россия")
    print(f"   Издательство: {publisher.get_info()}")

    book = Book("Бегущий в лабиринте", "Дэшнер Джеймс", 2015)
    book.set_genre(genre)
    book.set_publisher(publisher)
    print(f"   Книга: {book.get_info()}")
    print()

    # 2. Сценарий выдачи книги
    print("2. Выдача книги:")
    reader = Reader("Иван Петров")
    librarian = Librarian("Мария Ивановна")
    librarian.enable_issue()

    branch = LibraryBranch("Центральная библиотека")
    branch.add_book(book)

    catalog = CatalogEntry(book, "A-13")

    print(f"   Библиотекарь: {librarian.get_name()}")
    print(f"   Читатель: {reader.get_name()}")
    print(f"   Книга: {book.get_info()}")
    
    success = librarian.issue_book(book, reader)
    if success:
        print("   Результат: Успешно выдана")
    else:
        print("   Результат: Ошибка выдачи")
    
    print(f"   Книг у читателя: {reader.get_books_count()}")
    print(f"   Доступность книги: {book.is_available()}")
    print()

    # 3. Создание записи о выдаче
    print("3. Регистрация выдачи:")
    loan = Loan(book, reader)
    print(f"   {loan.get_summary()}")
    print(f"   Статус: {loan.get_status()}")
    print()

    # 4. Сценарий возврата
    print("4. Возврат книги:")
    reader.return_book(book)
    loan.mark_returned()
    print(f"   Статус выдачи: {loan.get_status()}")
    print(f"   Доступность книги: {book.is_available()}")
    print()

    # 5. Сценарий брони
    print("5. Бронирование:")
    reader2 = Reader("Анна Смирнова")
    reservation = Reservation(book, reader2)
    print(f"   {reservation.get_info()}")
    print(f"   Статус брони: {reservation.get_status()}")
    reservation.cancel()
    print(f"   Статус после отмены: {reservation.get_status()}")
    print()

    # 6. Сценарий штрафа
    print("6. Штраф:")
    fine = Fine(50)
    print(f"   {fine.get_info()}")
    fine.pay()
    print(f"   После оплаты: {fine.get_info()}")
    print()

    # 7. Информация о филиале и каталоге
    print("7. Информация о филиале:")
    print(f"   Название: {branch.get_name()}")
    print(f"   Книг в фонде: {branch.get_books_count()}")
    print(f"   {catalog.get_location()}")
    print()

     # 8. Тест валидации (Защита состояния)
    print("8. Проверка валидации данных:")
    try:
        bad_fine = Fine(-100)
    except ValueError as e:
        print(f"    Fine поймал ошибку: {e}")
    
    try:
        book = Book("Тест", "Автор", 2020)
        book.set_year(150)
    except ValueError as e:
        print(f"    Book поймал ошибку: {e}")
    
    try:
        reader = Reader("")
    except ValueError as e:
        print(f"    Reader поймал ошибку: {e}")
    print()

    # 9. Проверка инкапсуляции
    print("9. Проверка доступа к приватным полям:")
    print()
    
    print("   Проверка 1: Попытка доступа к book.__title")
    try:
        value = book.__title
        print(f"   Доступ разрешён (значение: {value})")
    except AttributeError as e:
        print(f"   Ошибка: {e}")
        print("   Вывод: поле защищено ")
    print()
    
    print("   Проверка 2: Попытка доступа к reader.__books")
    try:
        value = reader.__books
        print(f"   Доступ разрешён (значение: {value})")
    except AttributeError as e:
        print(f"   Ошибка: {e}")
        print("   Вывод: поле защищено ")
    print()
       
    print("   Проверка 3: Попытка доступа к fine.__paid")
    try:
        value = fine.__paid
        print(f"   Доступ разрешён (значение: {value})")
    except AttributeError as e:
        print(f"   Ошибка: {e}")
        print("   Вывод: поле защищено ")
    print()
        
    print("=== Конец демонстрации ===")


if __name__ == "__main__":
    main()