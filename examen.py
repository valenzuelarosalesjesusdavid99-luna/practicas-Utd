def calcular_aumento(horas):
    if horas == 10:
        return 0.20
    elif horas == 15:
        return 0.30
    elif horas == 20:
        return 0.15
    elif horas > 25:
        return 0.08
    else:
        return 0.0

def main():
    total_trabajadores = 0
    total_sueldos_netos = 0.0

    while True:
        print("\n--- Datos del trabajador ---")
        nombre = input("Nombre del trabajador: ")
        horas = float(input("Número de horas trabajadas: "))
        sueldo_por_hora = float(input("Sueldo por hora: "))

        sueldo_base = horas * sueldo_por_hora
        aumento_porcentaje = calcular_aumento(horas)
        aumento = sueldo_base * aumento_porcentaje
        sueldo_neto = sueldo_base + aumento

        print("\n--- Resultados ---")
        print(f"Trabajador: {nombre}")
        print(f"Horas trabajadas: {horas}")
        print(f"Sueldo base: {sueldo_base:.2f}")
        print(f"Aumento (%): {aumento_porcentaje * 100:.0f}%")
        print(f"Monto del aumento: {aumento:.2f}")
        print(f"Sueldo neto cobrado: {sueldo_neto:.2f}")

        total_trabajadores += 1
        total_sueldos_netos += sueldo_neto

        continuar = input("\n¿Desea ingresar otro trabajador? (s/n): ").lower()
        if continuar != 's':
            break

    print("\n--- Resumen final ---")
    print(f"Total de trabajadores ingresados: {total_trabajadores}")
    print(f"Monto total de sueldos netos: {total_sueldos_netos:.2f}")

if __name__ == "__main__":
    main()