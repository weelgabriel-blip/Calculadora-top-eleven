import streamlit as st

st.set_page_config(
    page_title="Optimizador Definitivo Top Eleven",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador Definitivo e Inteligente - Top Eleven")
st.caption("Motor Matemático Calibrado con Datos Reales de Campo (Pedro Rojas - 7 Estrellas)")

# BASE DE DATOS DE DRILLS CON ATRIBUTOS ORDENADOS (Los 2 primeros SIEMPRE son Principales)
DRILLS_BASE = {
    # ATAQUE
    "Remate 1 contra 1": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Definición", "Regate", "Aceleración", "Entradas", "Anticipación"]},
    "¡Pasa y dispara!": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Disparo", "Pase", "Velocidad", "Anticipación"]},
    "Jugadas balón parado": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Disparo", "Centro", "Aceleración", "Marcaje", "Cabeceado"]},
    "Técnica de disparo": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Definición", "Disparo", "Agilidad", "Fuerza", "Reflejos"]},
    "Driblar en slalom": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Regate", "Pase", "Velocidad", "Forma"]},
    "Jugar en las bandas": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Centro", "Definición", "Disparo", "Cabeceado", "Puños"]},
    "Contraataque rápido": {"cat": "Ataque", "int": "Muy Difícil", "costo": 10.5, "attr": ["Pase", "Creatividad", "Centro", "Definición", "Comunicación"]},

    # DEFENSA
    "Análisis de vídeos": {"cat": "Defensa", "int": "Muy Fácil", "costo": 4.5, "attr": ["Colocación", "Comunicación", "Creatividad", "Valentía"]},
    "Usa la cabeza": {"cat": "Defensa", "int": "Fácil", "costo": 6.0, "attr": ["Colocación", "Pase", "Cabeceado", "Creatividad"]},
    "Mantener la línea": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Colocación", "Concentración", "Comunicación"]},
    "Parar al atacante": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Entradas", "Regate", "Valentía", "Fuerza"]},
    "Defender los centros": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Cabeceado", "Centro", "Alcance aéreo", "Valentía"]},
    "Juego de presión": {"cat": "Defensa", "int": "Difícil", "costo": 9.0, "attr": ["Marcaje", "Entradas", "Agresividad", "Colocación", "Valentía"]},
    "Ejercicios portero": {"cat": "Defensa", "int": "Difícil", "costo": 9.0, "attr": ["Reflejos", "Agilidad", "Golpeo", "Alcance aéreo", "Lanzamiento"]},

    # POSESIÓN
    "Control del balón": {"cat": "Posesión", "int": "Muy Fácil", "costo": 4.5, "attr": ["Regate", "Creatividad", "Concentración", "Cabeceado"]},
    "Balón prisionero": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Pase", "Entradas", "Agresividad", "Colocación", "Forma"]},
    "Primer toque": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Pase", "Regate", "Forma", "Lanzamiento"]},
    "Cambio de banda rápido": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Pase", "Centro", "Creatividad", "Velocidad", "Colocación", "Comunicación"]},
    "Mantenerse en carril": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Velocidad", "Forma", "Alcance aéreo", "Colocación"]},
    "Juego de contacto": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Regate", "Fuerza", "Marcaje", "Agresividad", "Valentía"]},
    "Pases antes de disparo": {"cat": "Posesión", "int": "Difícil", "costo": 9.0, "attr": ["Pase", "Definición", "Creatividad", "Colocación", "Anticipación"]},

    # FÍSICO Y MENTAL
    "Calentamiento": {"cat": "Físico y Mental", "int": "Muy Fácil", "costo": 4.5, "attr": ["Forma", "Agresividad", "Cabeceado", "Reflejos"]},
    "Estiramientos": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Forma", "Agilidad", "Velocidad", "Fuerza"]},
    "Carioca con escalera": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Agilidad", "Velocidad", "Concentración", "Agresividad"]},
    "Carrera larga": {"cat": "Físico y Mental", "int": "Medio", "costo": 7.5, "attr": ["Velocidad", "Forma", "Concentración"]},
    "Carreras cortas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Velocidad", "Agilidad", "Fuerza", "Valentía"]},
    "Saltos de vallas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Velocidad", "Valentía", "Golpeo", "Agresividad"]},
    "Gimnasio": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Fuerza", "Forma", "Lanzamiento", "Golpeo"]},
    "Sprints": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Velocidad", "Aceleración", "Regate", "Forma"]}
}

