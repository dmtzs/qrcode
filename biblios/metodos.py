try:
    import os
    import sys
    import platform
    import qrcode
    import webbrowser
    import tkinter as tk
    from tkinter.constants import CENTER
    from tkinter import filedialog, messagebox
except ImportError as eImp:
    print(f"The following ERROR ocurred: {eImp}")

class funciones():
    folderName= ""
    fileIco= "qrIma.ico"
    mainWin= tk.Tk()

    def __init__(self, titleApp, mainTitleApp):
        self.titleApp= titleApp
        self.mainTitleApp= mainTitleApp
    
    def GUI(self):
        def resource_path(self, relativePath):
            basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            return os.path.join(basePath, relativePath)

        # ----------------Instrucciones de la GUI principal.----------------
        self.mainWin.title(self.titleApp)
        self.mainWin.resizable(width= False, height= False)
        try:
            imaIco= self.resource_path(self.fileIco)
            self.mainWin.iconbitmap(imaIco)
        except Exception:
            self.mainWin.iconbitmap("assets/qrIma.ico")
        screenWidth = self.mainWin.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = self.mainWin.winfo_screenheight()# Alto del área de visualización
        sis= platform.system()

        if sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.mainWin.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        # ----------------Componentes del frame----------------
        
        self.mainWin.mainloop()