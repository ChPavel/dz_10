import json

class Candidates:
    def __init__(self, url):
        self.url = url

    def load_date(self):
        '''
        Метод принимает файл JSON формата, читает, преобразует прочитанное в формат Python.
        :return: list.
        '''
        with open(self.url, 'r', encoding='utf-8') as file:
            candidates = list(json.loads(file.read()))
        return candidates

    def oll(self):
        '''
        Метод формирует из списка, полученного с помощью метода load_date, строку с нужными данными.
        :return: str (информация о всех кандидатах).
        '''
        oll_candidates = ""
        candidates = self.load_date()

        for candidate in candidates:
            name = candidate['name']
            position =  candidate['position']
            skills = candidate['skills']
            oll_candidates += (f'{name}\n{position}\n{skills}\n\n')

        return oll_candidates

    def choiсe(self, pk):
        '''
        Метод выбирает из списка, полученного с помощью метода load_date, нужный элемент по номеру и
        и возвращает в виде строки, если номера нет в списке - выводит соответствуещее сообщение.
        :param pk: int (порядковый номер кандидата в базе).
        :return: str (информация о выбранном кандидате).
        '''
        candidates = self.load_date()

        for candidate in candidates:
            picture = f"<img src=\"{candidate['picture']}\">"
            name = candidate['name']
            position = candidate['position']
            skills = candidate['skills']
            if pk == candidate['id']:
                choiсe = (f'{picture}\n{name}\n{position}\n{skills}\n\n')
                break
            else:
                choiсe = f'База содержит всего {len(candidates)} кандидатов'

        return choiсe

    def choiсe_skills(self, skill):
        '''
        Метод выбирает из списка, полученного с помощью метода load_date, информацию о кандидатах, имеющих
        заданный навык и выводит в виде строки, если навыка нет в списке - выводит соответствуещее сообщение.
        :param skill: str (искомый навык)
        :return: str (информация о подходящих кандидатах)
        '''
        candidates_with_skills = ''
        candidates = self.load_date()

        for candidate in candidates:
            name = candidate['name']
            position = candidate['position']
            skills = candidate['skills'].strip().lower().split(', ')
            if skill.lower() in skills:
                candidates_with_skills += (f'{name}\n{position}\n{candidate["skills"]}\n\n')

        if candidates_with_skills == '':
            candidates_with_skills = f"Среди кандидатов нет специалистов с навыком '{skill}'."
        return candidates_with_skills