import pytest
from main import TicTacToeBuggy

# 1. Створюємо фікстуру для ініціалізації гри
@pytest.fixture
def game():
    return TicTacToeBuggy()

# 2. Використовуємо параметризацію для перевірки ходів у різні позиції
@pytest.mark.parametrize("index", [0, 4, 8])
def test_make_move_logic(game, index):
    # Перевіряємо, що після ходу в клітинку там з'являється символ
    game.make_move(index)
    assert game.board[index] == "X"
    # Перевіряємо, що хід перейшов до наступного гравця
    assert game.current_player == "O"

# 3. Переписуємо існуючі тести з використанням фікстури
def test_initialization(game):
    assert len(game.board) == 9, "Поле має містити 9 елементів"
    assert all(slot == " " for slot in game.board), "Поле має бути порожнім"

def test_starting_player(game):
    assert game.current_player == "X", "Першим має ходити X"

def test_move_to_occupied_cell_raises_error(game):
    game.make_move(0)  # Перший хід в клітинку 0
    # Очікуємо, що повторний хід туди ж викликає помилку
    with pytest.raises(ValueError):
        game.make_move(0)

@pytest.mark.skip(reason="Функціонал мережевої гри ще не реалізовано")
def test_network_multiplayer(game):
    # Цей код ніколи не запуститься
    assert game.connect_to_server() is True

@pytest.mark.xfail(reason="Баг: індикатор ходу не оновлюється при нічиї")
def test_turn_label_after_draw(game):
    # Імітуємо ситуацію нічиєї
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", " "]
    game.make_move(8) # Останній хід
    assert game.turn_label.cget("text") == "Гра завершена"

# 6. Помилковий тест
def test_forced_failure(game):
    game.current_player = "X"
    # Навмисно очікуємо "O", хоча знаємо, що там "X"
    assert game.current_player == "O", "Тест впав: очікували 'O', але залишився 'X'"