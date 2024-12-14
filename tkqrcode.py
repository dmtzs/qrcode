try:
    from biblios import metodos
except ImportError as err_imp:
    print(f"The following ERROR ocurred: {err_imp}")

if __name__ == "__main__":
    MAIN_TITLE_APP = "QR codes"  # Label title inside the frame of the application
    TITLE_APP = "QR Code generator"  # Title inside the application bar

    try:
        met = metodos.Funciones(TITLE_APP, MAIN_TITLE_APP)
        met.gui()
    except Exception as exc:
        print(f"The following ERROR ocurred: {exc}")
    except KeyboardInterrupt:
        print("Was pressed Ctrl + C")
    finally:
        print("Ending program")