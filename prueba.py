import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import pandas as pd
from PIL import Image, ImageTk
import ttkbootstrap as ttkb
import ttkbootstrap as ttk
from ttkbootstrap.icons import Icon
from ttkbootstrap.constants import *
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill
from datetime import datetime, timedelta

class HorariosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Horarios y Docentes")
        self.root.resizable(False, True)  # Disable maximize button
        style = ttk.Style(theme="darkly")
        style.configure("TLabel", background="transparent", foreground="white", font=("Arial", 12, "bold"))
        # Crear un Notebook para las pestañas
        self.notebook = ttk.Notebook(root, bootstyle="info")
        self.notebook.pack(fill='both', expand=True)
        # Crear las pestañas
        self.tab_grupos = ttk.Frame(self.notebook)
        self.tab_docentes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_grupos, text="Grupos")
        self.notebook.add(self.tab_docentes, text="Docentes")
        # Inicializar las clases GruposApp y DocentesApp
        self.grupos_app = GruposApp(self.tab_grupos, self.switch_to_docentes_tab)
        self.docentes_app = DocentesApp(self.tab_docentes, [])
    def switch_to_docentes_tab(self, grupos):
        # Cambiar a la pestaña de Docentes y pasar los grupos
        self.notebook.select(self.tab_docentes)
        self.docentes_app.update_grupos(grupos)
