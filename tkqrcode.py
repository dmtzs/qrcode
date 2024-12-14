try:
    from biblios import *
except ImportError as err_imp:
    print(f"The following ERROR ocurred: {err_imp}")

if __name__== "__main__":
    main_title_app = "QR codes"  # Label title inside the frame of the application
    title_app = "QR Code generator"  # Title inside the application bar

    try:
        met= metodos.funciones(title_app, main_title_app)
        met.GUI()
    except Exception as exc:
        print(f"The following ERROR ocurred: {exc}")
    except KeyboardInterrupt:
        print("Was pressed Ctrl + C")
    finally:
        print("Ending program")