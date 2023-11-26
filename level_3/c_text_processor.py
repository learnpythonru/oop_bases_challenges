"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он
       возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные
       методы.
"""


class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        return f'{super().summarize()}, total number of words in the text: {len(self.text.split())}' # noqa


if __name__ == '__main__':
    text_processor = TextProcessor('cat dog panda')
    text_processor.to_upper()
    text_processor.summarize()
    advanced_text_processor = AdvancedTextProcessor('cat dog panda')
    advanced_text_processor.to_upper()
    advanced_text_processor.summarize()
