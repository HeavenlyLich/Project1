from main import TicTacToeBuggy


def test_logic():
    game = TicTacToeBuggy()

    # Тест 1: Перевірка ініціалізації поля (має бути 9 порожніх клітинок)
    assert len(game.board) == 9, "Поле має містити 9 елементів"
    assert all(slot == " " for slot in game.board), "Поле має бути порожнім при старті"

    # Тест 2: Перевірка початкового гравця
    assert game.current_player == "X", "Першим має ходити X"

    print("Прості тести assert пройдені успішно!")


if __name__ == "__main__":
    test_logic()

