import streamlit as st

st.set_page_config(
    page_title="Optimizador Mono-Meta - Top Eleven v2.0",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador de Precisión Mono-Meta (v2.0) - Top Eleven")
st.caption("Basado en el modelo matemático de Drill Development, Nivel de Ejercicio y absorción $2\\times$ de Habilidades Blancas.")

# DICCIONARIO COMPLETO DE EJERCICIOS CON ATRIBUTOS EXACTOS
DRILLS_BASE = {
    # ATAQUE
    "Remate 1 contra 1": {"cat": "Ataque", "costo": 6.0, "attr": ["Definición", "Regate", "Aceleración"]},
    "¡Pasa y dispara!": {"cat": "Ataque", "costo": 6.0, "attr": ["Disparo", "Pase", "Velocidad"]},
    "Jugadas balón parado": {"cat": "Ataque", "costo": 7.5, "attr": ["Disparo", "Centro", "Cabeceado"]},
    "Técnica de disparo": {"cat": "Ataque", "costo": 7.5, "attr": ["Definición", "Disparo", "Agilidad"]},
    "Driblar en slalom": {"cat": "Ataque", "costo": 9.0, "attr": ["Regate", "Pase", "Velocidad"]},
    "Jugar en las bandas": {"cat": "Ataque", "costo": 9.0, "attr": ["Centro", "Definición", "Disparo", "Cabeceado"]},
    "Contraataque rápido": {"cat": "Ataque", "costo": 10.5, "attr": ["Pase", "Creatividad", "Centro", "Disparo"]},

    # DEFENSA
    "Análisis de vídeos": {"cat": "Defensa", "costo": 4.5, "attr": ["Colocación", "Creatividad", "Valentía"]},
    "Usa la cabeza": {"cat": "Defensa", "costo": 6.0, "attr": ["Colocación", "Pase", "Cabeceado", "Creatividad"]},
    "Mantener la línea": {"cat": "Defensa", "costo": 7.5, "attr": ["Marcaje", "Colocación", "Concentración"]},
    "Parar al atacante": {"cat": "Defensa", "costo": 7.5, "attr": ["Marcaje", "Entradas", "Regate", "Valentía", "Fuerza"]},
    "Defender los centros": {"cat": "Defensa", "costo": 7.5, "attr": ["Marcaje", "Cabeceado", "Centro", "Valentía"]},
    "Juego de presión": {"cat": "Defensa", "costo": 9.0, "attr": ["Marcaje", "Entradas", "Agresividad", "Colocación", "Valentía"]},

    # POSESIÓN
    "Control del balón": {"cat": "Posesión", "costo": 4.5, "attr": ["Regate", "Creatividad", "Concentración", "Cabeceado"]},
    "Balón prisionero": {"cat": "Posesión", "costo": 6.0, "attr": ["Pase", "Entradas", "Agresividad", "Colocación"]},
    "Primer toque": {"cat": "Posesión", "costo": 6.0, "attr": ["Pase", "Regate"]},
    "Cambio de banda rápido": {"cat": "Posesión", "costo": 7.5, "attr": ["Pase", "Centro", "Creatividad", "Velocidad", "Colocación"]},
    "Mantenerse en carril": {"cat": "Posesión", "costo": 7.5, "attr": ["Velocidad", "Colocación"]},
    "Juego de contacto": {"cat": "Posesión", "costo": 7.5, "attr": ["Regate", "Fuerza", "Marcaje", "Agresividad", "Valentía"]},
    "Pases antes de disparo": {"cat": "Posesión", "costo": 9.0, "attr": ["Pase", "Definición", "Creatividad", "Colocación", "Anticipación"]},

    # FÍSICO Y MENTAL
    "Calentamiento": {"cat": "Físico y Mental", "costo": 4.5, "attr": ["Agresividad", "Cabeceado"]},
    "Estiramientos": {"cat": "Físico y Mental", "costo": 6.0, "attr": ["Agilidad", "Velocidad", "Fuerza"]},
    "Carioca con escalera": {"cat": "Físico y Mental", "costo": 6.0, "attr": ["Agilidad", "Velocidad", "Concentración", "Agresividad"]},
    "Carrera larga": {"cat": "Físico y Mental", "costo": 7.5, "attr": ["Velocidad", "Concentración"]},
    "Carreras cortas": {"cat": "Físico y Mental", "costo": 9.0, "attr": ["Velocidad", "Agilidad", "Fuerza", "Valentía"]},
    "Saltos de vallas": {"cat": "Físico y Mental", "costo": 9.0, "attr": ["Velocidad", "Valentía", "Agresividad"]},
    "Gimnasio": {"cat": "Físico y Mental", "costo": 10.5, "attr": ["Fuerza"]},
    "Sprints": {"cat": "Físico y Mental", "costo": 10.5, "attr": ["Velocidad", "Aceleración", "Regate"]}
}

MULT_NIVEL_DRILL = {
    "Aficionado": 1.00,
    "Semiprofesional": 1.11,
    "Profesional": 1.23,
    "Clase Mundial": 1.31
}

ATTR_ATAQUE = ["Disparo", "Definición", "Centro", "Pase", "Regate", "Cabeceado", "Creatividad"]
ATTR_DEFENSA = ["Marcaje", "Entradas", "Anticipación", "Colocación", "Agresividad", "Valentía", "Concentración"]
ATTR_FISICO = ["Velocidad", "Aceleración", "Fuerza", "Agilidad"]
TODOS_ATRIBUTOS = sorted(list(set(ATTR_ATAQUE + ATTR_DEFENSA + ATTR_FISICO)))

# MAPEO DE HABILIDADES BLANCAS POR ROL COMÚN
ROLES_BLANCOS = {
    "MC": ["Pase", "Creatividad", "Disparo", "Entradas", "Colocación", "Velocidad", "Fuerza"],
    "DMC": ["Pase", "Marcaje", "Entradas", "Colocación", "Valentía", "Fuerza", "Agresividad"],
    "AMC": ["Pase", "Creatividad", "Regate", "Disparo", "Definición", "Velocidad"],
    "DC": ["Marcaje", "Entradas", "Cabeceado", "Colocación", "Valentía", "Fuerza"]
}

def obtener_factor_edad(edad):
    if edad <= 21:
        return 1.00
    elif edad <= 25:
        return max(0.40, 1.00 - ((edad - 21) * 0.15))
    else:
        return max(0.20, 0.40 - ((edad - 25) * 0.04))

def simular_repeticion_v2(atributos, attr_objetivo, meta_val, drill_nombre, nivel_drill, edad, descuento_cond, blancas):
    info = DRILLS_BASE[drill_nombre]
    attrs_drill = info["attr"]
    
    factor_edad = obtener_factor_edad(edad)
    mult_nivel = MULT_NIVEL_DRILL[nivel_drill]
    
    # 1. Calcular % de desarrollo del ejercicio (respecto a 180%)
    vals_drill = [atributos.get(a, 0.0) for a in attrs_drill]
    promedio_drill = sum(vals_drill) / len(vals_drill) if vals_drill else 0.0
    desarrollo_pct = min(1.0, promedio_drill / 180.0)
    
    # 2. Freno de XP decreciente del ejercicio (Foro Top Eleven)
    freno_xp = max(0.05, (1.0 - desarrollo_pct) ** 1.2)
    
    # Pool total de XP generado por el set completo de 6 ranuras
    pool_xp_total = 2.8 * factor_edad * mult_nivel * freno_xp
    
    # 3. Pesos: Blanca = 2.0, Gris = 1.0 (absorción doble)
    pesos = [2.0 if a in blancas else 1.0 for a in attrs_drill]
    peso_total = sum(pesos)
    
    # 4. Distribución exacta entre los atributos del ejercicio (Cascada)
    for a, peso in zip(attrs_drill, pesos):
        if a in atributos:
            inc = (pool_xp_total / peso_total) * peso
            atributos[a] += inc

    costo_condicion = info["costo"] * descuento_cond
    return costo_condicion

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "Julio Lugo")
edad = st.sidebar.slider("Edad", 18, 36, 23)
rol_seleccionado = st.sidebar.selectbox("Rol del Jugador", ["MC", "DMC", "AMC", "DC"], index=0)
fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=2000)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de META ÚNICA")
meta_attr = st.sidebar.selectbox("Atributo Objetivo", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Creatividad"))
meta_val = st.sidebar.number_input("Porcentaje Meta (%)", min_value=1.0, max_value=500.0, value=200.0)
nivel_drill = st.sidebar.selectbox("Nivel del Ejercicio", list(MULT_NIVEL_DRILL.keys()), index=0)

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

# Carga de valores por defecto idénticos a las capturas reales de Lugo
defaults_julio = {
    "Pase": 246.0, "Creatividad": 131.0, "Centro": 92.0, "Disparo": 151.0, "Definición": 53.0,
    "Regate": 217.0, "Cabeceado": 143.0, "Marcaje": 221.0, "Entradas": 210.0, "Colocación": 192.0,
    "Valentía": 209.0, "Velocidad": 161.0, "Fuerza": 102.0
}

c_at, c_de, c_fi = st.columns(3)
valores_actuales = {}

with c_at:
    st.markdown("### ⚔️ Ataque")
    for attr in ATTR_ATAQUE:
        val_def = defaults_julio.get(attr, 0.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=0.0, max_value=500.0, value=val_def, key=attr)

with c_de:
    st.markdown("### 🛡️ Defensa")
    for attr in ATTR_DEFENSA:
        val_def = defaults_julio.get(attr, 0.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=0.0, max_value=500.0, value=val_def, key=attr)

with c_fi:
    st.markdown("### ⚡ Físico & Mental")
    for attr in ATTR_FISICO:
        val_def = defaults_julio.get(attr, 0.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=0.0, max_value=500.0, value=val_def, key=attr)

st.markdown("---")

btn_optimizar = st.button("🚀 CALCULAR ENTRENAMIENTO MONO-META v2.0", type="primary", use_container_width=True)

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    val_inicial = atributos_dinamicos[meta_attr]

    if val_inicial >= meta_val:
        st.warning(f"El atributo {meta_attr} ya alcanzó la meta ({val_inicial}% >= {meta_val}%).")
    else:
        descuento_cond = 0.5 if fan_club else 1.0
        blancas_jugador = ROLES_BLANCOS.get(rol_seleccionado, [])
        mejor_drill = "Contraataque rápido"

        reps_total = 0
        costo_condicion_total = 0.0

        while atributos_dinamicos[meta_attr] < meta_val and reps_total < 3000:
            costo_rep = simular_repeticion_v2(
                atributos_dinamicos, meta_attr, meta_val, mejor_drill, nivel_drill, edad, descuento_cond, blancas_jugador
            )
            reps_total += 1
            costo_condicion_total += costo_rep

        packs_necesarios = round(costo_condicion_total / 15.0, 1)

        st.success(f"¡Plan Mono-Meta Finalizado para *{nombre_jugador}*!")

        k1, k2, k3 = st.columns(3)
        k1.metric("Gasto Total Condición", f"-{round(costo_condicion_total, 1)}%")
        k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
        k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

        st.markdown("---")
        st.subheader("📋 Rutina Seleccionada")
        st.info(f"🎯 Ejercicio Recomendado: **{mejor_drill}** ({nivel_drill}) ➡️ **{reps_total} repeticiones** (Gasto: -{round(costo_condicion_total, 1)}% Condición)")

        st.markdown("---")
        st.subheader("📊 Ficha Técnica Proyectada (Cascadas Exactas)")

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
                if diff > 0:
                    st.write(f"⚡ **{attr} (Cascada)**: {val_final}% (🟢 +{diff}%)")
                else:
                    st.write(f"⚪ **{attr}**: {val_orig}% (0.0%)")

        with col_res_fis:
            st.markdown("#### ⚡ Físico & Mental")
            for attr in ATTR_FISICO:
                val_orig = valores_actuales[attr]
                val_final = round(atributos_dinamicos[attr], 1)
                diff = round(val_final - val_orig, 1)
                if diff > 0:
                    st.write(f"⚡ **{attr} (Cascada)**: {val_final}% (🟢 +{diff}%)")
                else:
                    st.write(f"⚪ **{attr}**: {val_orig}% (0.0%)")
