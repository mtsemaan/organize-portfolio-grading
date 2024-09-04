# Organizing Portfolio Grading
Meant for instructors of SCI1500 (Fall 2024) at the University of Utah. No personal data of *any kind* is included in this repository; just a bash script that relies on a particular folder structure and file naming scheme.

To grade a Portfolio artifact right now we must (i) enter the student's shared Portfolio folder, (ii) open the relevant assignment, (iii) exit the student's shared folder and then (iv) start the process over for the next student. It would be much easier on our end if we had, say, a folder called "Assignment 1" with every student in a given section's artifact for that assignment in one folder. Then we couldn't have to navigate up and down directories for each student. This short bash script does exactly that.

## How to Use
1. Download the `create-grading-folder.sh` file into the directory that contains your student Portfolio folders.
2. Open a terminal in that folder (or navigate to it).
3. Run the script from the terminal: type `bash create-grading-folder.sh` and then hit the Enter key.

When it's done, you should see a new folder called `To Grade`, inside of which will be a folder for each section, inside of which will be a folder for each assignment.

You can run this as many times as you want: it will automatically (over)write the most recent material from the student folders into `To Grade`.

## Caveats and Notes
* If you're using Windows, you need to install the Windows Subsystem for Linux (and a Linux distribution that includes bash). [This is most simply done](https://learn.microsoft.com/en-us/windows/wsl/install) by opening Powershell as an Administrator, typing `wsl --install`, hitting Enter, and restarting your computer.
* This works by looping through folders in the script's home directory that start with `SCI 1500-` and end with `_Portfolio`, so don't have any other folders in there named that way besides student portfolios.
* This does rely on the students using the right naming conventions. It can get a bit wonky if they didn't.
