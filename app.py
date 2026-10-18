import streamlit as st

st.set_page_config(
    page_title="Optimizador Mono-Meta - Top Eleven",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador de Precisión (Mono-Meta 6 Ranuras) - Top Eleven")
st.caption("Motor Matemático Calibrado: Jerarquía Completa de Atributos + Valores Iniciales de Campo")

# BASE DE DATOS DE DRILLS CON ATRIBUTOS ORDENADOS
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
        return 0.75
    elif edad <= 20:
        return 0.70
    elif edad <= 22:
        return 0.66
    else:
        return 0.64

def factor_freno_porcentaje(valor_attr):
    if valor_attr < 200.0:
        return 1.00
    elif valor_attr < 250.0:
        return 0.50
    elif valor_attr < 350.0:
        return 0.30
    else:
        return 0.18

def simular_repeticion_mono_meta(atributos, attr_objetivo, meta_val, drill_nombre, base_edad, descuento_cond):
    info = DRILLS_BASE[drill_nombre]
    attrs_drill = info["attr"]
    
    idx_meta = attrs_drill.index(attr_objetivo)
    val_actual_meta = atributos[attr_objetivo]
    factor_tramo_meta = factor_freno_porcentaje(val_actual_meta)
    
    # Ganancia para la meta seleccionada
    ganancia_meta = (base_edad if idx_meta < 2 else base_edad * 0.50) * factor_tramo_meta
    atributos[attr_objetivo] = min(meta_val, atributos[attr_objetivo] + ganancia_meta)
    
    # Actualización en cascada para TODOS los demás atributos del drill
    for i, a in enumerate(attrs_drill):
        if a != attr_objetivo and a in atributos:
            v_act = atributos[a]
            f_tramo = factor_freno_porcentaje(v_act)
            es_principal = (i < 2)
            g = (base_edad if es_principal else base_edad * 0.50) * f_tramo
            atributos[a] += g

    costo_condicion = info["costo"] * descuento_cond
    return costo_condicion

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "Julio Lugo")
edad = st.sidebar.slider("Edad", 18, 36, 23)
fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=1115)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de META ÚNICA")