class GruposApp:
    def __init__(self, tab, switch_to_docentes_callback):
        self.root = tab
        self.switch_to_docentes_callback = switch_to_docentes_callback
        # Cargar la imagen de fondo
        self.background_image = Image.open("fondo.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas = tk.Canvas(tab, width=self.background_image.width, height=self.background_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        # Estilos personalizados
        style = ttk.Style()
        style.configure("TLabel", background="transparent", foreground="white", font=("Arial", 12, "bold"))
        style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
        style.map("TButton", background=[('active', 'gray'), ('!disabled', 'black')],
              foreground=[('active', 'white'), ('!disabled', 'white')])
        self.grupos = [
            {
                'nombre': '7A', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 4, 'Historia': 3, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {
                'nombre': '7B', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 4, 'Historia': 3, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {   
                'nombre': '7C', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 4, 'Historia': 3, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {
                'nombre': '8A', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 3, 'Historia': 2, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Fisico-Quimica': 2, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {
                'nombre': '8B', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 3, 'Historia': 2, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Fisico-Quimica': 2, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {
                'nombre': '8C', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica', 'carga_horaria': {'Tecnologia': 5, 'Biologia': 3, 'Ed Fisica': 2, 'Arte': 3, 'Sexualidad': 2, 'Geografia': 3, 'Historia': 2, 'Lengua': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Fisico-Quimica': 2, 'Matematica': 5}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            {
                'nombre': '9A', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica', 'carga_horaria': {'Tecnologia': 4, 'Biologia': 3, 'Ed Fisica': 2, 'Literatura': 3, 'Fisica': 3, 'Formacion para la ciudadania': 2, 'Historia': 3, 'Comunicacion': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Quimica': 3, 'Matematica': 4}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},
            
            {   'nombre': '9B', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica', 'carga_horaria': {'Tecnologia': 4, 'Biologia': 3, 'Ed Fisica': 2, 'Literatura': 3, 'Fisica': 3, 'Formacion para la ciudadania': 2, 'Historia': 3, 'Comunicacion': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Quimica': 3, 'Matematica': 4}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},

            {
                'nombre': '9C', 'turno': 'Matutino', 'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica', 'carga_horaria': {'Tecnologia': 4, 'Biologia': 3, 'Ed Fisica': 2, 'Literatura': 3, 'Fisica': 3, 'Formacion para la ciudadania': 2, 'Historia': 3, 'Comunicacion': 4, 'Cs Computacion': 2, 'Ingles': 4, 'Quimica': 3, 'Matematica': 4}, 'horarios': ['7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55', '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15']},

        ]
        self.asignaturas = []
        self.asignaturas_horas = []
        self.horarios_por_turno = {}
        self.prioridad_asignaturas = set()
        self.create_group_form()
    def create_group_form(self):
        # Colocar los widgets sobre el canvas con estilos personalizados
        style = ttk.Style()
        style.configure("TLabel", background="transparent", foreground="white", font=("Arial", 12, "bold"))
        style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
        style.map("TButton", background=[('active', 'gray'), ('!disabled', 'black')],
                foreground=[('active', 'white'), ('!disabled', 'white')])
        self.nombre_grupo_label = tk.Label(self.root, text="Nombre del Grupo")
        self.nombre_grupo_entry = ttk.Entry(self.root, width=30)
        self.turno_label = tk.Label(self.root, text="Turno")
        self.turno_var = tk.StringVar(value="Seleccione un turno")
        self.clean_turno_btn = ttk.Button(self.root, text="Reiniciar", command=self.clean_turno, style="TButton")
        turnos = ["Matutino","Intermedio M-V", "Vespertino","Intermedio V-N", "Nocturno"]
        self.turno_menu = tk.OptionMenu(self.root, self.turno_var, *turnos, command=self.configurar_horarios)
        self.canvas.create_window(self.background_image.width/2 - 10, 50, window=self.nombre_grupo_label, anchor="e")
        self.canvas.create_window(self.background_image.width/2 + 60, 50, window=self.nombre_grupo_entry, anchor="w")
        self.canvas.create_window(self.background_image.width/2 + 310, 100, window=self.clean_turno_btn, anchor="e")
        self.canvas.create_window(self.background_image.width/2 - 40, 100, window=self.turno_label, anchor="e")
        self.canvas.create_window(self.background_image.width/2 + 60, 100, window=self.turno_menu, anchor="w")
        # Asignatura
        self.asignatura_label = tk.Label(self.root, text="Asignatura")
        self.asignatura_entry = ttk.Entry(self.root, width=30)
        self.asignatura_entry.bind("<Return>", self.anadir_asignatura)
        self.anadir_asignatura_btn = ttk.Button(self.root, text="Añadir Asignatura", command=self.anadir_asignatura, style="TButton")
        self.asignaturas_frame = ttk.Frame(self.root, style="TFrame")
        self.canvas.create_window(self.background_image.width/2 - 30, 150, window=self.asignatura_label, anchor="e")
        self.canvas.create_window(self.background_image.width/2 + 60, 150, window=self.asignatura_entry, anchor="w")
        self.canvas.create_window(self.background_image.width/2, 200, window=self.anadir_asignatura_btn)
        self.canvas.create_window(self.background_image.width/2, 370, window=self.asignaturas_frame, width=680, height=240)
        self.ver_datos_btn = ttk.Button(self.root, text="Ver Datos", command=self.ver_datos, style="TButton")
        self.cargar_grupo_btn = ttk.Button(self.root, text="Cargar Grupo", command=self.cargar_grupo, style="TButton")
        self.finalizar_carga_btn = ttk.Button(self.root, text="Finalizar Carga", command=self.finalizar_carga_grupos, style="TButton")
        self.canvas.create_window(self.background_image.width - 600, self.background_image.height - 50, window=self.ver_datos_btn)
        self.canvas.create_window(self.background_image.width/2 - 10, self.background_image.height - 50, window=self.cargar_grupo_btn)
        self.canvas.create_window(self.background_image.width/2 + 200, self.background_image.height - 50, window=self.finalizar_carga_btn)
    
    def configurar_horarios(self, turno):
        self.turno_var.set(turno)  # Actualizar la variable con el turno seleccionado

        if turno not in self.horarios_por_turno:
            self.horarios_por_turno[turno] = []

        ventana_horarios = tk.Toplevel(self.root)
        ventana_horarios.title(f"Configurar Horarios para Turno {turno}")
        ventana_horarios.geometry("250x300")  # Configurar tamaño de la ventana
        ventana_horarios.resizable(False, False)  # Deshabilitar redimensionamiento

        horas = ["1ra", "2da", "3ra", "4ta", "5ta", "6ta", "7ma", "8va"]
        intervalos = [(tk.Entry(ventana_horarios, width=10), tk.Entry(ventana_horarios, width=10)) for _ in horas]

        for i, (entrada_inicio, entrada_fin) in enumerate(intervalos):
            tk.Label(ventana_horarios, text=horas[i]).grid(row=i, column=0)
            entrada_inicio.grid(row=i, column=1, padx=10, pady=5)
            tk.Label(ventana_horarios, text="a").grid(row=i, column=2)
            entrada_fin.grid(row=i, column=3, padx=10, pady=5)

        # Llenar los campos con los intervalos de tiempo existentes para el turno seleccionado
        if turno in self.horarios_por_turno and self.horarios_por_turno[turno]:
            existing_intervals = self.horarios_por_turno[turno]
            for i, (entrada_inicio, entrada_fin) in enumerate(intervalos):
                if i < len(existing_intervals):
                    hora_inicio, hora_fin = existing_intervals[i].split(" - ")
                    entrada_inicio.insert(tk.END, hora_inicio)
                    entrada_fin.insert(tk.END, hora_fin)

        def guardar_horarios():
            nuevos_horarios = []
            for inicio, fin in intervalos:
                hora_inicio = inicio.get()
                hora_fin = fin.get()
                if not self.validar_formato_hora(hora_inicio) or not self.validar_formato_hora(hora_fin):
                    messagebox.showerror("Error", "Formato de hora inválido. Utilice el formato HH:MM.")
                    return
                nuevos_horarios.append(f"{hora_inicio} - {hora_fin}")
            
            self.horarios_por_turno[turno] = nuevos_horarios  # Guardar los nuevos horarios
            ventana_horarios.destroy()  # Cerrar la ventana después de guardar

        # Botón para finalizar y guardar los horarios
        tk.Button(ventana_horarios, text="Finalizar", command=guardar_horarios).grid(row=len(horas), column=1, columnspan=3, padx=10, pady=5)

    def clean_turno(self):
        turno = self.turno_var.get()
        if turno != "Seleccione Turno" and turno in self.horarios_por_turno:
            self.horarios_por_turno[turno] = []  # Reiniciar la lista de horarios para el turno seleccionado
            messagebox.showinfo("Reiniciar Turno", f"Los horarios para el turno '{turno}' han sido reiniciados.")
        else:
            messagebox.showwarning("Reiniciar Turno", "No se ha seleccionado un turno válido para reiniciar.")

    def validar_formato_hora(self, hora):
        try:
            horas, minutos = hora.split(":")
            horas = int(horas)
            minutos = int(minutos)
            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                return False
            return True
        except ValueError:
            return False

    def anadir_asignatura(self, event=None):
        asignatura = self.asignatura_entry.get().strip()
        if asignatura:
            horas = simpledialog.askinteger("Carga Horaria", f"Ingrese la carga horaria para {asignatura}:")
            if horas is not None:
                self.asignaturas.append(asignatura)
                self.asignaturas_horas.append(f"{asignatura} - {horas} hs")
                self.actualizar_asignaturas_frame()
                self.asignatura_entry.delete(0, tk.END)
    def actualizar_asignaturas_frame(self):
        # Limpiar el frame existente
        for widget in self.asignaturas_frame.winfo_children():
            widget.destroy()
        # Definir el número máximo de columnas
        max_columnas = 3
        # Recorrer las asignaturas para crear los widgets correspondientes
        for i, asignatura in enumerate(self.asignaturas_horas):
            nombre_asignatura, _ = asignatura.split(" - ")
            # Crear un frame para cada grupo de botones
            btn_frame = tk.Frame(self.asignaturas_frame)
            btn_frame.grid(row=i // max_columnas, column=i % max_columnas, padx=5, pady=5)
            # Botón de la asignatura
            btn_label = ttk.Button(btn_frame, text=asignatura, width=10, bootstyle="info-outline")
            btn_label.pack(side=tk.LEFT)
            # Botón de prioridad (estrella)
            star_text = "⭐" if nombre_asignatura in self.prioridad_asignaturas else "☆"
            star_button = ttk.Button(btn_frame, text=star_text, width=2, bootstyle="warning-outline", 
                                    command=lambda a=nombre_asignatura: self.toggle_prioridad_asignatura(a))
            star_button.pack(side=tk.LEFT, padx=5)
            if nombre_asignatura in self.prioridad_asignaturas:
                star_button.configure(bootstyle="warning")
            else:
                star_button.configure(bootstyle="warning-outline")
            # Botón para eliminar la asignatura
            btn_delete = ttk.Button(btn_frame, text="X", width=2, bootstyle="danger-outline", 
                                    command=lambda a=asignatura: self.eliminar_asignatura(a))
            btn_delete.pack(side=tk.LEFT, padx=5)
    def eliminar_asignatura(self, asignatura):
        nombre, _ = asignatura.split(" - ")
        self.asignaturas.remove(nombre)
        self.asignaturas_horas.remove(asignatura)
        self.actualizar_asignaturas_frame()
    def toggle_prioridad_asignatura(self, asignatura):
        if asignatura in self.prioridad_asignaturas:
            self.prioridad_asignaturas.remove(asignatura)  # Eliminar la prioridad si ya está seleccionada
            messagebox.showinfo("Prioridad Removida", f"La asignatura {asignatura} ya no tiene prioridad.")
        else:
            self.prioridad_asignaturas.add(asignatura)  # Añadir la asignatura como prioritaria
            messagebox.showinfo("Prioridad Asignada", f"La asignatura {asignatura} ahora tiene prioridad.")
        self.actualizar_asignaturas_frame()  # Refrescar la visualización para reflejar cambios en la prioridad
    def cargar_grupo(self):
        nombre_grupo = self.nombre_grupo_entry.get().strip()
        turno = self.turno_var.get()
        if not nombre_grupo:
            messagebox.showerror("Error", "Debe ingresar un nombre para el grupo.")
            return
        if turno not in self.horarios_por_turno or not self.horarios_por_turno[turno]:
            messagebox.showerror("Error", "Debe configurar los horarios para este turno.")
            return
        if not self.asignaturas:
            messagebox.showerror("Error", "Debe añadir al menos una asignatura.")
            return
        grupo = {
            "nombre": nombre_grupo,
            "turno": turno,
            "asignaturas": ', '.join(self.asignaturas),
            "carga_horaria": {asignatura.split(" - ")[0]: int(asignatura.split(" - ")[1].split()[0]) for asignatura in self.asignaturas_horas},
            "horarios": self.horarios_por_turno[turno]
        }
        # Confirmar antes de cargar
        if messagebox.askyesno("Confirmar Carga", f"¿Está seguro de cargar el grupo {nombre_grupo}?\n\n"
                                f"Nombre del Grupo: {nombre_grupo}\n"
                                f"Turno: {turno}\n"
                                f"Horarios: {', '.join(self.horarios_por_turno[turno])}\n"
                                f"Asignaturas con Carga Horaria:\n"
                                f"{', '.join(self.asignaturas_horas)}"):
            self.grupos.append(grupo)
            print(f"Grupo cargado: {grupo}")
            self.limpiar_formulario_grupo()
            messagebox.showinfo("Grupo cargado", "El grupo ha sido cargado correctamente.")
    def ver_datos(self):
        # Crear una nueva ventana para ver los datos
        ventana_datos = tk.Toplevel(self.root)
        ventana_datos.title("Datos del Grupo")

        # Crear un Frame para contener el Canvas y la Scrollbar
        frame_datos = tk.Frame(ventana_datos)
        frame_datos.pack(fill="both", expand=True)

        # Crear un Canvas dentro del Frame
        canvas_datos = tk.Canvas(frame_datos)
        canvas_datos.pack(side="left", fill="both", expand=True)

        # Agregar una Scrollbar vertical y configurarla para el Canvas
        scrollbar_datos = ttk.Scrollbar(frame_datos, orient="vertical", command=canvas_datos.yview)
        scrollbar_datos.pack(side="right", fill="y")
        canvas_datos.configure(yscrollcommand=scrollbar_datos.set)

        # Crear un Frame dentro del Canvas para colocar el contenido
        frame_interior = tk.Frame(canvas_datos)

        # Crear el contenido de los datos
        for grupo in self.grupos:
            datos_grupo = (
                f"Nombre del Grupo: {grupo['nombre']}\n"
                f"Turno: {grupo['turno']}\n"
                f"Asignaturas: {grupo['asignaturas']}\n"
                f"Carga Horaria:\n"
            )
            for asignatura, carga_horaria in grupo['carga_horaria'].items():
                datos_grupo += f"{asignatura}: {carga_horaria} hs\n"
            datos_grupo += f"Horarios: {', '.join(grupo['horarios'])}\n"
            datos_grupo += "-----------------------------------\n"
            label_datos = tk.Label(frame_interior, text=datos_grupo, justify="left", anchor="w", bg="black", fg="white", font=("Arial", 8, "bold"))
            label_datos.pack(anchor="w", padx=10, pady=5)

        # Colocar el Frame interior dentro del Canvas
        canvas_datos.create_window((0, 0), window=frame_interior, anchor="nw")

        # Configurar el tamaño del Canvas según el contenido
        frame_interior.update_idletasks()
        canvas_datos.config(scrollregion=canvas_datos.bbox("all"))

        # Configurar la redimensión del Canvas
        frame_interior.bind(
            "<Configure>",
            lambda event: canvas_datos.configure(scrollregion=canvas_datos.bbox("all"))
        )

        # Agregar la capacidad de desplazarse con la rueda del ratón
        canvas_datos.bind_all("<MouseWheel>", lambda event: canvas_datos.yview_scroll(int(-1*(event.delta/120)), "units"))

    def limpiar_formulario_grupo(self):
        self.nombre_grupo_entry.delete(0, tk.END)
        self.asignaturas = []
        self.configurar_horarios("Seleccione un turno")
        self.asignaturas_horas = []
        self.actualizar_asignaturas_frame()
    def finalizar_carga_grupos(self):
        if not self.grupos:
            messagebox.showerror("Error", "Debe cargar al menos un grupo.")
            return

        # Cambiar a la pestaña de Docentes
        self.switch_to_docentes_callback(self.grupos)
    def get_grupos(self):
        return self.grupos

class DocentesApp:
    def __init__(self, tab, grupos):
        self.root = tab
        self.grupos = grupos
        ### ACA ESTA EL CAMBIO: Agregué los docentes que llegué a hardcodear, funciona. 
        self.docentes = [

                        {'nombre': 'Lucia Martinez', #
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=1),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Lucia Videla ',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Laura López Tuero ',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Juan Bustos ',
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            }
                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Rogelio Giró ', #
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Patricia Alejandra Lopez Marquez',
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },

                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Stephanie Grego',#
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            }, 
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },

                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Gustavo Moraes ',
                        
                        'grupos': [
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=1),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=1),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Dario da Silveira',
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },

                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Ana Trindade',
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=1),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=1),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=1),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Leticia Medeiros', # No tiene asignatura asignada, en el pdf dice '243' pero no se a que se refiere
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Ximena Perez ',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Fernando Hernández',
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Astrid Rodriguez',
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },


                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },

                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=1),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Gina Nuñez',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Hermes Saldaña',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=1)
                            },
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=1),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                        }
                        },
                        {'nombre': 'Nestor Lucas', #
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Fernando Alvarez',
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=1),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Diego Rios',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=1),
                            },
                        }
                        },    
                        {'nombre': 'Mariana Alonzo',
                        'grupos': [
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=1),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Carolina Alonzo ',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },

                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '9C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35':tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=1),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=1),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=1),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=1),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            }
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=1),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=1),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9C': {
                                'Tecnologia': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=1),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            }
                        }
                        },
                        {'nombre': 'Ana Ferreira Campanella', #
                        'grupos': [
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=1),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=1),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=1),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=1),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=1),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '7B': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Hector Batalles',
                        'grupos': [
                            {
                                'nombre': '9A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '9B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Literatura, Fisica, Formacion para la ciudadania, Historia, Comunicacion, Cs Computacion, Ingles, Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 4, 
                                    'Biologia': 3, 
                                    'Ed Fisica': 2, 
                                    'Literatura': 3, 
                                    'Fisica': 3, 
                                    'Formacion para la ciudadania': 2, 
                                    'Historia': 3, 
                                    'Comunicacion': 4, 
                                    'Cs Computacion': 2, 
                                    'Ingles': 4, 
                                    'Quimica': 3, 
                                    'Matematica': 4
                                    },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '9A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                            '9B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=1),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35':tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=1),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=0),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=0),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=0),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=0),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=0),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=0),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=0),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=0),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=0),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=1),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15':tk.IntVar(value=0)
                            },
                        },
                        'asignaturas': {
                            '9A': {
                                'Tecnologia': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },
                            '9B': {
                                'Tecnologia': tk.IntVar(value=1),
                                'Biologia': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Literatura': tk.IntVar(value=0),
                                'Fisica': tk.IntVar(value=0),
                                'Formacion para la ciudadania': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=0),
                                'Comunicacion': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),  
                                'Ingles': tk.IntVar(value=0),
                                'Quimica': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                            },

                        }
                        },
                        {'nombre': 'Nestor Barea',
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=0),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=0),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=0),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=1),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=0),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=0),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=1),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=0),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=1),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=0),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=1),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=0),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=1),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=0),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=1),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=1),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=1),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=1),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=1)
                            },
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=1),
                                'Historia': tk.IntVar(value=0),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                        }
                        },
                        {'nombre': 'Alejandra Galli', 
                        'grupos': [
                            {
                                'nombre': '7A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '7C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 4,
                                    'Historia': 3,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8A',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8B',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                            {
                                'nombre': '8C',
                                'turno': 'Matutino',
                                'asignaturas': 'Tecnologia, Biologia, Ed Fisica, Arte, Sexualidad, Geografia, Historia, Lengua, Cs Computacion, Ingles, Fisico-Quimica, Matematica',
                                'carga_horaria': {
                                    'Tecnologia': 5,
                                    'Biologia': 3,
                                    'Ed Fisica': 2,
                                    'Arte': 3,
                                    'Sexualidad': 2,
                                    'Geografia': 3,
                                    'Historia': 2,
                                    'Lengua': 4,
                                    'Cs Computacion': 2,
                                    'Ingles': 4,
                                    'Fisico-Quimica': 2,
                                    'Matematica': 5
                                },
                                'horarios': [
                                    '7:15 - 7:55', '7:55 - 8:35', '8:45 - 9:35', '9:35 - 10:15', '10:15 - 10:55',
                                    '11:05 - 11:50', '11:55 - 12:35', '12:35 - 13:15'
                                ]
                            },
                        ],
                        'disponibilidad': {
                            '7A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Lunes 7:15 - 7:55': tk.IntVar(value=0),
                                'Martes 7:15 - 7:55': tk.IntVar(value=0),
                                'Miércoles 7:15 - 7:55': tk.IntVar(value=1),
                                'Jueves 7:15 - 7:55': tk.IntVar(value=1),
                                'Viernes 7:15 - 7:55': tk.IntVar(value=1),
                                'Lunes 7:55 - 8:35': tk.IntVar(value=0),
                                'Martes 7:55 - 8:35': tk.IntVar(value=0),
                                'Miércoles 7:55 - 8:35': tk.IntVar(value=1),
                                'Jueves 7:55 - 8:35': tk.IntVar(value=1),
                                'Viernes 7:55 - 8:35': tk.IntVar(value=1),
                                'Lunes 8:45 - 9:35': tk.IntVar(value=0),
                                'Martes 8:45 - 9:35': tk.IntVar(value=0),
                                'Miércoles 8:45 - 9:35': tk.IntVar(value=1),
                                'Jueves 8:45 - 9:35': tk.IntVar(value=1),
                                'Viernes 8:45 - 9:35': tk.IntVar(value=1),
                                'Lunes 9:35 - 10:15': tk.IntVar(value=0),
                                'Martes 9:35 - 10:15': tk.IntVar(value=0),
                                'Miércoles 9:35 - 10:15': tk.IntVar(value=1),
                                'Jueves 9:35 - 10:15': tk.IntVar(value=1),
                                'Viernes 9:35 - 10:15': tk.IntVar(value=1),
                                'Lunes 10:15 - 10:55': tk.IntVar(value=0),
                                'Martes 10:15 - 10:55': tk.IntVar(value=0),
                                'Miércoles 10:15 - 10:55': tk.IntVar(value=1),
                                'Jueves 10:15 - 10:55': tk.IntVar(value=1),
                                'Viernes 10:15 - 10:55': tk.IntVar(value=1),
                                'Lunes 11:05 - 11:50': tk.IntVar(value=0),
                                'Martes 11:05 - 11:50': tk.IntVar(value=0),
                                'Miércoles 11:05 - 11:50': tk.IntVar(value=1),
                                'Jueves 11:05 - 11:50': tk.IntVar(value=1),
                                'Viernes 11:05 - 11:50': tk.IntVar(value=1),
                                'Lunes 11:55 - 12:35': tk.IntVar(value=0),
                                'Martes 11:55 - 12:35': tk.IntVar(value=0),
                                'Miércoles 11:55 - 12:35': tk.IntVar(value=0),
                                'Jueves 11:55 - 12:35': tk.IntVar(value=0),
                                'Viernes 11:55 - 12:35': tk.IntVar(value=0),
                                'Lunes 12:35 - 13:15': tk.IntVar(value=0),
                                'Martes 12:35 - 13:15': tk.IntVar(value=0),
                                'Miércoles 12:35 - 13:15': tk.IntVar(value=0),
                                'Jueves 12:35 - 13:15': tk.IntVar(value=0),
                                'Viernes 12:35 - 13:15': tk.IntVar(value=0)
                            }
                        },
                        'asignaturas': {
                            '7A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '7C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0)
                            },
                            '8A': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8B': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                            '8C': {
                                'Arte': tk.IntVar(value=0),
                                'Biologia': tk.IntVar(value=0),
                                'Cs Computacion': tk.IntVar(value=0),
                                'Ed Fisica': tk.IntVar(value=0),
                                'Geografia': tk.IntVar(value=0),
                                'Historia': tk.IntVar(value=1),
                                'Ingles': tk.IntVar(value=0),
                                'Lengua': tk.IntVar(value=0),
                                'Matematica': tk.IntVar(value=0),
                                'Sexualidad': tk.IntVar(value=0),
                                'Tecnologia': tk.IntVar(value=0),
                                'Fisico-Quimica': tk.IntVar(value=0)
                            },
                        }
                        },
                    ]

        self.disponibilidad_actual = {}
        
        self.asignaturas_seleccionadas = {}
        self.grupos_seleccionados = []  # Lista para almacenar los grupos seleccionados
        # Configuración del fondo
        self.background_image = Image.open("fondo.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas = tk.Canvas(tab, width=self.background_image.width, height=self.background_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Crear el formulario de docente
        self.create_docente_form()

    def convertir_a_minutos(self, intervalo):
        inicio, fin = intervalo.split(' - ')
        formato = '%H:%M'
        inicio_dt = datetime.strptime(inicio, formato)
        fin_dt = datetime.strptime(fin, formato)
        return (inicio_dt.hour * 60 + inicio_dt.minute, fin_dt.hour * 60 + fin_dt.minute)
    def update_grupos(self, grupos):
        self.grupos = grupos

    def create_docente_form(self):
        # Nombre del docente
        self.nombre_docente_label = tk.Label(self.root, text="Nombre del Docente")
        self.canvas.create_window(300, 50, window=self.nombre_docente_label)
        self.nombre_docente_entry = tk.Entry(self.root)
        self.canvas.create_window(500, 50, window=self.nombre_docente_entry)
        self.nombre_docente_entry.bind("<Return>", self.mostrar_seleccion_grupos)  # Bind para mostrar los grupos al presionar Enter

        # Botón para seleccionar grupos
        self.grupo_label = tk.Label(self.root, text="Grupos")
        self.canvas.create_window(300, 100, window=self.grupo_label)
        self.seleccionar_grupos_btn = ttk.Button(self.root, text="Seleccionar Grupos", command=self.mostrar_seleccion_grupos)
        self.canvas.create_window(500, 100, window=self.seleccionar_grupos_btn)

        # Botón para guardar el docente
        self.guardar_docente_btn = ttk.Button(self.root, text="Guardar Docente", command=self.guardar_docente, style="TButton")
        self.canvas.create_window(self.background_image.width/2 - 200, self.background_image.height - 80, window=self.guardar_docente_btn)

        # Botón para generar horarios
        self.generar_horarios_btn = ttk.Button(self.root, text="Generar Horarios", command=self.generar_horarios, style="TButton")
        self.canvas.create_window(self.background_image.width - 240, self.background_image.height - 80, window=self.generar_horarios_btn)

        # Frame para docentes cargados
        self.docentes_frame = ttk.Frame(self.root)
        self.canvas.create_window(self.background_image.width/2, 370, window=self.docentes_frame, width=680, height=200)

        tk.Label(self.docentes_frame, text="Docentes Cargados:").pack(side=tk.TOP, fill=tk.X)
        self.docentes_listbox = tk.Listbox(self.docentes_frame)
        self.docentes_listbox.pack(side=tk.TOP, fill=tk.X)

        # Botón para ver datos
        self.ver_datos_btn = ttk.Button(self.root, text="Ver Datos", command=self.ver_datos, style="TButton")
        self.canvas.create_window(self.background_image.width - 400, self.background_image.height - 80, window=self.ver_datos_btn)

    def mostrar_seleccion_grupos(self, event=None):
        self.ventana_grupos = tk.Toplevel(self.root)
        self.ventana_grupos.title("Seleccionar Grupos")
        self.ventana_grupos.geometry("300x250")

        self.botones_grupos = {}
        frame = ttk.Frame(self.ventana_grupos)
        frame.pack(pady=10)

        for i, grupo in enumerate(self.grupos):
            row = i // 3
            column = i % 3
            btn = ttk.Button(frame, text=grupo['nombre'], command=lambda g=grupo: self.toggle_grupo(g))
            btn.grid(row=row, column=column, padx=5, pady=5)
            self.botones_grupos[grupo['nombre']] = btn

        ttk.Button(self.ventana_grupos, text="Finalizar", command=self.finalizar_seleccion_grupos).pack(pady=10)

    def toggle_grupo(self, grupo):
        nombre_grupo = grupo['nombre']
        if grupo in self.grupos_seleccionados:
            self.grupos_seleccionados.remove(grupo)
            self.botones_grupos[nombre_grupo].configure(bootstyle="secondary")
        else:
            self.grupos_seleccionados.append(grupo)
            self.botones_grupos[nombre_grupo].configure(bootstyle="success")

    def finalizar_seleccion_grupos(self):
        self.ventana_grupos.destroy()
        if self.grupos_seleccionados:
            self.ingresar_disponibilidad()

    def ingresar_disponibilidad(self):
        self.ventana_disponibilidad = tk.Toplevel(self.root)
        self.ventana_disponibilidad.title("Disponibilidad Horaria")
        self.notebook = ttk.Notebook(self.ventana_disponibilidad)
        self.notebook.pack(expand=True, fill="both")

        # Inicializar self.checkbox_vars para almacenar los Checkbutton de todos los grupos
        self.checkbox_vars = {}

        for grupo in self.grupos_seleccionados:
            frame_grupo = ttk.Frame(self.notebook)
            self.notebook.add(frame_grupo, text=grupo['nombre'])
            self.mostrar_horarios(frame_grupo, grupo)

        ttk.Button(self.ventana_disponibilidad, text="Finalizar", command=self.finalizar_disponibilidad).pack(pady=10)

    def mostrar_horarios(self, frame, grupo):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horarios = grupo['horarios']
        self.disponibilidad_actual[grupo['nombre']] = {}

        # Diccionario para almacenar los Checkbuttons y sus variables de control para este grupo específico
        self.checkbox_vars[grupo['nombre']] = {}

        # Fila "Seleccionar todo" para cada día
        for j, dia in enumerate(dias):
            tk.Label(frame, text=dia).grid(row=0, column=j + 1, padx=5, pady=5)
            var = tk.IntVar()
            checkbox = tk.Checkbutton(frame, variable=var, command=lambda d=dia: self.seleccionar_todo(grupo['nombre'], d))
            checkbox.grid(row=1, column=j + 1, padx=5, pady=5)
            self.checkbox_vars[grupo['nombre']][f"{dia} Seleccionar todo"] = var

        # Create a frame for the "Seleccionar todo" checkboxes
        select_all_frame = ttk.Frame(frame, borderwidth=2, relief="solid")
        select_all_frame.grid(row=1, column=0, padx=5, pady=5)

        # Add label and checkboxes to the "Seleccionar todo" frame
        tk.Label(select_all_frame, text="Seleccionar todo").pack()

        for i, horario in enumerate(horarios):
            tk.Label(frame, text=horario).grid(row=i + 2, column=0, padx=5, pady=5)
            for j, dia in enumerate(dias):
                var = tk.IntVar()
                checkbox = tk.Checkbutton(frame, variable=var)
                checkbox.grid(row=i + 2, column=j + 1, padx=5, pady=5)
                self.disponibilidad_actual[grupo['nombre']][f"{dia} {horario}"] = var

                # Guardar cada Checkbutton en el diccionario, usando el nombre del grupo como clave principal
                self.checkbox_vars[grupo['nombre']][f"{dia} {horario}"] = var

        # Añadir un botón para copiar la disponibilidad a los demás grupos
        copiar_btn = ttk.Button(frame, text="Copiar a otros grupos", command=lambda: self.copiar_disponibilidad(grupo))
        copiar_btn.grid(row=len(horarios) + 2, column=0, columnspan=len(dias) + 1, pady=10)

    def seleccionar_todo(self, grupo_nombre, dia):
        """Función para seleccionar o deseleccionar toda la fila de un día específico."""
        for horario in self.disponibilidad_actual[grupo_nombre]:
            if horario.startswith(dia):
                estado_actual = self.checkbox_vars[grupo_nombre][horario].get()
                # Alternar el estado de todas las casillas de verificación en la fila del día seleccionado
                nuevo_estado = 0 if estado_actual == 1 else 1
                self.checkbox_vars[grupo_nombre][horario].set(nuevo_estado)

    def copiar_disponibilidad(self, grupo_seleccionado):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horarios = grupo_seleccionado['horarios']

        for grupo in self.grupos_seleccionados:
            if grupo == grupo_seleccionado:
                continue  # Saltar el grupo seleccionado

            if grupo['horarios'] == horarios:
                for dia in dias:
                    for horario in horarios:
                        if f"{dia} {horario}" in self.checkbox_vars[grupo_seleccionado['nombre']]:
                            estado = self.checkbox_vars[grupo_seleccionado['nombre']][f"{dia} {horario}"].get()
                            if f"{dia} {horario}" in self.checkbox_vars[grupo['nombre']]:
                                self.checkbox_vars[grupo['nombre']][f"{dia} {horario}"].set(estado)


    def finalizar_disponibilidad(self):
        self.ventana_disponibilidad.destroy()
        self.seleccionar_asignaturas()

    def seleccionar_asignaturas(self):
        self.ventana_asignaturas = tk.Toplevel(self.root)
        self.ventana_asignaturas.title("Seleccionar Asignaturas")

        self.notebook_asignaturas = ttk.Notebook(self.ventana_asignaturas)
        self.notebook_asignaturas.pack(expand=True, fill="both")

        for grupo in self.grupos_seleccionados:
            frame_grupo = ttk.Frame(self.notebook_asignaturas)
            self.notebook_asignaturas.add(frame_grupo, text=grupo['nombre'])

            tk.Label(frame_grupo, text=f"Asignaturas para {grupo['nombre']}").pack()

            self.asignaturas_seleccionadas[grupo['nombre']] = {}
            asignaturas = sorted(grupo['asignaturas'].split(', '))
            for asignatura in asignaturas:
                var = tk.IntVar()
                chk = tk.Checkbutton(frame_grupo, text=asignatura, variable=var)
                chk.pack(anchor='w')
                self.asignaturas_seleccionadas[grupo['nombre']][asignatura] = var

            # Añadir un botón para copiar las asignaturas a los demás grupos
            copiar_btn_asig = ttk.Button(frame_grupo, text="Copiar a otros grupos", command=lambda g=grupo: self.copiar_asignaturas(g))
            copiar_btn_asig.pack(pady=10)

        ttk.Button(self.ventana_asignaturas, text="Finalizar", command=self.finalizar_asignaturas).pack(pady=10)

    def copiar_asignaturas(self, grupo_seleccionado):
        """Copia las asignaturas seleccionadas de un grupo a los demás grupos."""
        asignaturas_copiar = self.asignaturas_seleccionadas[grupo_seleccionado['nombre']]
        
        for grupo in self.grupos_seleccionados:
            if grupo != grupo_seleccionado:
                for asignatura, var in asignaturas_copiar.items():
                    self.asignaturas_seleccionadas[grupo['nombre']][asignatura].set(var.get())

    def finalizar_asignaturas(self):
        self.ventana_asignaturas.destroy()
        self.guardar_docente()

    def guardar_docente(self):
        nombre_docente = self.nombre_docente_entry.get().strip()
        if not nombre_docente or not self.grupos_seleccionados:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        docente = {
            "nombre": nombre_docente,
            "grupos": self.grupos_seleccionados,
            "disponibilidad": self.disponibilidad_actual,
            "asignaturas": self.asignaturas_seleccionadas,
        }     
        
        # Agregar el docente a la lista de docentes
        self.docentes.append(docente)
            
        print('anasheeeeee: ', self.docentes)
        # Actualizar el frame de docentes cargados
        self.actualizar_docentes_frame()
        
        messagebox.showinfo("Docente guardado", "Los datos del docente han sido guardados correctamente.")
        self.limpiar_formulario_docente()

    def limpiar_formulario_docente(self):
        self.nombre_docente_entry.delete(0, tk.END)
        self.grupos_seleccionados = []
        self.disponibilidad_actual = {}
        self.asignaturas_seleccionadas = {}
        self.actualizar_docentes_frame()

    def actualizar_docentes_frame(self):
        # Limpiar el contenido anterior del frame
        for widget in self.docentes_frame.winfo_children():
            widget.destroy()

        # Etiqueta para indicar los docentes cargados
        tk.Label(self.docentes_frame, text="Docentes Cargados:").pack(side=tk.TOP, fill=tk.X)

        # Crear un frame para contener el canvas y las scrollbars
        container_frame = ttk.Frame(self.docentes_frame)
        container_frame.pack(fill=tk.BOTH, expand=True)

        # Crear un canvas dentro del contenedor
        canvas = tk.Canvas(container_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Añadir una scrollbar vertical al contenedor
        scrollbar_y = ttk.Scrollbar(container_frame, orient="vertical", command=canvas.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        # Añadir una scrollbar horizontal al contenedor
        scrollbar_x = ttk.Scrollbar(container_frame, orient="horizontal", command=canvas.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar el canvas para que funcione con las scrollbars
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Frame dentro del canvas donde se agregan los botones de los docentes
        buttons_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=buttons_frame, anchor="nw")

        max_columnas = 4  # Define el número máximo de columnas

        for i, docente in enumerate(self.docentes):
            row = i // max_columnas
            col = i % max_columnas

            # Crear un frame para cada grupo de botones de docente
            btn_frame = ttk.Frame(buttons_frame)
            btn_frame.grid(row=row, column=col, padx=5, pady=5, sticky="w")

            # Texto del botón del docente
            docente_text = f"{docente['nombre']} - Grupos: {', '.join([grupo['nombre'] for grupo in docente['grupos']])}"

            # Botón para mostrar la información del docente
            docente_button = ttk.Button(btn_frame, text=docente_text, 
                                        command=lambda d=docente: self.mostrar_info_docente(d),
                                        style="TButton")
            docente_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Botón para eliminar al docente
            delete_button = ttk.Button(btn_frame, text="X", width=2, 
                                    command=lambda d=docente: self.eliminar_docente(d),
                                    style="Danger.TButton")
            delete_button.pack(side=tk.LEFT, padx=(5, 0))

        # Actualizar la scrollregion del canvas después de haber agregado todos los widgets
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def eliminar_docente(self, docente):
        self.docentes.remove(docente)
        self.actualizar_docentes_frame()
    def generar_horarios(self):
            horarios = []
            superposiciones = []
            dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

            # Inicializar la estructura de la planilla
            for grupo in self.grupos:
                grupo_nombre = grupo['nombre']
                for intervalo in grupo['horarios']:
                    fila = {"Grupo": grupo_nombre, "Horario": intervalo}
                    for dia in dias:
                        fila[dia] = ""
                    horarios.append(fila)
                # Agrega una fila en blanco entre grupos
                horarios.append({"Grupo": "", "Horario": "", "Lunes": "", "Martes": "", "Miércoles": "", "Jueves": "", "Viernes": ""})

            # Asignar horarios a cada grupo y asignatura
            for grupo in self.grupos:
                grupo_nombre = grupo['nombre']
                for docente in self.docentes:
                    if grupo in docente['grupos']:
                        for asignatura, asignatura_var in docente['asignaturas'][grupo_nombre].items():
                            if asignatura_var.get() == 1:
                                total_horas_asignatura = grupo['carga_horaria'][asignatura]
                                combinaciones_horas = self.generar_combinaciones_horas(total_horas_asignatura)
                                self.asignar_horas_asignatura(horarios, grupo_nombre, docente, asignatura, combinaciones_horas, dias, superposiciones)

            self.exportar_horarios_excel(horarios, superposiciones)

            if superposiciones:
                messagebox.showwarning("Superposiciones Detectadas", "\n".join(superposiciones))
            else:
                messagebox.showinfo("Horarios Generados", "Los horarios han sido generados exitosamente.")

    def asignar_horas_asignatura(self, horarios, grupo_nombre, docente, asignatura, combinaciones_horas, dias, superposiciones):
        """Asigna las horas de una asignatura respetando las combinaciones y prioridades."""
        horas_asignadas = 0
        dias_asignados = []
        dia_actual = None
        for combinacion in combinaciones_horas:
            for dia in dias:
                horas_disponibles = self.obtener_horas_disponibles(horarios, grupo_nombre, docente, dia)
                if len(horas_disponibles) >= combinacion[0] and horas_asignadas < sum(combinacion) and dia not in dias_asignados:
                    horas_asignadas_dia,dia_actual = self.asignar_horas_en_dia(horarios, grupo_nombre, docente, asignatura, [combinacion[0]], dia, horas_disponibles, superposiciones,dias, combinaciones_horas, dias_asignados, combinacion_restante=[])
                    horas_asignadas += horas_asignadas_dia
                    if dia_actual is not None:
                        dia = dia_actual
                    dias_asignados.append(dia)
                    
                    # Asignar el resto de la combinación en otros días
                    if horas_asignadas_dia > 0 and len(combinacion) > 1:
                        combinacion_restante = combinacion[1:]
                        for dia_restante in dias:
                            if dia_restante != dia and dia_restante not in dias_asignados:  # No asignar en el mismo día
                                horas_disponibles_restantes = self.obtener_horas_disponibles(horarios, grupo_nombre, docente, dia_restante)
                                if len(horas_disponibles_restantes) >= combinacion_restante[0]:
                                    horitas,dia_actual = self.asignar_horas_en_dia(horarios, grupo_nombre, docente, asignatura, combinacion_restante, dia_restante, horas_disponibles_restantes, superposiciones,dias, combinaciones_horas, dias_asignados, combinacion_restante)
                                    horas_asignadas_dia += horitas
                                    horas_asignadas += horas_asignadas_dia
                                    dias_asignados.append(dia_restante)
                                    break  # Salir del loop si se asignaron todas las horas
                    if horas_asignadas >= sum(combinacion):
                        break  # Salir si se asignaron todas las horas
                if horas_asignadas >= sum(combinacion):
                    break   
    
    def intentar_asignar_combinacion(self, horarios, grupo_nombre, docente, asignatura, combinacion, dias, superposiciones):
        """Intenta asignar una combinación de horas en cualquier día disponible."""
        for dia in dias:
            horas_disponibles = self.obtener_horas_disponibles(horarios, grupo_nombre, docente, dia)
            if len(horas_disponibles) >= len(combinacion):
                if self.asignar_horas_en_dia(horarios, grupo_nombre, docente, asignatura, combinacion, dia, horas_disponibles, superposiciones,dias_asignados=[], combinacion_restante=[]):
                    return True
        return False

    def obtener_horas_disponibles(self, horarios, grupo_nombre, docente, dia):
        """Obtiene las horas disponibles para un docente en un grupo y día específicos."""
        return [fila['Horario'] for fila in horarios if fila['Grupo'] == grupo_nombre and 
                fila[dia] == "" and 
                docente['disponibilidad'][grupo_nombre].get(f"{dia} {fila['Horario']}", tk.IntVar()).get() == 1 and
                not self.docente_ocupado_en_otro_grupo(horarios, docente, dia, fila['Horario'])]


    def obtener_horas_disponibles_superponibles(self, horarios, grupo_nombre, docente, dia):
        """Obtiene las horas disponibles para un docente en un grupo y día específicos."""
        return [fila['Horario'] for fila in horarios if fila['Grupo'] == grupo_nombre and 
                docente['disponibilidad'][grupo_nombre].get(f"{dia} {fila['Horario']}", tk.IntVar()).get() == 1 and
                not self.docente_ocupado_en_otro_grupo(horarios, docente, dia, fila['Horario'])]
        
    def obtener_dia_superponible(self, horarios, grupo_nombre, docente, dia):
        """Obtiene el día disponible para un docente en un grupo y día específicos."""
        for fila in horarios:
            if fila['Grupo'] == grupo_nombre and fila[dia] == "" and docente['disponibilidad'][grupo_nombre].get(f"{dia} {fila['Horario']}", tk.IntVar()).get() == 1:
                return True
        return False

    def docente_ocupado_en_otro_grupo(self, horarios, docente, dia, horario):
        """Verifica si el docente ya está ocupado en otro grupo en el mismo horario."""
        for fila in horarios:
            if fila['Horario'] == horario and fila[dia].endswith(f"({docente['nombre']})"):
                return True
        return False

#Verificar superopisiciones , y tener en cuenta que si se genera superoposion no sea en el mismo dia. 

    def asignar_horas_en_dia(self, horarios, grupo_nombre, docente, asignatura, combinacion, dia, horas_disponibles, superposiciones, dias, combinaciones_horas, dias_asignados, combinacion_restante):
        """Asigna las horas de una asignatura en un día específico, asegurando la continuidad y evitando intercalaciones."""
        horas_asignadas = 0
        horas_totales = sum(combinacion)
        horarios_contiguos = [
            ('7:15 - 7:55', '7:55 - 8:35'),
            ('7:55 - 8:35', '8:45 - 9:35'),
            ('8:45 - 9:35', '9:35 - 10:15'),
            ('9:35 - 10:15', '10:15 - 10:55'),
            ('10:15 - 10:55', '11:05 - 11:50'),
            ('11:05 - 11:50', '11:55 - 12:35'),
            ('11:55 - 12:35', '12:35 - 13:15')
        ]
        dias_utilizados = {dia: 0}  # Registro de horas asignadas por día
        dia_actual = None

        # Paso 1: Intentar asignar horas contiguas en el día especificado
        for i in range(len(horas_disponibles) - horas_totales + 1):
            contiguas = True
            for j in range(horas_totales - 1):
                intervalo_actual = horas_disponibles[i + j]
                intervalo_siguiente = horas_disponibles[i + j + 1]
                if (intervalo_actual, intervalo_siguiente) not in horarios_contiguos:
                    contiguas = False
                    break
            if contiguas:
                # Asignar horas contiguas en el día especificado
                for j in range(horas_totales):
                    intervalo = horas_disponibles[i + j]
                    for fila in horarios:
                        if fila['Grupo'] == grupo_nombre and fila['Horario'] == intervalo:
                            fila[dia] = f"{asignatura} ({docente['nombre']})"
                            horas_asignadas += 1
                            dias_utilizados[dia] += 1
                            break
                break  # Salir después de asignar las horas continuas en el día

        # Paso 2: Si no se pudieron asignar todas las horas de forma contigua, distribuir las horas restantes en otros días
        horas_restantes = horas_totales - horas_asignadas
        if horas_restantes > 0:
            for dia_restante in dias:  # Utilizar el parámetro `dias`
                if dia_restante != dia and dia_restante not in dias_utilizados and dia_restante not in dias_asignados:  # No asignar en el mismo día
                    horas_disponibles_restantes = self.obtener_horas_disponibles(horarios, grupo_nombre, docente, dia_restante)
                    for i in range(len(horas_disponibles_restantes) - horas_restantes + 1):
                        contiguas = True
                        for j in range(horas_restantes - 1):
                            intervalo_actual = horas_disponibles_restantes[i + j]
                            intervalo_siguiente = horas_disponibles_restantes[i + j + 1]
                            if (intervalo_actual, intervalo_siguiente) not in horarios_contiguos:
                                contiguas = False
                                break
                        if contiguas:
                            # Asignar las horas restantes en el nuevo día
                            for j in range(horas_restantes):
                                intervalo = horas_disponibles_restantes[i + j]
                                for fila in horarios:
                                    if fila['Grupo'] == grupo_nombre and fila['Horario'] == intervalo:
                                        fila[dia_restante] = f"{asignatura} ({docente['nombre']})"
                                        horas_asignadas += 1
                                        dias_utilizados[dia_restante] = dias_utilizados.get(dia_restante, 0) + 1
                                        break
                            dia_actual = dia_restante
                            break
                if horas_asignadas >= horas_totales:
                    break  # Salir si se asignaron todas las horas
                    
        # Deberia salir de esta funcion para cambiar de combinacion (porque recorrio toda la semana y no pudo meter la combinacion actual)
        # Verificar si estamos en la última combinación posible


        # Paso 3: Si aún quedan horas por asignar, gestionar la superposición y registrar celdas vacías
        if combinacion == combinacion_restante:
            if horas_asignadas < horas_totales:
                horas_faltantes = horas_totales - horas_asignadas
                for dia_superpuesto in dias:
                    dia_superponible = self.obtener_dia_superponible(horarios, grupo_nombre, docente, dia_superpuesto)
                    horas_disponibles = self.obtener_horas_disponibles_superponibles(horarios, grupo_nombre, docente, dia_superpuesto)
                    if dia_superponible:
                        if horas_faltantes == 0:
                            break
                        for intervalo in horas_disponibles:
                            if horas_faltantes == 0:
                                break
                            for fila in horarios:
                                if fila['Grupo'] == grupo_nombre and fila['Horario'] == intervalo:
                                    if fila[dia_superpuesto] != "":
                                        # Superposición detectada
                                        fila[dia_superpuesto] += f" / {asignatura} ({docente['nombre']})"
                                        superposiciones.append((fila['Horario'], dia_superpuesto, fila[dia_superpuesto]))
                                    else:
                                        fila[dia_superpuesto] = f"{asignatura} ({docente['nombre']})"
                                    horas_asignadas += 1
                                    horas_faltantes -= 1
                                    break

            # Paso 4: Registrar celdas vacías si no se pudieron asignar todas las horas
            if horas_asignadas < horas_totales:
                for dia_vacio in self.dias:
                    for intervalo in horas_disponibles:
                        if horas_asignadas >= horas_totales:
                            break
                        for fila in horarios:
                            if fila['Grupo'] == grupo_nombre and fila['Horario'] == intervalo and fila[dia_vacio] == "":
                                fila[dia_vacio] = "No asignada: Falta de disponibilidad"
                                self.registrar_celda_vacia(fila['Horario'], dia_vacio, "Falta de disponibilidad")
                                horas_asignadas += 1
                                break

        return horas_asignadas,dia_actual




    def generar_combinaciones_horas(self, total_horas):
        """Genera combinaciones posibles de horas para respetar la prioridad de distribución."""
        if total_horas == 2:
            return [(2,)]  # 2 horas juntas en el mismo día
        elif total_horas == 3:
            return [(3,),(2, 1) ]  # 3 horas juntas o 2 juntas + 1 separada
        elif total_horas == 4:
            return [(2, 2), (3, 1)]  # 3 + 1 o 2 + 2 (No 4 juntas ni 4 separadas)
        elif total_horas == 5:
            return [(3, 2)]  # 3 horas juntas en un día y 2 en otro
        return []


    def exportar_horarios_excel(self, horarios, superposiciones):
        """Exporta los horarios generados a un archivo de Excel con tres hojas."""
        df = pd.DataFrame(horarios)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
                # Hoja 1: Planilla de Horarios
                df.to_excel(writer, sheet_name='Horarios', index=False)

                # Hoja 2: Horarios de cada docente en cada grupo
                self.exportar_horarios_docentes_por_grupo(writer, horarios)

                # Hoja 3: Superposiciones
                self.exportar_superposiciones(writer, superposiciones, horarios)

            messagebox.showinfo("Planilla Guardada", "La planilla ha sido guardada en el archivo de Excel.")
        
        if superposiciones:
            superposiciones_str = '\n'.join(superposiciones)
            messagebox.showwarning("Superposiciones Detectadas", f"Se encontraron superposiciones en los siguientes horarios:\n{superposiciones_str}")

    def exportar_horarios_docentes_por_grupo(self, writer, horarios):
        """Exporta los horarios de cada docente por grupo a una hoja de Excel."""
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        rows = []

        # Extraer información del horario final
        for fila in horarios:
            grupo_nombre = fila['Grupo']
            intervalo = fila['Horario']
            if grupo_nombre:  # Ignorar filas vacías que separan grupos
                for dia in dias:
                    contenido = fila[dia]
                    if contenido:
                        # Extraer el docente y la asignatura
                        asignatura_docente = contenido.split(" | ")  # Puede haber varios asignados en el mismo horario
                        for ad in asignatura_docente:
                            asignatura, docente = ad.split('(')
                            docente = docente.strip(')')
                            rows.append([docente, grupo_nombre, asignatura, dia, intervalo])

        # Convertir a DataFrame
        df_docentes = pd.DataFrame(rows, columns=["Docente", "Grupo", "Asignatura", "Día", "Horario"])
        df_docentes.to_excel(writer, sheet_name='Horarios Docentes', index=False)

    def exportar_superposiciones(self, writer, superposiciones, horarios):
        """Exporta las superposiciones detectadas a una hoja de Excel si existen."""
        filas_superposiciones = []

        # Filtrar superposiciones para incluir solo las que están en la planilla final
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        for sup in superposiciones:
            # Separar la superposición en partes
            partes = sup.split(" en ")
            if len(partes) == 2:
                grupo_info, horario_info = partes
                grupo, intervalo = horario_info.split(" (")
                dia = grupo.split()[1].strip(")")
                
                # Verificar si esta superposición aparece en el horario final
                for fila in horarios:
                    if fila['Grupo'] == grupo and fila['Horario'] == intervalo:
                        if dia in dias and fila[dia].endswith(f"({partes[0].split()[1]})"):
                            filas_superposiciones.append([grupo_info, horario_info])

        # Exportar si hay superposiciones filtradas
        if filas_superposiciones:
            df_superposiciones = pd.DataFrame(filas_superposiciones, columns=["Superposición", "Detalles"])
            df_superposiciones.to_excel(writer, sheet_name='Superposiciones', index=False)

    def ver_datos(self):
        ventana_ver_datos = tk.Toplevel(self.root)
        ventana_ver_datos.title("Datos Cargados")
        
        #Crear un Frame para contener el Canvas y la Scrollbar
        frame_ver = ttk.Frame(ventana_ver_datos)
        frame_ver.pack(fill="both", expand=True)

        canvas_ver = tk.Canvas(frame_ver)
        canvas_ver.pack(side="left", fill="both", expand=True)

        scrollbar_y = ttk.Scrollbar(frame_ver, orient="vertical", command=canvas_ver.yview)
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(ventana_ver_datos, orient="horizontal", command=canvas_ver.xview)
        scrollbar_x.pack(side="top", fill="x")

        canvas_ver.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        frame_ver = tk.Frame(canvas_ver)
        canvas_ver.create_window((0, 0), window=frame_ver, anchor="nw")

        for grupo in self.grupos:
            grupo_label = tk.Label(frame_ver, text=f"Grupo: {grupo['nombre']} - Turno: {grupo['turno']}", font=("Arial", 12, "bold"))
            grupo_label.pack(pady=5)

            for docente in self.docentes:
                if grupo in docente['grupos']:
                    for asignatura, asignatura_var in docente['asignaturas'][grupo['nombre']].items():
                        if asignatura_var.get() == 1:
                            docente_label = tk.Label(frame_ver, text=f"Docente: {docente['nombre']} - Asignatura: {asignatura} - Disponibilidad: {', '.join([hora for hora, var in docente['disponibilidad'][grupo['nombre']].items() if var.get() == 1])}")
                            docente_label.pack(anchor="w")

        frame_ver.update_idletasks()
        canvas_ver.config(scrollregion=canvas_ver.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = HorariosApp(root)
    root.mainloop()