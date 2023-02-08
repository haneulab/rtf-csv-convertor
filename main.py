
from src.utils.utils import debug
from src.rtf.rtf import get_rtf_dirs_paths, get_rtf_files_paths, striprtf

PATH_TO_DATA = "data"

def main(_: str) -> None:
    paths_of_dirs = get_rtf_dirs_paths(PATH_TO_DATA)
    files = {}

    read_file_paths = []
    not_read_file_paths = []

    for path_to_specific_data_dir in paths_of_dirs:
        files[path_to_specific_data_dir] = get_rtf_files_paths(PATH_TO_DATA, path_to_specific_data_dir, read_file_paths, not_read_file_paths, striprtf)


debug(__name__, main)
