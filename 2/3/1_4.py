'''
поток, который для указанного текстового файла создает его копию с заменой одного текста на другой.
'''

import threading


class ReplaceThread(threading.Thread):

    def __init__(self, file: str, old_text: str, new_text: str):
        super().__init__()
        self._file = file
        self._old_text = old_text
        self._new_text = new_text
        name, suf = self._file.rsplit(".")
        self._new_file = f"{name}_new.{suf}"

    def run(self):
        with open(self._file, encoding="utf-8") as source, open(self._new_file, "w", encoding="utf-8") as store:
            for line in source:
                content = line.replace(self._old_text, self._new_text)
                store.write(content)