import streamlit as st

st.set_page_config(
    page_title="Optimizador Definitivo Top Eleven",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador Definitivo e Inteligente - Top Eleven")
st.caption("Sistema de cálculo con Cascada en Tiempo Real: Elimina rutinas redundantes y ahorra el máximo de Green Packs.")

# BASE DE DATOS DE DRILLS Y ATRIBUTOS REALES
DRILLS_BASE = {
    # ATAQUE
    "Remate 1 contra 1": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Entradas", "Aceleración", "Definición", "Regate", "Anticipación"]},
    "¡Pasa y dispara!": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Anticipación", "Velocidad", "Disparo", "Pase"]},
    "Jugadas balón parado": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Centro", "Aceleración", "Disparo", "Cabeceado"]},
    "Técnica de disparo": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Agilidad", "Definición", "Disparo", "Fuerza", "Reflejos"]},
    "Driblar en slalom": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Regate", "Forma", "Velocidad", "Pase"]},
    "Jugar en las bandas": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Puños", "Centro", "Definición", "Disparo", "Cabeceado"]},
    "Contraataque rápido": {"cat": "Ataque", "int": "Muy Difícil", "costo": 10.5, "attr": ["Comunicación", "Centro", "Definición", "Pase", "Creatividad"]},

    # DEFENSA
    "Análisis de vídeos": {"cat": "Defensa", "int": "Muy Fácil", "costo": 4.5, "attr": ["Creatividad", "Valentía", "Colocación", "Comunicación"]},
    "Usa la cabeza": {"cat": "Defensa", "int": "Fácil", "costo": 6.0, "attr": ["Creatividad", "Cabeceado", "Colocación", "Pase"]},
    "Mantener la línea": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Comunicación", "Concentración", "Colocación", "Marcaje"]},
    "Parar al atacante": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Entradas", "Regate", "Valentía", "Fuerza"]},
    "Defender los centros": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Alcance aéreo", "Centro", "Valentía", "Cabeceado"]},
    "Juego de presión": {"cat": "Defensa", "int": "Difícil", "costo": 9.0, "attr": ["Marcaje", "Entradas", "Agresividad", "Colocación", "Valentía"]},
    "Ejercicios portero": {"cat": "Defensa", "int": "Difícil", "costo": 9.0, "attr": ["Agilidad", "Golpeo", "Alcance aéreo", "Lanzamiento", "Reflejos"]},

    # POSESIÓN
    "Control del balón": {"cat": "Posesión", "int": "Muy Fácil", "costo": 4.5, "attr": ["Creatividad", "Concentración", "Cabeceado", "Regate"]},
    "Balón prisionero": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Entradas", "Agresividad", "Colocación", "Pase", "Forma"]},
    "Primer toque": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Regate", "Forma", "Lanzamiento", "Pase"]},
    "Cambio de banda rápido": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Pase", "Creatividad", "Colocación", "Comunicación", "Centro", "Velocidad"]},
    "Mantenerse en carril": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Forma", "Velocidad", "Alcance aéreo", "Colocación"]},
    "Juego de contacto": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Agresividad", "Regate", "Valentía", "Fuerza"]},
    "Pases antes de disparo": {"cat": "Posesión", "int": "Difícil", "costo": 9.0, "attr": ["Definición", "Colocación", "Pase", "Creatividad", "Anticipación"]},

    # FÍSICO Y MENTAL
    "Calentamiento": {"cat": "Físico y Mental", "int": "Muy Fácil", "costo": 4.5, "attr": ["Forma", "Cabeceado", "Reflejos", "Agresividad"]},
    "Estiramientos": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Forma", "Agilidad", "Velocidad", "Fuerza"]},
    "Carioca con escalera": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Concentración", "Agilidad", "Velocidad", "Agresividad"]},
    "Carrera larga": {"cat": "Físico y Mental", "int": "Medio", "costo": 7.5, "attr": ["Velocidad", "Forma", "Concentración"]},
    "Carreras cortas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Agilidad", "Valentía", "Velocidad", "Fuerza"]},
    "Saltos de vallas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Valentía", "Velocidad", "Golpeo", "Agresividad"]},
    "Gimnasio": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Forma", "Lanzamiento", "Golpeo", "Fuerza"]},
    "Sprints": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Forma", "Velocidad", "Aceleración", "Regate"]}
}

