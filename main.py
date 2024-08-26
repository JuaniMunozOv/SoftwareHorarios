import tkinter as tk
from grupos import GruposApp
from docentes import DocentesApp
import pandas as pd
from tkinter import filedialog, messagebox

def main():
    # Primero, ejecutamos la aplicación de grupos
    root_grupos = tk.Tk()
    app_grupos = GruposApp(root_grupos)
    root_grupos.mainloop()

    # Obtenemos los grupos cargados
    grupos = app_grupos.get_grupos()
    print("Grupos cargados:", grupos)  # Depuración

    # Luego, ejecutamos la aplicación de docentes
    if grupos:
        root_docentes = tk.Tk()
        docentes_app = DocentesApp(root_docentes, grupos)
        root_docentes.mainloop()

        # Obtenemos los docentes cargados
        docentes = docentes_app.get_docentes()
        print("Docentes cargados:", docentes)  # Depuración

        # Crear ventana para generación de planilla si hay docentes
        if docentes:
            generar_planilla(docentes, grupos)
        else:
            print("No se han registrado docentes.")
    else:
        print("No se cargaron grupos. No se puede continuar con la carga de docentes.")

def generar_planilla(docentes, grupos):
    # Crear ventana para botón de generación de planilla
    root_planilla = tk.Tk()
    root_planilla.title("Generar Planilla")

    tk.Label(root_planilla, text="Generación de Planilla Final").pack(pady=10)
    tk.Button(root_planilla, text="Generar y Guardar Planilla", command=lambda: guardar_planilla(docentes, grupos)).pack(pady=20)

    root_planilla.mainloop()

def guardar_planilla(docentes, grupos):
    horarios = []
    for grupo in grupos:
        grupo_nombre = grupo['nombre']
        for i, intervalo in enumerate(grupo['horarios']):
            fila = {
                "Grupo": grupo_nombre if i == 0 else "",
                "Horario": intervalo,
                "Lunes": "",
                "Martes": "",
                "Miércoles": "",
                "Jueves": "",
                "Viernes": ""
            }
            horarios.append(fila)

    for docente in docentes:
        for asignatura, disponibilidad in docente['disponibilidad'].items():
            horas_totales = sum(len(horas) for horas in disponibilidad.values())
            if horas_totales == 2:
                distribuir_horas(asignatura, disponibilidad, horarios, 2, 2)
            elif horas_totales == 3:
                distribuir_horas(asignatura, disponibilidad, horarios, 3, 2, 1)
            elif horas_totales == 4:
                distribuir_horas(asignatura, disponibilidad, horarios, 4, 3, 1, 2, 2)
            elif horas_totales == 5:
                distribuir_horas(asignatura, disponibilidad, horarios, 5, 3, 2)

    df = pd.DataFrame(horarios)
    filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if filepath:
        df.to_excel(filepath, index=False)
        messagebox.showinfo("Planilla Guardada", "La planilla ha sido guardada en el archivo de Excel.")

def distribuir_horas(asignatura, disponibilidad, horarios, horas_totales, *reglas):
    for regla in reglas:
        if horas_totales == regla:
            for dia, horas in disponibilidad.items():
                if len(horas) >= regla:
                    for i in range(len(horarios)):
                        if horarios[i]["Horario"] in horas[:regla]:
                            horarios[i][dia] = asignatura
                    horas_totales -= regla
                    break
            if horas_totales == 0:
                break

if __name__ == "__main__":
    main()