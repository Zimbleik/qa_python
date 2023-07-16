import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_get_book_rating_book_doesnt_exist_book(self):

        """ Проверка рейтинга недобавленной книги. Ожидаемый результат: None """

        book = BooksCollector()
        assert book.get_book_rating('Книга') is None

    def test_set_book_rating_one_book_rating(self):

        """ Присвоение книге рейтинга. Ожидаемый результат: Книге присвоен рейтинг """

        book = BooksCollector()
        book.add_new_book("Книга")
        book.set_book_rating('Книга', 6)

        assert book.get_book_rating("Книга") == 6

    def test_get_books_with_specific_rating_one_book_specific_rating(self):

        """ Добавление книги со специфическим рейтингом в список. Ожидаемый результат: книга присутствует в списке books_with_specific_rating """

        book = BooksCollector()
        book.add_new_book("Книга")
        book.add_new_book("Книженция")
        book.set_book_rating('Книга', 6)
        book.set_book_rating('Книженция', 16)
        books_with_specific_rating = book.get_books_with_specific_rating(6)

        assert books_with_specific_rating == ['Книга']

    def test_add_book_in_favorites_add_one_book(self):

        """ Добавление Книги в список favorites. Ожидаемый результат: Книга присутствует в списке """

        book = BooksCollector()
        book.add_new_book("Книга")
        book.add_book_in_favorites("Книга")
        favorites_books = book.get_list_of_favorites_books()

        assert 'Книга' in favorites_books

    def test_delete_book_from_favorites_delete_one_book(self):

        """ Удаление Книги из списка favorites. Ожидаемый результат: Книга отсутсвует в списке """

        book = BooksCollector()
        book.add_new_book("Книга")
        book.add_book_in_favorites("Книга")
        book.delete_book_from_favorites("Книга")
        favorites_books = book.get_list_of_favorites_books()

        assert "Книга" not in favorites_books

    def test_add_book_in_favorites_add_nonexistent_book(self):

        """ Попытка добавить книгу в список favorites, если её нет в словаре books_rating. Ожидаемый результат: пустой список get_list_of_favorites_books """

        book = BooksCollector()
        book.add_book_in_favorites('Книга')
        assert len(book.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_empty_favorites_books(self):

        """ Проверка вызова метода get_list_of_favorites_books без добавленных книг. Ожидаемый результат: пустой список """

        book = BooksCollector()
        assert len(book.get_list_of_favorites_books()) == 0

    def test_get_books_with_specific_rating_rating_doesnt_exist(self):

        """ Попытка найти книги с несуществующим рейтингом. Ожидаемый результат: пустой список """

        book = BooksCollector()
        book.add_new_book('Книга с рейтингом 9')
        assert len(book.get_books_with_specific_rating(5)) == 0

    @pytest.mark.parametrize("param", [0, 11])
    def test_set_book_rating_set_book_rating_0_or_11(self, param):

        """ Проверка приграничного значения рейтинга. Попытка установить рейтинг 0 и 11. Ожидаемый результат: рейтинг равен 1 """

        book = BooksCollector()
        book.add_new_book('Книга с приграничным рейтингом')
        book.set_book_rating('Книга с приграничным рейтингом', param)
        assert book.get_book_rating('Книга с приграничным рейтингом') == 1
