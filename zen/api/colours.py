# Import necessary modules
from rich.style import Style
from textual.widgets.text_area import TextAreaTheme


class Colours:
    # Initialize color values
    def __init__(self) -> None:
        self.bg: str = "#141b1e"
        self.light_bg: str = "#232a2d"
        self.red: str = "#e57474"
        self.green: str = "#8ccf7e"
        self.yellow: str = "#e5c76b"
        self.blue: str = "#67b0e8"
        self.magenta: str = "#c47fd5"
        self.cyan: str = "#6cbfbf"
        self.light_gray: str = "#b3b9b8"
        self.white: str = "#dadada"
        self.win_border: str = self.magenta
        self.fg: str = self.white
        self.menu_bg: str = self.bg
        self.file_name: str = self.fg
        self.file_ext: str = self.light_gray
        self.dir_name: str = self.blue

    # Create a theme for TextArea
    # Automatically called on buf open
    def _mk_theme(self):
        return TextAreaTheme(
            name="theme",
            base_style=Style(color=self.fg, bgcolor=self.bg),
            gutter_style=Style(color=self.light_gray),
            cursor_style=Style(color=self.bg, bgcolor=self.fg),
            cursor_line_style=Style(bgcolor=self.light_bg),
            cursor_line_gutter_style=Style(color=self.red, bgcolor=self.bg, bold=True),
            bracket_matching_style=Style(bgcolor=self.green, bold=True, underline=True),
            selection_style=Style(bgcolor=self.light_gray),
            syntax_styles={
                "string": Style(color=self.green),
                "string.documentation": Style(color=self.green),
                "comment": Style(color=self.light_gray),
                "keyword": Style(color=self.red),
                "operator": Style(color=self.cyan),
                "repeat": Style(color=self.blue),
                "exception": Style(color=self.red),
                "include": Style(color=self.blue),
                "keyword.function": Style(color=self.red),
                "keyword.return": Style(color=self.red),
                "keyword.operator": Style(color=self.cyan),
                "conditional": Style(color=self.blue),
                "number": Style(color=self.magenta),
                "float": Style(color=self.magenta),
                "class": Style(color=self.yellow),
                "type.class": Style(color=self.yellow),
                "function": Style(color=self.blue),
                "function.call": Style(color=self.blue),
                "method": Style(color=self.blue),
                "method.call": Style(color=self.blue),
                "boolean": Style(color=self.magenta),
                "json.null": Style(color=self.magenta),
                "regex.punctuation.bracket": Style(color=self.blue),
                "regex.operator": Style(color=self.cyan),
                "html.end_tag_error": Style(color=self.red, underline=True),
                "tag": Style(color=self.blue),
                "yaml.field": Style(color=self.blue, bold=True),
                "json.label": Style(color=self.blue, bold=True),
                "toml.type": Style(color=self.blue),
                "toml.datetime": Style(color=self.magenta),
                "heading": Style(color=self.blue, bold=True),
                "bold": Style(bold=True),
                "italic": Style(italic=True),
                "strikethrough": Style(strike=True),
                "link": Style(color=self.magenta, underline=True),
                "inline_code": Style(color=self.yellow),
            },
        )


# Instantiate Colours class globally
COLOURS: Colours = Colours()
