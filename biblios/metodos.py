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

    def resource_path(self, relativePath):
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)
    
    def GUI(self):
        def abrirRuta():
            self.folderName= filedialog.askdirectory()

            if len(self.folderName) > 1:
                rutaError.config(text= self.folderName, fg= "green", font= ("jost", 8))
            else:
                rutaError.config(text= "Please choose a path", fg= "red", font= ("jost", 8))

        def cambiarLabelTrue(*args):
            url= ytEntry.get()
            
            if url!= "" and "https://www.youtube.com/" in url:
                texto= "URL ingresada correctamente"
                color= "green"
                #banderas[0]= 1
            
            elif (("https://www.youtube.com/" not in url) and url!= ""):
                texto= "Ingresa una URL válida"
                color= "red"
                #banderas[0]= 0

            elif url== "":
                texto= "Ingresa la URL del video"
                color= "red"
                #banderas[0]= 0

            #desbloqBoton()
            
            return ytError.config(text= texto, fg= color, font= ("jost", 15))

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
        titleLabel= tk.Label(self.mainWin, fg= "black", text= self.mainTitleApp, font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        fileLabel= tk.Label(self.mainWin, fg= "black", text= "Choose path to save output file:", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 78, anchor= CENTER)

        saveEntry= tk.Button(self.mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Path", command= abrirRuta)
        saveEntry.place(x= 10, y= 100)

        rutaError= tk.Label(self.mainWin, fg= "red", text= "Select a path", font= ("jost", 8))
        rutaError.place(x= 90, y= 102)

        # Label youtube link
        ytdlabel= tk.Label(self.mainWin, fg= "black", text= "Enter the text or URL for the qrcode you want:", font= ("jost", 15))
        ytdlabel.place(relx= 0.5, y= 170, anchor= CENTER)

        # Entry box
        ytEntryText= tk.StringVar()
        ytEntry= tk.Entry(self.mainWin, width= 79, textvariable= ytEntryText)
        ytEntry.place(x= 10, y= 190)
        ytEntry.focus()
        ytEntryText.trace_add("write", cambiarLabelTrue)

        # Error message
        ytError= tk.Label(self.mainWin, text= "", fg= "red", font= ("jost", 11))
        ytError.place(x= 120, y= 210)
        
        self.mainWin.mainloop()