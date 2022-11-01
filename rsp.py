import random
Hand = int

ROCK = 0
SCISSORS = 1
PAPER = 2


def is_a_winning_b(a: Hand, b: Hand) -> bool:
    return (a - b) % 3 == 2


def is_a_losing_b(a: Hand, b: Hand) -> bool:
    if a != b:
        return (a - b) % 3 != 2
    else:
        return False


def is_a_equal_b(a: Hand, b: Hand) -> bool:
    return a == b


KOREAN = 'korean'
MGB = 'mgb'
ENGLISH = 'english'
JAPANESE = 'japanese'
CHINESE = 'chinese'


LANGUAGE_TABLE = {
    KOREAN: ['바위', '가위', '보'],
    MGB: ['묵', '찌', '빠'],
    ENGLISH: ['ROCK', 'SCISSORS', 'PAPER'],
    JAPANESE: ['グー', 'チョキ', 'パー'],
    CHINESE: ['石头',  '剪刀', '布']
}

Language = str


def stringify(hand: Hand, language: Language = KOREAN) -> str:
    return LANGUAGE_TABLE[language][hand]


def random_choice() -> Hand:
    return random.randrange(0,3)