MULT_INTENSIDAD = {"Muy Fácil": 0.8, "Fácil": 1.0, "Medio": 1.3, "Difícil": 1.7, "Muy Difícil": 2.2}

ATTR_ATAQUE = ["Disparo", "Definición", "Centro", "Pase", "Regate", "Cabeceado", "Creatividad"]
ATTR_DEFENSA = ["Marcaje", "Entradas", "Anticipación", "Colocación", "Agresividad", "Valentía", "Concentración", "Comunicación"]
ATTR_FISICO = ["Velocidad", "Aceleración", "Fuerza", "Forma", "Agilidad"]

TODOS_ATRIBUTOS = sorted(list(set(ATTR_ATAQUE + ATTR_DEFENSA + ATTR_FISICO)))

def simular_repeticion_drill(atributos, drill_nombre, factor_edad, descuento_cond):
    info = DRILLS_BASE[drill_nombre]
    ganancia_principal = 0.342 * factor_edad
    ganancia_cascada = ganancia_principal * 0.50

    attrs_drill = info["attr"]
    
    for i, attr in enumerate(attrs_drill):
        if attr in atributos:
            if i < 2:
                atributos[attr] += ganancia_principal
            else:
                atributos[attr] += ganancia_cascada
                
    costo_condicion = info["costo"] * descuento_cond
    return costo_condicion

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "weel")
edad = st.sidebar.slider("Edad", 18, 36, 18)
fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=2000)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de 3 Metas")

meta1_attr = st.sidebar.selectbox("Atributo Objetivo 1", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Definición"))
meta1_val = st.sidebar.number_input("Meta 1 (%)", min_value=1.0, max_value=500.0, value=220.0)

meta2_attr = st.sidebar.selectbox("Atributo Objetivo 2", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Disparo"))
meta2_val = st.sidebar.number_input("Meta 2 (%)", min_value=1.0, max_value=500.0, value=180.0)

meta3_attr = st.sidebar.selectbox("Atributo Objetivo 3", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Velocidad"))
meta3_val = st.sidebar.number_input("Meta 3 (%)", min_value=1.0, max_value=500.0, value=150.0)

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

c_at, c_de, c_fi = st.columns(3)
valores_actuales = {}

with c_at:
    st.markdown("### ⚔️ Ataque")
    for attr in ATTR_ATAQUE:
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=80.0, key=attr)

with c_de:
    st.markdown("### 🛡️ Defensa")
    for attr in ATTR_DEFENSA:
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=75.0, key=attr)

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
    factor_edad = max(0.35, 1.0 - (edad - 18) * 0.035)

    plan_rutinas = []
    costo_condicion_total = 0.0

    while any(atributos_dinamicos[attr] < target for attr, target in metas_dict.items()):
        metas_pendientes = {attr: target for attr, target in metas_dict.items() if atributos_dinamicos[attr] < target}
        
        mejor_drill = None
        max_coincidencias = -1
        
        for d_name, d_info in DRILLS_BASE.items():
            coincidencias = sum(1 for attr in metas_pendientes if attr in d_info["attr"])
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_drill = d_name
        
        if not mejor_drill or max_coincidencias == 0:
            attr_objetivo = list(metas_pendientes.keys())[0]
            drills_compatibles = [k for k, v in DRILLS_BASE.items() if attr_objetivo in v["attr"]]
            mejor_drill = drills_compatibles[0]

        reps_drill = 0
        costo_drill = 0.0

        while True:
            metas_del_drill = [attr for attr in metas_pendientes if attr in DRILLS_BASE[mejor_drill]["attr"]]
            
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
