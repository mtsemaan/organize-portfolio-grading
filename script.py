from os import scandir, getcwd, mkdir
from shutil import copy

def mkdiro(path):
    """
    Same as `os.mkdir` but automatically skips without raising an error if the directory exists.
    """
    try:
        mkdir(path)
    except FileExistsError:
        pass

def create_grading_folder(assignment_names = None, split_sections = False):
    """
    Copies files from student Portfolios into a 'To Grade' folder suitable for easily grading an assignment at a time.

    Parameters
    ----------
    assignment_names : str or iterable of str, optional
        If you wish to forcefully collect/copy only a particular assignment or set of assignments, you may enter them here. By default (`None`), this will automatically infer assignment names from student files and make a separate folder for each assignment.

    split_sections : bool, optional
        Set to `True` if you want to make separate folders for each SCI 1500 section. Default is `False`.
    """
    # Get the full path to the current working directory.
    cwd = getcwd()

    # Create a 'To Grade' folder in this directory.
    grading_dir = cwd + "/To Grade"
    mkdiro(grading_dir)

    # Scan the root directory for subdirectories that start with "SCI"
    with scandir(cwd) as root:
        for item in root:
            if item.is_dir() and item.name[:3] == "SCI":
    #         
                ## Now scan through files in those subdirectories (student folders)
                with scandir(item.path) as student_folder:
                    for file in student_folder:
                        if file.is_file():
                ##
                            if assignment_names == None and split_sections == False:
                            # Extract assignment name from file name.
                                assignment_name = file.name.split("_")[-1].split(".")[0]
                                assignment_dir = grading_dir + "/" + assignment_name

                                # Make a folder for grading that assignment.
                                mkdiro(assignment_dir)
                            else:
                                print("Not implemented yet.")

                            # Copy assignment over.
                            copy(file.path, assignment_dir)

create_grading_folder()