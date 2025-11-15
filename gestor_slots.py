from datetime import datetime

class Slot:
    def __init__(self, **kwargs):
        # Asigna directamente los valores
        for clave, valor in kwargs.items():
            setattr(self, clave.strip().lower(), str(valor).strip())

        # Estado en memoria (por defecto todos disponibles)
        self.estado = "disponible"

        # Normaliza el horario al formato HH:MM si es posible
        try:
            hora = datetime.strptime(self.hora.strip(), "%H:%M")
            self.hora = hora.strftime("%H:%M")
        except Exception:
            self.hora = getattr(self, "hora", "")

    def __str__(self):
        dia = getattr(self, "dia", "Desconocido")
        hora = getattr(self, "hora", "Sin hora")
        estado = getattr(self, "estado", "Desconocido")
        return f"{dia} - {hora} ({estado})"


class GestorSlots:
    def __init__(self, db_slots):
        self.db_slots = db_slots
        self.transf_slots, self.slots = self.db_slots.read()

        # Inicializa todos los slots como disponibles
        i = 0
        while i < len(self.slots):
            slot = self.slots[i]
            if not hasattr(slot, "estado"):
                slot.estado = "disponible"
            i = i + 1

    def validar_dia(self, dia_str):
        # Valida que el día sea un número entero entre 1 y 31
        es_valido = False
        try:
            dia = int(dia_str.strip())
            if dia >= 1 and dia <= 31:
                es_valido = True
        except Exception:
            es_valido = False
        return es_valido

    def validar_hora(self, hora_str):
        # Valida el formato HH:MM usando datetime
        es_valido = False
        try:
            hora_normalizada = datetime.strptime(hora_str.strip(), "%H:%M")
            es_valido = True
        except Exception:
            es_valido = False
        return es_valido

    def listar_slots(self, dia_filtrado=None):
        if not self.slots:
            print("No hay horarios disponibles.")
            return

        print("\nHORARIOS DISPONIBLES:")
        i = 0
        hay_disponibles = False
        while i < len(self.slots):
            slot = self.slots[i]
            dia_slot = getattr(slot, "dia", None)
            hora_slot = getattr(slot, "hora", None)
            estado_slot = getattr(slot, "estado", "disponible")

            if (dia_filtrado is None or str(dia_slot) == str(dia_filtrado)) and estado_slot == "disponible":
                print(f"[{i + 1}] Día {dia_slot} - {hora_slot}")
                hay_disponibles = True
            i = i + 1

        if not hay_disponibles:
            print("No hay horarios disponibles para ese día.")

    def seleccionar_slot(self):
        if not self.slots:
            print("No hay slots cargados.")
            return None

        dia_ingresado = input("\nIngrese el día (1–31): ").strip()
        if not self.validar_dia(dia_ingresado):
            print("Día inválido. Debe estar entre 1 y 31.")
            return None

        print(f"--- Horarios disponibles para el día {dia_ingresado} ---")
        self.listar_slots(dia_ingresado)

        hora_ingresada = input("Ingrese el horario (HH:MM): ").strip()
        if not self.validar_hora(hora_ingresada):
            print("Formato de hora inválido. Debe ser HH:MM (por ejemplo 09:30).")
            return None

        hora_normalizada = hora_ingresada.strip()
        dia_normalizado = dia_ingresado.strip()

        i = 0
        while i < len(self.slots):
            slot = self.slots[i]
            dia_slot = str(getattr(slot, "dia", "")).strip()
            hora_slot = str(getattr(slot, "hora", "")).strip()
            estado_slot = getattr(slot, "estado", "disponible")

            if dia_slot == dia_normalizado and hora_slot == hora_normalizada:
                if estado_slot == "ocupado":
                    print("Ese horario ya está ocupado.")
                    return None

                # Marca como ocupado solo en memoria
                slot.estado = "ocupado"
                print(f"Turno asignado: Día {dia_slot} - {hora_slot}")
                return slot
            i = i + 1

        print("No se encontró un horario disponible para esa fecha.")
        return None
    
    def seleccionar_slot_para_empleado(self, id_empleado, dia, turnos_existentes, lista_empleados=None):
        # Recolectar horarios desde slots.csv 
        horarios = []
        horarios_slots = {}
        i = 0
        while i < len(self.slots):
            s = self.slots[i]
            if str(getattr(s, "dia", "")).strip() == str(dia):
                hora_s = str(getattr(s, "hora", "")).strip()
                if hora_s not in horarios:
                    horarios.append(hora_s)
                    horarios_slots[hora_s] = s
            i += 1

        # Recolectar horarios adicionales desde turnos.csv
        j = 0
        while j < len(turnos_existentes):
            t = turnos_existentes[j]
            try:
                id_t = str(getattr(t, "id_empleado", "")).strip()
                dia_t = str(getattr(t, "dia", "")).strip()
                hora_t = str(getattr(t, "hora", "")).strip()
                if not (id_t or dia_t or hora_t) and hasattr(t, "__getitem__"):
                    raise TypeError
            except Exception:
                if hasattr(t, "__getitem__") and len(t) >= 5:
                    id_t = str(t[0]).strip()
                    dia_t = str(t[3]).strip()
                    hora_t = str(t[4]).strip()
                else:
                    id_t = dia_t = hora_t = ""

            if dia_t == str(dia) and hora_t and hora_t not in horarios:
                horarios.append(hora_t)
            j += 1

        if not horarios:
            print(f"No hay horarios configurados ni registrados para el día {dia}.")
            return None

        # Determinar ocupación (y nombres si hay lista de empleados disponible)
        entries = []
        p = 0
        while p < len(horarios):
            hora = horarios[p]
            slot_obj = horarios_slots.get(hora, None)
            ocupado_por = None
            nombre_ocupante = ""

            q = 0
            while q < len(turnos_existentes):
                t = turnos_existentes[q]
                try:
                    id_t = str(getattr(t, "id_empleado", "")).strip()
                    dia_t = str(getattr(t, "dia", "")).strip()
                    hora_t = str(getattr(t, "hora", "")).strip()
                    if not (id_t or dia_t or hora_t) and hasattr(t, "__getitem__"):
                        raise TypeError
                except Exception:
                    if hasattr(t, "__getitem__") and len(t) >= 5:
                        id_t = str(t[0]).strip()
                        dia_t = str(t[3]).strip()
                        hora_t = str(t[4]).strip()
                    else:
                        id_t = dia_t = hora_t = ""

                if dia_t == str(dia) and hora_t == hora:
                    ocupado_por = id_t
                    break
                q += 1

            # Buscar nombre del empleado que ocupa ese horario
            if ocupado_por and lista_empleados:
                r = 0
                while r < len(lista_empleados):
                    emp = lista_empleados[r]
                    emp_id = (
                        str(getattr(emp, "id_empleado", "")) 
                        or str(getattr(emp, "\ufeffid_empleado", "")) 
                        or str(getattr(emp, "id", ""))
                    )
                    if emp_id == ocupado_por:
                        nombre_ocupante = (
                            f"{getattr(emp, 'nombre', '')} {getattr(emp, 'apellido', '')}".strip()
                        )
                        break
                    r += 1

            entries.append((hora, slot_obj, ocupado_por, nombre_ocupante))
            p += 1

        # Mostrar horarios
        print(f"\n--- Horarios disponibles / registrados para el día {dia} ---")
        idx = 0
        while idx < len(entries):
            hora, _, ocupado_por, nombre_ocupante = entries[idx]
            etiqueta = f"[{idx + 1}] Día {dia} - {hora}"
            if ocupado_por:
                if nombre_ocupante:
                    etiqueta += f"  (OCUPADO por {nombre_ocupante})"
                else:
                    etiqueta += f"  (OCUPADO por id={ocupado_por})"
            print(etiqueta)
            idx += 1

        # Selección 
        entrada = input("Ingrese el horario (HH:MM) o el número de la lista: ").strip()
        sel = None
        try:
            num = int(entrada) - 1
            if 0 <= num < len(entries):
                sel = entries[num]
        except Exception:
            n = 0
            while n < len(entries):
                if entries[n][0] == entrada:
                    sel = entries[n]
                    break
                n += 1

        if sel is None:
            print("No se seleccionó un horario válido.")
            return None

        hora_sel, slot_sel_obj, ocupado_por_id, _ = sel

        # Validación de ocupación 
        if ocupado_por_id and str(ocupado_por_id) == str(id_empleado):
            print(f"Ese horario ya está ocupado por este empleado (id={id_empleado}).")
            return None

        # Crear pseudo-slot si no existe 
        if slot_sel_obj is None:
            class _PseudoSlot:
                pass
            pseudo = _PseudoSlot()
            setattr(pseudo, "dia", str(dia))
            setattr(pseudo, "hora", hora_sel)
            setattr(pseudo, "estado", "ocupado" if ocupado_por_id else "disponible")
            slot_sel_obj = pseudo

        return slot_sel_obj