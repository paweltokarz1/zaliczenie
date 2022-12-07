import pytest
from engine import Engine
from validator import Validator
from stats import Stats
from menu import Menu
from dictionary import Dictionary

engine = Engine()
validator = Validator()
stats = Stats()
menu = Menu()
dictionary = Dictionary()


@pytest.mark.parametrize("test_input, expected", [(3, 3), (2, 2), (1, 1)])
def test_shoudl_return_numbers_of_tries(test_input, expected):
    assert engine.proby(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("ziemniak", False), ("gniazdo", True)])
def test_shoudl_check_word_is_isogram(test_input, expected):
    assert validator.is_isogram(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("StRUś", "struś"), ("gnIaZdo", "gniazdo")])
def test_shoudl_lower_case_in_word(test_input, expected):
    assert validator.lower_case(test_input) == expected

def test_shoudl_return_initial_cows():
    assert stats.cows == 0

def test_shoudl_return_initial_bulls():
    assert stats.bulls == 0

def test_print_menu():
    assert menu.print_menu(menu.menu_options) == {
        1: "Nowa gra",
        2: "Zasady gry",
        3: "Zmień ilość prób",
        4: "Koniec",
    }

def test_shoudl_check_that_method_random_word_is_working_propertly():
    assert dictionary.random_word() != "awwrhwrhwrhwr"

def test_initial_word_from_user():
    assert engine.word_from_user == ""
