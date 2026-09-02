from pathlib import Path


class MissingFileError(Exception):
    pass


class InvalidFormatError(Exception):
    pass


class InvalidDataError(Exception):
    pass


class FileManager:
    allowed_extensions = {".txt", ".csv"}

    def read_numbers(self, file_name):
        path = Path(file_name)
        if not path.exists():
            raise MissingFileError("File does not exist.")
        if path.suffix not in self.allowed_extensions:
            raise InvalidFormatError("Only TXT and CSV files are supported.")
        try:
            return [float(line.strip()) for line in path.read_text(encoding="utf-8").splitlines()]
        except PermissionError as error:
            raise PermissionError("Permission denied while reading the file.") from error
        except ValueError as error:
            raise InvalidDataError("File contains invalid numeric data.") from error


try:
    manager = FileManager()
    print(manager.read_numbers("numbers.txt"))
except (MissingFileError, InvalidFormatError, PermissionError, InvalidDataError) as error:
    print(f"File management error: {error}")
