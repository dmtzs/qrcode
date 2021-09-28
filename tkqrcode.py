try:
    from biblios import metodos
except ImportError as eImp:
    print(f"The following ERROR ocurred: {eImp}")

if __name__== "__main__":
    mainTitleApp= "QR codes"
    titleApp= "QR Code generator"

    try:
        met= metodos.funciones(titleApp, mainTitleApp)
        met.GUI()
    except Exception as ex:
        print(f"The following ERROR ocurred: {ex}")
    except KeyboardInterrupt:
        print("Was pressed Ctrl + C")
    finally:
        print("Ending program")

