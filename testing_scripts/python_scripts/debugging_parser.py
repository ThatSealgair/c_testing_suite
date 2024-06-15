import enum from Enum

TEST = "[TEST]"
DEBUG = "[DEBUG]"
POINTER = "[POINTER]"

class Level(Enum):
    FINAL = 0
    TEST = 1
    DEBUG = 2
    POINTER = 21

    @classmethod
    def _check_value(line: str) -> Level:
        if line == TEST:
            # Returns if the line is a testing notificatio.n
            print("Test")
            return Level.TEST
        elif line == DEBUG:
            # Returns if the line is a debug notification.
            print("Debug")
            Level.DEBUG

        # Returns if the line is an expected output.
        return Level.FINAL

    def _check_pointer(line: str) -> int:
        
        pointer_line: int = line.find(POINTER)

        if -1 < pointer_line:
            # Returns the position of the pointer value
            return pointer_line + 1

        # Returns None if there is no pointer call.    
        return None


if __name__ == "__main__":
    print("Test")
