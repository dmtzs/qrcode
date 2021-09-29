try:
    from biblios import metodos
except ImportError as eImp:
    print(f"The following ERROR ocurred: {eImp}")

if __name__== "__main__":
    mainTitleApp= "QR codes"# Label title inside the frame of the application
    titleApp= "QR Code generator"# Title inside the application bar

    try:
        met= metodos.funciones(titleApp, mainTitleApp)
        met.GUI()
    except Exception as ex:
        print(f"The following ERROR ocurred: {ex}")
    except KeyboardInterrupt:
        print("Was pressed Ctrl + C")
    finally:
        print("Ending program")