ATTR_ATAQUE = ["Disparo", "Definición", "Centro", "Pase", "Regate", "Cabeceado", "Creatividad"]
ATTR_DEFENSA = ["Marcaje", "Entradas", "Anticipación", "Colocación", "Agresividad", "Valentía", "Concentración", "Comunicación"]
ATTR_FISICO = ["Velocidad", "Aceleración", "Fuerza", "Forma", "Agilidad"]

TODOS_ATRIBUTOS = sorted(list(set(ATTR_ATAQUE + ATTR_DEFENSA + ATTR_FISICO)))

def obtener_ganancia_base_edad(edad):
    if edad <= 18:
        return 0.55
    elif edad == 19:
        return 0.48
    elif edad == 20:
        return 0.42
    elif edad == 21:
        return 0.38
    elif edad == 22:
        return 0.342
    else:
        return max(0.18, 0.342 - (edad - 22) * 0.03)

def factor_freno_porcentaje(valor_attr):
    # TABLA CALIBRADA CON PRUEBA REAL DE PEDRO ROJAS (20 AÑOS, 170% GEN)
    if valor_attr < 100.0:
        return 1.00
    elif valor_attr < 150.0:
        return 0.85
    elif valor_attr < 200.0:
        return 0.49  # Ajuste exacto derivado de los 199 análisis de video
    elif valor_attr < 250.0:
        return 0.40
    elif valor_attr < 350.0:
        return 0.30
    else:
        return 0.20

def simular_repeticion_drill_con_freno(atributos, metas_dict, drill_nombre, base_edad, descuento_cond):
    info = DRILLS_BASE[drill_nombre]
    attrs_drill = info["attr"]
    
    hubo_progreso = False
    for i, attr in enumerate(attrs_drill):
        if attr in atributos and attr in metas_dict:
            if atributos[attr] >= metas_dict[attr]:
                continue
                
            val_actual = atributos[attr]
            factor_tramo = factor_freno_porcentaje(val_actual)
            
            if i < 2:
                ganancia = base_edad * factor_tramo
            else:
                ganancia = (base_edad * 0.50) * factor_tramo
                
            atributos[attr] = min(metas_dict[attr], atributos[attr] + ganancia)
            hubo_progreso = True
                
    costo_condicion = info["costo"] * descuento_cond if hubo_progreso else 0.0
    return costo_condicion, hubo_progreso

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "Pedro Rojas")
edad = st.sidebar.slider("Edad", 18, 36, 20)
fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=2000)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de 3 Metas")

meta1_attr = st.sidebar.selectbox("Atributo Objetivo 1", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Colocación"))
meta1_val = st.sidebar.number_input("Meta 1 (%)", min_value=1.0, max_value=500.0, value=200.0)

meta2_attr = st.sidebar.selectbox("Atributo Objetivo 2", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Regate"))
meta2_val = st.sidebar.number_input("Meta 2 (%)", min_value=1.0, max_value=500.0, value=230.0)

meta3_attr = st.sidebar.selectbox("Atributo Objetivo 3", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Centro"))
meta3_val = st.sidebar.number_input("Meta 3 (%)", min_value=1.0, max_value=500.0, value=220.0)

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

c_at, c_de, c_fi = st.columns(3)
valores_actuales = {}

with c_at:
    st.markdown("### ⚔️ Ataque")
    for attr in ATTR_ATAQUE:
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=113.0 if attr=="Centro" else (218.0 if attr=="Regate" else 80.0), key=attr)

with c_de:
    st.markdown("### 🛡️ Defensa")
    for attr in ATTR_DEFENSA:
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=138.0 if attr=="Colocación" else 75.0, key=attr)

with c_fi:
    st.markdown("### ⚡ Físico & Mental")
    for attr in ATTR_FISICO:
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=85.0, key=attr)

st.markdown("---")

