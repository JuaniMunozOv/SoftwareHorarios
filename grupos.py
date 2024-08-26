import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import pandas as pd
from PIL import Image, ImageTk
import ttkbootstrap as ttkb

class GruposApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Horarios")

        # Crear una instancia del estilo
        self.style = ttkb.Style()
        self.style.configure('Custom.TButton', font=('Helvetica', 12))

        # Cargar la imagen de fondo
        self.background_image = Image.open("fondo11.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Crear un canvas para mostrar la imagen de fondo
        self.canvas = tk.Canvas(root, width=self.background_image.width, height=self.background_image.height)
        self.canvas.pack(fill="both", expand=True)

        # Mostrar la imagen en el canvas
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.grupos = []  # Lista para almacenar los grupos
        self.asignaturas = []  # Lista para almacenar solo los nombres de asignaturas
        self.asignaturas_horas = []  # Lista para almacenar asignaturas con carga horaria
        self.horarios_por_turno = {}  # Diccionario para almacenar los horarios por turno

        # Añadir los widgets sobre el fondo de la imagen
        self.create_group_form()

    def create_group_form(self):
        # Colocar los widgets sobre el canvas
        self.nombre_grupo_label = tk.Label(self.root, text="Nombre del Grupo")
        self.nombre_grupo_entry = tk.Entry(self.root)
        self.turno_label = tk.Label(self.root, text="Turno")
        self.turno_var = tk.StringVar(value="Matutino")
        turnos = ["Matutino", "Vespertino", "Nocturno"]
        self.turno_menu = tk.OptionMenu(self.root, self.turno_var, *turnos, command=self.configurar_horarios)

        # Usar el método `create_window` del canvas para colocar los widgets
        self.canvas.create_window(100, 50, window=self.nombre_grupo_label)
        self.canvas.create_window(250, 50, window=self.nombre_grupo_entry)
        self.canvas.create_window(100, 100, window=self.turno_label)
        self.canvas.create_window(250, 100, window=self.turno_menu)

        # Asignatura
        self.asignatura_label = tk.Label(self.root, text="Asignatura")
        self.canvas.create_window(100, 150, window=self.asignatura_label)
        self.asignatura_entry = tk.Entry(self.root)
        self.canvas.create_window(250, 150, window=self.asignatura_entry)
        self.asignatura_entry.bind("<Return>", self.anadir_asignatura)  # Vincular Enter

        # Botón para añadir asignatura
        self.anadir_asignatura_btn = ttkb.Button(self.root, text="Añadir Asignatura", command=self.anadir_asignatura, style='Custom.TButton')
        self.canvas.create_window(400, 150, window=self.anadir_asignatura_btn)

        # Frame para botones de asignaturas
        self.asignaturas_frame = tk.Frame(self.root)
        self.canvas.create_window(250, 200, window=self.asignaturas_frame)

        # Botón para cargar grupo
        self.cargar_grupo_btn = ttkb.Button(self.root, text="Cargar Grupo", command=self.cargar_grupo, style='Custom.TButton')
        self.canvas.create_window(150, 250, window=self.cargar_grupo_btn)

        # Botón para finalizar carga de grupos
        self.finalizar_carga_btn = ttkb.Button(self.root, text="Finalizar Carga", command=self.finalizar_carga_grupos, style='Custom.TButton')
        self.canvas.create_window(350, 250, window=self.finalizar_carga_btn)

    def configurar_horarios(self, turno):
        # Crear ventana para configurar los horarios
        ventana_horarios = tk.Toplevel(self.root)
        ventana_horarios.title(f"Configurar Horarios para Turno {turno}")

        horas = ["1ra", "2da", "3ra", "4ta", "5ta", "6ta", "7ma", "8va"]
        intervalos = []

        for i, hora in enumerate(horas):
            tk.Label(ventana_horarios, text=hora).grid(row=i, column=0)
            entrada_inicio = tk.Entry(ventana_horarios, width=10)
            entrada_inicio.grid(row=i, column=1)
            tk.Label(ventana_horarios, text="a").grid(row=i, column=2)
            entrada_fin = tk.Entry(ventana_horarios, width=10)
            entrada_fin.grid(row=i, column=3)
            intervalos.append((entrada_inicio, entrada_fin))

        def guardar_horarios():
            self.horarios_por_turno[turno] = [f"{inicio.get()} - {fin.get()}" for inicio, fin in intervalos]
            ventana_horarios.destroy()

        tk.Button(ventana_horarios, text="Finalizar", command=guardar_horarios).grid(row=len(horas), column=1, columnspan=3)
    def anadir_asignatura(self, event=None):
        asignatura = self.asignatura_entry.get().strip()
        if asignatura:
            # Input para carga horaria
            horas = simpledialog.askinteger("Carga Horaria", f"Ingrese la carga horaria para {asignatura}:")
            if horas is not None:
                self.asignaturas.append(asignatura)  # Almacenar solo el nombre
                self.asignaturas_horas.append(f"{asignatura} - {horas} horas")  # Almacenar con carga horaria
                self.actualizar_asignaturas_frame()
                self.asignatura_entry.delete(0, tk.END)

    def actualizar_asignaturas_frame(self):
        # Limpiar frame de asignaturas
        for widget in self.asignaturas_frame.winfo_children():
            widget.destroy()

        # Crear botones para cada asignatura con una 'X'
        for asignatura in self.asignaturas_horas:
            btn_frame = tk.Frame(self.asignaturas_frame)
            btn_frame.pack(side=tk.LEFT, padx=5, pady=5)

            btn_label = tk.Label(btn_frame, text=asignatura)
            btn_label.pack(side=tk.LEFT)

            btn_delete = ttkb.Button(btn_frame, text="X", command=lambda a=asignatura: self.eliminar_asignatura(a), style='Custom.TButton')
            btn_delete.pack(side=tk.RIGHT)

    def eliminar_asignatura(self, asignatura):
        # Separar nombre y horas
        nombre, _ = asignatura.split(" - ")
        self.asignaturas.remove(nombre)
        self.asignaturas_horas.remove(asignatura)
        self.actualizar_asignaturas_frame()

    def cargar_grupo(self):
        nombre_grupo = self.nombre_grupo_entry.get().strip()
        turno = self.turno_var.get()
        if not nombre_grupo:
            messagebox.showerror("Error", "Debe ingresar un nombre para el grupo.")
            return

        if turno not in self.horarios_por_turno or not self.horarios_por_turno[turno]:
            messagebox.showerror("Error", "Debe configurar los horarios para este turno.")
            return

        grupo = {
            "nombre": nombre_grupo,
            "turno": turno,
            "asignaturas": ', '.join(self.asignaturas),  # Solo nombres de asignaturas
            "carga_horaria": {asignatura.split(" - ")[0]: int(asignatura.split(" - ")[1].split()[0]) for asignatura in self.asignaturas_horas},
            "horarios": self.horarios_por_turno[turno]
        }
        self.grupos.append(grupo)
        print(f"Grupo cargado: {grupo}")  # Agregar impresión para depuración
        self.limpiar_formulario_grupo()
        messagebox.showinfo("Grupo cargado", "El grupo ha sido cargado correctamente.")

    def limpiar_formulario_grupo(self):
        self.nombre_grupo_entry.delete(0, tk.END)
        self.asignaturas = []
        self.asignaturas_horas = []
        self.actualizar_asignaturas_frame()

    def guardar_grupos_excel(self):
        grupos_data = []
        for grupo in self.grupos:
            grupo_info = {
                "Nombre": grupo["nombre"],
                "Turno": grupo["turno"],
                "Horarios": ", ".join(grupo["horarios"])
            }
            for asignatura, horas in grupo["carga_horaria"].items():
                grupo_info[asignatura] = horas
            grupos_data.append(grupo_info)

        df = pd.DataFrame(grupos_data)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            df.to_excel(filepath, index=False)
            messagebox.showinfo("Grupos guardados", "Los grupos se han guardado en el archivo de Excel.")

    def finalizar_carga_grupos(self):
        # Ya no guardamos en Excel directamente
        messagebox.showinfo("Finalizado", "Finalizada la carga de grupos.")
        self.root.quit()  # Cerrar la ventana y pasar a la siguiente etapa

    def get_grupos(self):
        return self.grupos

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GruposApp(root)
    root.mainloop()