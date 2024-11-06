from pathlib import Path
class fileHandler:
    def find_file(filename, search_path=''):
        search_dir = Path(search_path)
        for file_path in search_dir.rglob(filename):
            return file_path
        return None