import pytest
from main import count_vowels

@pytest.mark.parametrize("s, expected", [
    ("aeiouyAEIOUY", 12),
    ("АаЕеЁёИиОоУуЫыЭэЮюЯя", 20),
    ("bcdfg", 0),
    ("The SUn risEs", 4),
    ("Cats And dOgs", 3),
    ("I like boOks", 5),
    ("СолнцЕ встАёт", 4),
    ("Кошки и сОбаки", 6),
    ("Я лЮблю кнИги", 5),
])

def test_count_vowels(s, expected):
    assert count_vowels(s) == expected

if __name__ == "__main__":
    pytest.main()