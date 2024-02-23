# Import necessary modules
import sys

from textual import events
from textual.app import App

from components.file_tree import FileTree
from components.text_buffer import BufManagerWrapper
from userConfig.main import BUILTINS
from utils.globals.keys import KEYS


# Define Main class that inherits from App
class Main(App):
    def __init__(self, bufs: list[str], *args, **kwargs):
        self._bufs = bufs  # Store buffers temporarily
        BUILTINS._app = self
        super().__init__(*args, **kwargs)

    def compose(self):
        # Generate FileTree component
        yield FileTree(classes="-hidden")
        # Generate BufManagerWrapper component with stored buffers
        yield BufManagerWrapper(self._bufs)
        del self._bufs  # Cleanup some temporary variables

    def on_key(self, event: events.Key) -> None:
        # Add pressed key to global keys
        KEYS.add(event.key or "")
        KEYS.try_exec()


# Main function to run the application
def main():
    # Check if filename/filepath is provided as argument
    if len(sys.argv) < 2:
        sys.exit("Provide at least one filename/filepath")
    # Get filenames/filepath from command line arguments
    bufs = [str(s) for s in sys.argv[1:]]
    # Initialize Main class with filenames/filepath and run the application
    Main(bufs).run()


if __name__ == "__main__":
    main()
