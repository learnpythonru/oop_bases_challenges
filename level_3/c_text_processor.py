"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        return f'Total text length: {len(self.text)}, total number of words in the text: {sum(1 for x in self.text.split())}'


if __name__ == '__main__':
    text_1 = TextProcessor('Today is a difficult day for all of us')
    print(text_1.text)
    print(text_1.to_upper())
    print(text_1.summarize())
    text_2 = AdvancedTextProcessor('Tomorrow will be much more difficult than today')
    print(text_2.text)
    print(text_2.to_upper())
    print(text_2.summarize())
    print(text_1.summarize())
