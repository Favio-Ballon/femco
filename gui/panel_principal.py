from customtkinter import *
from logica.dao import clienteDao, agenciaDao
from logica.dto.clienteDto import ClienteDto
from logica.dto.agenciaDto import AgenciaDto

agencia_elegida:str
class LoginPanel(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Femco")
        self.configure(fg_color="#001438")
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.label = CTkLabel(self, text="Login")
        self.label.pack()
        self.agencia = CTkComboBox(self, values=[record[3] for record in agenciaDao.get_all()], state="readonly")
        #centrar el combobox
        self.button = CTkButton(self, text="Login", command=self.login)

        self.label.place(relx=0.5, rely=0.45, anchor="center")
        self.agencia.place(relx=0.5, rely=0.5, anchor="center")
        self.button.place(relx=0.5, rely=0.55, anchor="center")

    def login(self):
        # You may want to add authentication logic here
        if self.agencia.get() == "":
            return
        global agencia_elegida
        agencia_elegida = self.agencia.get()
        self.master.switch_frame(PanelFacturar)  # Switch to PanelFacturar (passing the selected agency name as an argument

class PanelFacturar(CTkFrame):
    global agencia_elegida
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Facturacion")
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()
        self.configure(fg_color="#001438")

    #agregar menu
    def create_widgets(self):
        self.panel_menu()
        pass


    def show_clientes(self):
        print("Showing Clientes")  # Placeholder, add your logic here

    def show_agencias(self):
        print("Showing Agencias")  # Placeholder, add your logic here

    def panel_menu(self):
        #create panel
        self.panel = CTkFrame(self)
        self.panel.configure(fg_color="#001440")
        self.panel.pack(anchor="center", side="left", fill="y")
        #create buttons
        self.button_facturar = CTkButton(self.panel, text="Facturar", command=self.facturar)
        self.button_cotizar = CTkButton(self.panel, text="Cotizar", command=self.cotizar)
        self.button_inventario = CTkButton(self.panel, text="Inventario", command=self.inventario)

        self.button_facturar.pack(fill="both",pady=5)
        self.button_cotizar.pack(fill="both",pady=5)
        self.button_inventario.pack(fill="both", pady=5)


    def facturar(self):
        self.master.switch_frame(PanelFacturar)

    def cotizar(self):
        self.master.switch_frame(PanelCotizar)

    def inventario(self):
        self.master.switch_frame(PanelInventario)


class PanelCotizar(CTkFrame):
    pass

class PanelInventario(CTkFrame):
    pass




class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("1200x720")
        self.resizable(False, False)
        self._frame = None  # Initialize _frame attribute
        self.switch_frame(LoginPanel)

    def switch_frame(self, frame_class, ):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
