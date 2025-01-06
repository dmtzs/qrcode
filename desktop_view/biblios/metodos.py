try:
    import os
    import sys
    import platform
    import qrcode
    import webbrowser
    import customtkinter as ctk
    from PIL import Image
    from tkinter import filedialog, messagebox, CENTER
except ImportError as eImp:
    print(f"The following ERROR ocurred: {eImp}")
    exit(1)  # Exit the program if the import fails

class Funciones():
    folderName= ""
    fileIco= "qrIma.ico"
    mainWin= ctk.CTk()

    def __init__(self, titleApp, mainTitleApp):
        self.titleApp= titleApp
        self.mainTitleApp= mainTitleApp

    def resource_path(self, relativePath):
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)
    
    def gui(self):
        banderas= [0, 0, 0]  # Path selected, Entrybox with content and Name of the qrcode result.
        def repoGit():
            webbrowser.open("https://github.com/dmtzs/qrcode")

        def abrirRuta():
            self.folderName= filedialog.askdirectory()

            if len(self.folderName) > 1:
                rutaError.configure(text= self.folderName, fg_color= "green", font= ctk.CTkFont(size=12))
                banderas[0]= 1
            else:
                rutaError.configure(text= "Please choose a path", fg_color= "red", font= ctk.CTkFont(size=12))
                banderas[0]= 0

        def cambiarLabelTrue(*args):
            qrtext= ytEntryText.get()
            
            if qrtext != "":
                texto= "QRcode content inserted correctly"
                color= "green"
                banderas[1]= 1

            elif qrtext== "" or qrtext.isspace():
                texto= "Insert a text for the content of the qrcode"
                color= "red"
                banderas[1]= 0
            
            return ytError.configure(text= texto, fg_color= color)

        def validarEntry(*args):
            contentEntry= fileNameEntryVar.get()

            if contentEntry!= "":
                banderas[2]= 1
            elif contentEntry== "" or contentEntry.isspace():
                banderas[2]= 0

        def qrcodeGenerator():
            try:
                if banderas[0]== 0:
                    messagebox.showerror("ERROR", "Please select a path to generate the output qr code")
                elif banderas[1]== 0:
                    messagebox.showerror("ERROR", "Please write something in order to generate a qr code")
                elif banderas[2]== 0:
                    messagebox.showerror("ERROR", "Please write a name for the qrcode image generated")
                else:
                    content= ytEntryText.get()
                    out= fileNameEntry.get()

                    qrImg= qrcode.make(content)

                    imgFile= open(f"{self.folderName}/{out}.png", "wb")
                    
                    qrImg.save(imgFile)
                    imgFile.close()

                    messagebox.showinfo("Sucess", "QR Code image generated")
            except Exception:
                messagebox.showerror("ERROR", "There was an error in the QR Code generator method")

        # ----------------main GUI instructions.----------------
        self.mainWin.title(self.titleApp)
        self.mainWin.resizable(width= False, height= False)
        try:
            imaIco= self.resource_path(self.fileIco)
            self.mainWin.iconbitmap(imaIco)
        except Exception:
            self.mainWin.iconbitmap("assets/qrIma.ico")
        screenWidth = self.mainWin.winfo_screenwidth()  # Width of the visualization area
        screenHeight = self.mainWin.winfo_screenheight()  # Height of the visualization area
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

        # ----------------Components of the frame----------------
        titleLabel= ctk.CTkLabel(self.mainWin, text= self.mainTitleApp, font= ctk.CTkFont(size=25, weight="bold"))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        fileLabel= ctk.CTkLabel(self.mainWin, text= "Choose path to save output file:", font= ctk.CTkFont(size=15))
        fileLabel.place(relx= 0.5, y= 78, anchor= CENTER)

        saveEntry= ctk.CTkButton(self.mainWin, fg_color= "white", width= 10, bg_color= "#0A617C", text= "Path", command= abrirRuta)
        saveEntry.place(x= 10, y= 100)

        rutaError= ctk.CTkLabel(self.mainWin, fg_color= "red", text= "Select a path", font= ctk.CTkFont(size=12))
        rutaError.place(x= 90, y= 102)

        # Label youtube link
        ytdlabel= ctk.CTkLabel(self.mainWin, text= "Enter the text or URL for the qrcode you want:", font= ctk.CTkFont(size=15))
        ytdlabel.place(relx= 0.5, y= 170, anchor= CENTER)

        # Entry box
        ytEntryText= ctk.StringVar()
        ytEntry= ctk.CTkEntry(self.mainWin, width= 79, textvariable= ytEntryText)
        ytEntry.place(x= 10, y= 190)
        ytEntry.focus()
        ytEntryText.trace_add("write", cambiarLabelTrue)

        # Error message
        ytError= ctk.CTkLabel(self.mainWin, text= "Insert a text for the content of the qrcode", fg_color= "red", font= ctk.CTkFont(size=11))
        ytError.place(x= 120, y= 210)

        # Label output file name
        fileNameLabel= ctk.CTkLabel(self.mainWin, text= "Enter the name of the qrcode image:", font= ctk.CTkFont(size=15))
        fileNameLabel.place(x= 10, y= 245)

        # Entry box for the file name of the qrcode image
        fileNameEntryVar= ctk.StringVar()
        fileNameEntry= ctk.CTkEntry(self.mainWin, width= 25, textvariable= fileNameEntryVar)
        fileNameEntry.place(x= 339, y= 252)
        fileNameEntryVar.trace_add("write", validarEntry)
        fileNameEntryVar.set("output")

        # Apply button
        applyBut= ctk.CTkButton(self.mainWin, text= "Generate qrcode", fg_color= "white", bg_color= "#0A617C", width= 15, command= qrcodeGenerator)
        applyBut.place(relx= 0.5, y= 315, anchor= CENTER)

        # Thumbnail
        try:
            Ima= Image.open("./assets/qrIma.png")
        except:
            filepathpng= self.resource_path("qrIma.png")
            Ima= Image.open(filepathpng)
        Ima= Ima.resize((190, 190), Image.Resampling.LANCZOS)  # height, width
        renderIma= ctk.CTkImage(light_image=Ima, size=(190, 190))
        # Label for showing the thumbnail
        ImaLabel= ctk.CTkLabel(self.mainWin, image= renderIma)
        ImaLabel.place(relx= 0.5, y= 425, anchor= CENTER)
        Ima.close()

        # Label to github repository
        labelGit= ctk.CTkLabel(self.mainWin, text= "Repositorio del programa:", font= ctk.CTkFont(size=10))
        labelGit.place(x= 130, y= 525)

        # Button to repository
        butGit= ctk.CTkButton(self.mainWin, width= 10, bg_color= "#0A617C", fg_color= "white", text= "Repositorio", command= repoGit)
        butGit.place(x= 290, y= 523)
        
        self.mainWin.mainloop()