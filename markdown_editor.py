class ExitException(Exception):
    pass


class MarkdownEditor:
    marks = {'header': "#",
             'bolt': "**",
             'italic': "*",
             'crossed': "~~",
             'inline_code': "`",
             'new_line': "\n",
             }
    formats = ("plain", "bold", "italic", "header", "link", "inline-code",
               "ordered-list", "unordered-list", "new-line", "crossed")
    commands = ("!help", "!done")

    def __init__(self):
        self.text = []

    def __str__(self):
        return "".join(self.text)

    def plain_text(self, text):
        """adds text without changing it"""
        self.text.append(text)

    def bolt(self, str_line):
        """adds to textlist text in bolt format **bolt**"""
        self.text.append(self.marks['bolt'] + str_line + self.marks['bolt'])

    def italic(self, str_line):
        """adds to textlist text in italic format *italic*"""
        self.text.append(self.marks['italic'] + str_line + self.marks['italic'])

    def crossed(self, str_line):
        """adds to textlist text in crossed format ~~crossed~~"""
        self.text.append(self.marks['crossed'] + str_line + self.marks['crossed'])

    def inline_code(self, str_line):
        """adds to textlist text in inline code format `inline_code`"""
        self.text.append(self.marks['inline_code'] + str_line + self.marks['inline_code'])

    def link(self, link_header, link):
        """adds to textlist text in link format [link_header](link)"""
        self.text.append(f"[{link_header}]({link})")

    def heading(self, heading, level):
        """adds to textlist text in link format [link_header](link)"""
        if len(self.text) == 0 or self.text[-1] == "\n":
            text = self.marks['header'] * level + " " + heading + self.marks['new_line']
        else:
            text = self.marks['new_line'] + self.marks['header'] * level + " " + heading + self.marks['new_line']
        self.text.append(text)

    def lists_maker(self, rows_num: int, ordered=True):
        """adds to textlist list, if ordered parameter is True, adds numbered list. Else adds pointed list."""
        if ordered:
            lst = [f"{num}. {input(f'Row #{num}: ')}" for num in range(1, rows_num + 1)]
        else:
            lst = [f"* {input(f'Row #{num}: ')}" for num in range(1, rows_num + 1)]
        self.text.append("\n".join(lst) + "\n")

    def new_line(self):
        """adds newline to textlist (\n)"""
        self.text.append(self.marks['new_line'])

    def help(self):
        """help menu prints available formatters and menu commands"""
        print("Available formatters:", " ".join(self.formats))
        print("Special commands:", " ".join(self.commands))

    @staticmethod
    def input_rows_num():
        """Checks input to be greater than zero"""
        while True:
            row_num = int(input("Number of rows: "))
            if row_num <= 0:
                print("The number of rows should be greater than zero")
                continue
            else:
                break
        return row_num

    def write_to_file(self):
        """This method writes all text from textlist to output.md file."""
        with open("output.md", "w") as file:
            file.write(self.__str__())

    @staticmethod
    def input_header_level():
        """Takes from input header level and checks it for being from 1 to 6"""
        while True:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 6:
                break
            else:
                print("The level should be within the range of 1 to 6")
                continue
        return lvl

    @staticmethod
    def link_parameters():
        """Takes from input Label and URL parameter and return"""
        label = input("Label: ")
        link = input("URL: ")
        return label, link

    @staticmethod
    def input_text():
        """Takes text from the input."""
        text = input("Text: ")
        return text

    @staticmethod
    def done():
        """Method that exits program"""
        raise ExitException

    def text_menu(self):
        """That part of class implements text menu for a user"""
        while True:
            try:
                command = input("Choose a formatter:")
                if (command not in self.commands) and (command not in self.formats):
                    print("Unknown formatting type or command")
                elif command == "!help":
                    self.help()
                elif command == "!done":
                    self.write_to_file()
                    self.done()
                elif command == "plain":
                    text = self.input_text()
                    self.plain_text(text)
                    print(self.__str__())
                elif command == "bold":
                    text = self.input_text()
                    self.bolt(text)
                    print(self.__str__())
                elif command == "italic":
                    text = self.input_text()
                    self.italic(text)
                    print(self.__str__())
                elif command == "inline-code":
                    text = self.input_text()
                    self.inline_code(text)
                    print(self.__str__())
                elif command == "crossed":
                    text = self.input_text()
                    self.crossed(text)
                    print(self.__str__())
                elif command == "link":
                    label, link = self.link_parameters()
                    self.link(label, link)
                    print(self.__str__())
                elif command == "header":
                    level = self.input_header_level()
                    header_text = self.input_text()
                    self.heading(header_text, level)
                    print(self.__str__())
                elif command == "ordered-list":
                    rows_num = self.input_rows_num()
                    self.lists_maker(rows_num)
                    print(self.__str__())
                elif command == "unordered-list":
                    rows_num = self.input_rows_num()
                    self.lists_maker(rows_num, ordered=False)
                    print(self.__str__())
                elif command == "new-line":
                    self.new_line()
                    print(self.__str__())
            except ExitException:
                break


if __name__ == '__main__':
    m = MarkdownEditor()
    m.text_menu()