meta_attr = st.sidebar.selectbox("Atributo Objetivo", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Creatividad"))
meta_val = st.sidebar.number_input("Porcentaje Meta (%)", min_value=1.0, max_value=500.0, value=200.0)

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

c_at, c_de, c_fi = st.columns(3)
valores_actuales = {}

# VALORES INICIALES EXACTOS DE JULIO LUGO EN CAMPO
DEFAULTS_JULIO_LUGO = {
    "Disparo": 151.0,
    "Definición": 53.0,
    "Centro": 52.0,
    "Pase": 246.0,
    "Regate": 217.0,
    "Cabeceado": 143.0,
    "Creatividad": 131.0,
    "Marcaje": 221.0,
    "Entradas": 210.0,
    "Anticipación": 75.0,
    "Colocación": 192.0,
    "Agresividad": 76.0,
    "Valentía": 209.0,
    "Concentración": 75.0,
    "Comunicación": 75.0,
    "Velocidad": 161.0,
    "Aceleración": 85.0,
    "Fuerza": 102.0,
    "Forma": 67.0,
    "Agilidad": 85.0
}

with c_at:
    st.markdown("### ⚔️ Ataque")
    for attr in ATTR_ATAQUE:
        def_val = DEFAULTS_JULIO_LUGO.get(attr, 80.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=def_val, key=attr)

with c_de:
    st.markdown("### 🛡️ Defensa")
    for attr in ATTR_DEFENSA:
        def_val = DEFAULTS_JULIO_LUGO.get(attr, 75.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=def_val, key=attr)

with c_fi:
    st.markdown("### ⚡ Físico & Mental")
    for attr in ATTR_FISICO:
        def_val = DEFAULTS_JULIO_LUGO.get(attr, 85.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=def_val, key=attr)

st.markdown("---")

btn_optimizar = st.button("🚀 CALCULAR ENTRENAMIENTO MONO-META (6 RANURAS)", type="primary", use_container_width=True)

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    val_inicial = atributos_dinamicos[meta_attr]

    if val_inicial >= meta_val:
        st.warning(f"El atributo {meta_attr} ya alcanzó o superó la meta ({val_inicial}% >= {meta_val}%).")
    else:
        descuento_cond = 0.5 if fan_club else 1.0
        base_edad = obtener_ganancia_base_edad(edad)

        drills_principales = [k for k, v in DRILLS_BASE.items() if meta_attr in v["attr"][:2]]
        
        if drills_principales:
            mejor_drill = drills_principales[0]
        else:
            mejor_drill = [k for k, v in DRILLS_BASE.items() if meta_attr in v["attr"]][0]

        reps_total = 0
        costo_condicion_total = 0.0

        while atributos_dinamicos[meta_attr] < meta_val and reps_total < 3000:
            costo_rep = simular_repeticion_mono_meta(
                atributos_dinamicos, meta_attr, meta_val, mejor_drill, base_edad, descuento_cond
            )
            reps_total += 1
            costo_condicion_total += costo_rep

        sesiones_6_ranuras = (reps_total + 5) // 6
        costo_sesion = DRILLS_BASE[mejor_drill]["costo"] * 6 * descuento_cond
        gasto_real_condicion = sesiones_6_ranuras * costo_sesion
        
        packs_necesarios = round((gasto_real_condicion / 15.0) * 2.17, 1)

        st.success(f"¡Plan Mono-Meta Finalizado para *{nombre_jugador}*!")

        k1, k2, k3 = st.columns(3)
        k1.metric("Gasto Total Condición", f"-{round(gasto_real_condicion, 1)}%")
        k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
        k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

        st.markdown("---")
        st.subheader("📋 Rutina Seleccionada (6 Ranuras Llenas)")
        st.info(f"🎯 Ejercicio Recomendado: **{mejor_drill}** ➡️ **{sesiones_6_ranuras} sesiones de 6 ranuras** ({reps_total} repeticiones totales | Gasto: -{round(gasto_real_condicion, 1)}% Condición)")

        st.markdown("---")
        st.subheader("📊 Ficha Técnica Proyectada tras el Entrenamiento")

        col_res_ataq, col_res_def, col_res_fis = st.columns(3)

        with col_res_ataq:
            st.markdown("#### ⚔️ Ataque")
            for attr in ATTR_ATAQUE:
                val_orig = valores_actuales[attr]
                val_final = round(atributos_dinamicos[attr], 1)
                diff = round(val_final - val_orig, 1)
                if attr == meta_attr:
                    st.write(f"🎯 **{attr} (META)**: {val_final}% (🟢 +{diff}%)")
                elif diff > 0:
                    st.write(f"⚡ **{attr} (Cascada)**: {val_final}% (🟢 +{diff}%)")
                else:
                    st.write(f"⚪ **{attr}**: {val_orig}% (0.0%)")

        with col_res_def:
            st.markdown("#### 🛡️ Defensa")
            for attr in ATTR_DEFENSA:
                val_orig = valores_actuales[attr]
                val_final = round(atributos_dinamicos[attr], 1)
                diff = round(val_final - val_orig, 1)
                if attr == meta_attr:
                    st.write(f"🎯 **{attr} (META)**: {val_final}% (🟢 +{diff}%)")
                elif diff > 0:
                    st.write(f"⚡ **{attr} (Cascada)**: {val_final}% (🟢 +{diff}%)")
                else:
                    st.write(f"⚪ **{attr}**: {val_orig}% (0.0%)")

        with col_res_fis:
            st.markdown("#### ⚡ Físico & Mental")
            for attr in ATTR_FISICO:
                val_orig = valores_actuales[attr]
                val_final = round(atributos_dinamicos[attr], 1)
                diff = round(val_final - val_orig, 1)
                if attr == meta_attr:
                    st.write(f"🎯 **{attr} (META)**: {val_final}% (🟢 +{diff}%)")
                elif diff > 0:
                    st.write(f"⚡ **{attr} (Cascada)**: {val_final}% (🟢 +{diff}%)")
                else:
                    st.write(f"⚪ **{attr}**: {val_orig}% (0.0%)")
