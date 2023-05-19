import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='sort_log.log',
                    filemode='w',
                    encoding='utf-8')
INPUT_FILE = 'user_support_letters.csv'
OUTPUT_FILE = 'sorted_cat.csv'
CATEGORIES = {
              'Security': ['пароль',
                           'выйти',
                           'аккаунт', ],

              'Refunds': ['верн',
                          'возвр',
                          'отпис',
                          'деньги',
                          'гроші',
                          'отменить', ],

              'Troubleshooting': ['не могу',
                                  'неправильно',
                                  'проблем',
                                  'медленно',
                                  'когда',
                                  'не заходит',
                                  'не работает',
                                  'ошиб',
                                  'завис',
                                  'скорость',
                                  'почин', ],

              'Account': ['регистрация'],

              'Advertising and Collaboration': ['реклам',
                                                'сотруд'],

              'Limits': ['сколько', 'лимит'],
              'Payments': ['плат',
                           'налич', ],

              'Features': ['формат',
                           'функциональность',
                           'можно ли',
                           'решение',
                           'функция',
                           'как',
                           'автоматич',
                           'максималь',
                           'антиплагиат',
                           'версия', ],
             }


def sort_categories(questions: list[str]) -> list[tuple[str, set]]:
    """Lists messages and their categories."""
    result = []
    for question in questions:
        result.append(choose_category(question))
    return result


def choose_category(message: str) -> tuple[str, set]:
    """Returns tuple of message and set of categories."""
    quest_categ = set()
    for k, v in CATEGORIES.items():
        for word in v:
            if word in message.lower():
                quest_categ.add(k)
    if len(quest_categ) == 0:
        logging.debug(f"Unsorted data: {message}")
    else:
        return (message, quest_categ)


def get_data_csv(filename: str) -> list[str]:
    """Returns a list of messages from users."""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line.rstrip('\n'))
    except FileNotFoundError:
        logging.error('Файл не найден')
    return data


def save_data(results: list,
              filename: str,) -> None:
    """Stores sort results."""
    with open(filename, 'w', encoding='utf-8') as file:
        for question in results:
            file.write(f'{question[0]} | {question[1]} \n')


def main():
    """The main function of the file."""
    database = get_data_csv(INPUT_FILE)
    if not database:
        logging.error('Работа завершена некорректно.')
        return
    sorted_cat = sort_categories(database)
    if len(database) == len(sorted_cat):
        logging.info('Работа завершена успешно.')
    elif len(database) > len(sorted_cat):
        logging.warning('Имеются несортированные сообщения')
    else:
        logging.warning('Некоторые данные были утеряны')
    save_data(sorted_cat, OUTPUT_FILE)


if __name__ == '__main__':
    logging.info('Работа начата')
    main()
