from argparse import ArgumentParser


class ParserSubclass(ArgumentParser):

    def __init__(self, **kwargs):
        super().__init__(
            prog='sample-directive-class',
            description='Support SphinxArgParse HTML testing'
            )

        self.add_argument('--foo', help='foo help')


class CLIWrapper():

    def __init__(self):
        self.parser_attribute = ParserSubclass()
        self.parser_attribute.add_argument('--attribute', help='attr help')

    def get_parser_instancemethod(self):
        parser = ParserSubclass()
        parser.add_argument('--instance', help='instance help')
        return parser

    @classmethod
    def get_parser_classmethod(cls):
        parser = ParserSubclass()
        parser.add_argument('--class', help='class help')
        return parser

    @staticmethod
    def get_parser_staticmethod():
        parser = ParserSubclass()
        parser.add_argument('--static', help='static help')
        return parser

    @property
    def parser_property(self):
        parser = ParserSubclass()
        parser.add_argument('--property', help='property help')
        return parser
