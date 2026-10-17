def simular_repeticion_drill(atributos, drill_nombre, factor_edad, descuento_cond):
    """
    Simula 1 sola repetición del drill actualizando TODOS sus atributos en tiempo real.
    Rendimiento base calibrado con prueba real: 0.342% por repetición para atributos principales.
    """
    info = DRILLS_BASE[drill_nombre]
    mult_int = MULT_INTENSIDAD.get(info["int"], 1.0)
    
    # Rendimiento calibrado (0.342% base a 145-150% GEN)
    ganancia_principal = 0.342 * factor_edad
    ganancia_cascada = ganancia_principal * 0.50 # 50% exacto para secundarios
    
    # Atributos objetivo principales del drill (los 2 primeros o principales)
    attrs_drill = info["attr"]
    
    for i, attr in enumerate(attrs_drill):
        if attr in atributos:
            # Los 2 primeros atributos reciben ganancia completa, el resto recibe ganancia de cascada
            if i < 2:
                atributos[attr] += ganancia_principal
            else:
                atributos[attr] += ganancia_cascada
                
    costo_condicion = info["costo"] * descuento_cond
    return costo_condicion

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    
    metas_dict = {
        meta1_attr: meta1_val,
        meta2_attr: meta2_val,
        meta3_attr: meta3_val
    }

    descuento_cond = 0.5 if fan_club else 1.0
    factor_edad = max(0.35, 1.0 - (edad - 18) * 0.035)

    plan_rutinas = []
    costo_condicion_total = 0.0

    # SIMULACIÓN PARALELA EN TIEMPO REAL
    # Mientras alguna meta no se haya alcanzado, seguimos entrenando
    while any(atributos_dinamicos[attr] < target for attr, target in metas_dict.items()):
        
        # 1. Identificar qué metas faltan por cumplir
        metas_pendientes = {attr: target for attr, target in metas_dict.items() if atributos_dinamicos[attr] < target}
        
        # 2. Buscar el mejor drill que cubra la MÁXIMA cantidad de metas pendientes al mismo tiempo
        mejor_drill = None
        max_coincidencias = -1
        
        for d_name, d_info in DRILLS_BASE.items():
            coincidencias = sum(1 for attr in metas_pendientes if attr in d_info["attr"])
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_drill = d_name
        
        if not mejor_drill or max_coincidencias == 0:
            # Si no hay drill que combine, tomar uno directo para la primera meta pendiente
            attr_objetivo = list(metas_pendientes.keys())[0]
            drills_compatibles = [k for k, v in DRILLS_BASE.items() if attr_objetivo in v["attr"]]
            mejor_drill = drills_compatibles[0]

        # 3. Simular bucle para el drill seleccionado hasta cumplir la meta
        reps_drill = 0
        costo_drill = 0.0
        
        # Guardar estado inicial del bloque
        attrs_iniciales_bloque = atributos_dinamicos.copy()

        while True:
            # Verificar si las metas asociadas a este drill ya se cumplieron
            metas_del_drill = [attr for attr in metas_pendientes if attr in DRILLS_BASE[mejor_drill]["attr"]]
            
            # Si se cumplieron las metas asociadas o ya no hay metas para este drill, salir
            if not metas_del_drill or all(atributos_dinamicos[attr] >= metas_dict[attr] for attr in metas_del_drill):
                break
                
            costo_rep = simular_repeticion_drill(atributos_dinamicos, mejor_drill, factor_edad, descuento_cond)
            reps_drill += 1
            costo_drill += costo_rep
            costo_condicion_total += costo_rep

        if reps_drill > 0:
            plan_rutinas.append({
                "drill": mejor_drill,
                "reps": reps_drill,
                "costo": costo_drill
            })

    packs_necesarios = round(costo_condicion_total / 15.0, 1)

    # IMPRESIÓN DE RESULTADOS
    st.success(f"¡Plan Optimizado Mínimo Costo para {nombre_jugador}!")

    k1, k2, k3 = st.columns(3)
    k1.metric("Gasto Real Total Condición", f"-{round(costo_condicion_total, 1)}%")
    k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
    k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

    st.markdown("---")
    st.subheader("📋 Circuito de Rutinas Eficiente (Simulación Paralela)")
    
    for plan in plan_rutinas:
        st.info(f"🎯 Ejecutar {plan['drill']} ➡️ {plan['reps']} repeticiones (Gasto: -{round(plan['costo'], 1)}% Condición)")
