import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Hp\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Hp\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("main_project.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facial Recognition & Digital Attendance Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'header, buttons icons and Background Images','Capture_faces','datab','att']}},
    version = "1.0",
    description = "Face Recognition & Digital Attendance System | Developed By Aryav Varshney",
    executables = executables
    )