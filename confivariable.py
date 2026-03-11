# --- CONSTANTES (Valores investigados RD) ---
TASA_AFP = 0.0287  # 2.87%
TASA_SFS = 0.0304  # 3.04%
TASA_ISR = 0.15    # 15% (Tramo simplificado)
TASA_BONO = 0.0833 # Equivalente aproximado a un salario por año

def calcular_nomina():
    print("\n--- Sistema de Cálculo de Sueldo Neto ---")
    
    try:
        # --- ENTRADA DE DATOS ---
        sueldo_bruto = float(input("Ingrese el sueldo bruto mensual: "))
        otros_descuentos = float(input("Ingrese otros descuentos (si no hay, use 0): "))

        # --- VALIDACIÓN ---
        if sueldo_bruto <= 0:
            print("Error: El sueldo debe ser un valor positivo.")
            return

        # --- PROCESO DE CÁLCULO ---
        # 1. Seguridad Social (TSS)
        desc_afp = sueldo_bruto * TASA_AFP
        desc_sfs = sueldo_bruto * TASA_SFS
        total_tss = desc_afp + desc_sfs

        # 2. Impuesto Sobre la Renta (Sobre el sueldo neto de TSS)
        base_isr = sueldo_bruto - total_tss
        desc_isr = base_isr * TASA_ISR

        # 3. Bonificación (Opcional según el ejercicio)
        bono = sueldo_bruto * TASA_BONO

        # 4. Cálculo Final
        sueldo_neto = (sueldo_bruto - total_tss - desc_isr - otros_descuentos) + bono

        # --- SALIDA DE RESULTADOS ---
        print("\n========================================")
        print(f"Sueldo Bruto:          RD$ {sueldo_bruto:,.2f}")
        print(f"Descuento TSS (AFP+SFS): RD$ {total_tss:,.2f}")
        print(f"Retención ISR:         RD$ {desc_isr:,.2f}")
        print(f"Otros Descuentos:      RD$ {otros_descuentos:,.2f}")
        print(f"Bonificación:          RD$ {bono:,.2f}")
        print("----------------------------------------")
        print(f"SUELDO NETO:           RD$ {sueldo_neto:,.2f}")
        print("========================================\n")

    except ValueError:
        print("Error: Por favor, ingrese un monto numérico válido.")

# Esto hace que el programa inicie al presionar Play
if __name__ == "__main__":
    calcular_nomina()