btn_optimizar = st.button("🚀 OPTIMIZAR PLAN DE MÍNIMO COSTO (REAL-TIME CASCADE)", type="primary", use_container_width=True)

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    
    metas_dict = {
        meta1_attr: meta1_val,
        meta2_attr: meta2_val,
        meta3_attr: meta3_val
    }

    descuento_cond = 0.5 if fan_club else 1.0
    base_edad = obtener_ganancia_base_edad(edad)

    plan_rutinas = []
    costo_condicion_total = 0.0

    seguridad_bucle = 0
    while any(atributos_dinamicos[attr] < metas_dict[attr] for attr in metas_dict) and seguridad_bucle < 3000:
        seguridad_bucle += 1
        
        metas_pendientes = {attr: target for attr, target in metas_dict.items() if atributos_dinamicos[attr] < target}
        
        mejor_drill = None
        max_coincidencias = -1
        
        for d_name, d_info in DRILLS_BASE.items():
            coincidencias = sum(1 for attr in metas_pendientes if attr in d_info["attr"][:2])
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_drill = d_name
        
        if not mejor_drill or max_coincidencias == 0:
            attr_objetivo = list(metas_pendientes.keys())[0]
            drills_compatibles = [k for k, v in DRILLS_BASE.items() if attr_objetivo in v["attr"][:2]]
            if drills_compatibles:
                mejor_drill = drills_compatibles[0]
            else:
                mejor_drill = [k for k, v in DRILLS_BASE.items() if attr_objetivo in v["attr"]][0]

        reps_drill = 0
        costo_drill = 0.0

        while True:
            metas_del_drill_pendientes = [attr for attr in metas_pendientes if attr in DRILLS_BASE[mejor_drill]["attr"]]
            if not metas_del_drill_pendientes or all(atributos_dinamicos[attr] >= metas_dict[attr] for attr in metas_del_drill_pendientes):
                break
                
            costo_rep, progreso = simular_repeticion_drill_con_freno(
                atributos_dinamicos, metas_dict, mejor_drill, base_edad, descuento_cond
            )
            
            if not progreso:
                break
                
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

    st.success(f"¡Plan Optimizado Mínimo Costo para {nombre_jugador}!")

    k1, k2, k3 = st.columns(3)
    k1.metric("Gasto Real Total Condición", f"-{round(costo_condicion_total, 1)}%")
    k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
    k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

    st.markdown("---")
    st.subheader("📋 Circuito de Rutinas Eficiente (Simulación Paralela)")
    
    for plan in plan_rutinas:
        st.info(f"🎯 Ejecutar {plan['drill']} ➡️ {plan['reps']} repeticiones (Gasto: -{round(plan['costo'], 1)}% Condición)")

    st.markdown("---")
    st.subheader("📊 Pronóstico de la Ficha Técnica Final Proyectada")

    col_res_ataq, col_res_def, col_res_fis = st.columns(3)

    with col_res_ataq:
        st.markdown("#### ⚔️ Ataque")
        for attr in ATTR_ATAQUE:
            val_orig = valores_actuales[attr]
            val_final = round(atributos_dinamicos[attr], 1)
            diff = round(val_final - val_orig, 1)
            if attr in metas_dict:
                st.write(f"🎯 {attr} (META): {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ {attr} (Cascada): {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ {attr}: {val_orig}% (0.0%)")

    with col_res_def:
        st.markdown("#### 🛡️ Defensa")
        for attr in ATTR_DEFENSA:
            val_orig = valores_actuales[attr]
            val_final = round(atributos_dinamicos[attr], 1)
            diff = round(val_final - val_orig, 1)
            if attr in metas_dict:
                st.write(f"🎯 {attr} (META): {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ {attr} (Cascada): {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ {attr}: {val_orig}% (0.0%)")

    with col_res_fis:
        st.markdown("#### ⚡ Físico & Mental")
        for attr in ATTR_FISICO:
            val_orig = valores_actuales[attr]
            val_final = round(atributos_dinamicos[attr], 1)
            diff = round(val_final - val_orig, 1)
            if attr in metas_dict:
                st.write(f"🎯 {attr} (META): {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ {attr} (Cascada): {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ {attr}: {val_orig}% (0.0%)")
