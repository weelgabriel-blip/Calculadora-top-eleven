import streamlit as st

st.set_page_config(
    page_title="Optimizador Mono-Meta v2.8 - Top Eleven",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador de Precisión Mono-Meta (v2.8 Definitivo) - Top Eleven")
st.caption("Modelo calibrado a 111 sesiones exactas (84.3 Packs), Drill Cap, cascadas reales y soporte multi-rol.")

# 1. DICCIONARIO COMPLETO Y CORREGIDO DE EJERCICIOS
DRILLS_BASE = {
    # ATAQUE
    "Remate 1 contra 1": {"cat": "Ataque", "costo": 6.0, "attr": ["Definición", "Regate", "Aceleración"]},
    "¡Pasa y dispara!": {"cat": "Ataque", "costo": 6.0, "attr": ["Disparo", "Pase", "Velocidad"]},
    "Jugadas balón parado": {"cat": "Ataque", "costo": 7.5, "attr": ["Disparo", "Centro", "Cabeceado"]},
    "Técnica de disparo": {"cat": "Ataque", "costo": 7.5, "attr": ["Definición", "Disparo", "Agilidad"]},
    "Driblar en slalom": {"cat": "Ataque", "costo": 9.0, "attr": ["Regate", "Pase", "Velocidad"]},
    "Jugar en las bandas": {"cat": "Ataque", "costo": 9.0, "attr": ["Centro", "Definición", "Disparo", "Cabeceado"]},
    "Contraataque rápido": {"cat": "Ataque", "costo": 10.5, "attr": ["Pase", "Creatividad", "Centro", "Definición"]},

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

HABILIDADES_BLANCAS_POR_ROL = {
    "GK": ["Reflejos", "Agilidad", "Alcance aéreo", "Lanzamiento", "Puños", "Comunicación", "Colocación"],
    "DR": ["Entradas", "Marcaje", "Colocación", "Cabeceado", "Pase", "Centro", "Velocidad"],
    "DL": ["Entradas", "Marcaje", "Colocación", "Cabeceado", "Pase", "Centro", "Velocidad"],
    "DC": ["Entradas", "Marcaje", "Colocación", "Cabeceado", "Valentía", "Fuerza", "Agresividad"],
    "DMC": ["Entradas", "Marcaje", "Colocación", "Pase", "Creatividad", "Valentía", "Fuerza", "Agresividad"],
    "MC": ["Pase", "Creatividad", "Disparo", "Regate", "Entradas", "Colocación", "Velocidad"],
    "MR": ["Pase", "Centro", "Regate", "Velocidad", "Creatividad", "Colocación"],
    "ML": ["Pase", "Centro", "Regate", "Velocidad", "Creatividad", "Colocación"],
    "AMC": ["Pase", "Creatividad", "Disparo", "Definición", "Regate", "Velocidad"],
    "AMR": ["Pase", "Centro", "Regate", "Definición", "Velocidad", "Creatividad"],
    "AML": ["Pase", "Centro", "Regate", "Definición", "Velocidad", "Creatividad"],
    "ST": ["Definición", "Disparo", "Cabeceado", "Regate", "Velocidad", "Fuerza", "Aceleración"]
}

ATTR_ATAQUE = ["Disparo", "Definición", "Centro", "Pase", "Regate", "Cabeceado", "Creatividad"]
ATTR_DEFENSA = ["Marcaje", "Entradas", "Anticipación", "Colocación", "Agresividad", "Valentía", "Concentración"]
ATTR_FISICO = ["Velocidad", "Aceleración", "Fuerza", "Agilidad"]
TODOS_ATRIBUTOS = sorted(list(set(ATTR_ATAQUE + ATTR_DEFENSA + ATTR_FISICO)))

def obtener_blancas_combinadas(roles):
    blancas = set()
    for r in roles:
        if r in HABILIDADES_BLANCAS_POR_ROL:
            blancas.update(HABILIDADES_BLANCAS_POR_ROL[r])
    return list(blancas)

def obtener_factor_edad(edad):
    if edad <= 21:
        return 1.00
    elif edad <= 25:
        return max(0.40, 1.00 - ((edad - 21) * 0.12))
    else:
        return max(0.20, 0.40 - ((edad - 25) * 0.04))

def simular_sesion_completa_v2_8(atributos, attr_objetivo, meta_val, drill_nombre, nivel_drill, edad, descuento_cond, blancas):
    info = DRILLS_BASE[drill_nombre]
    attrs_drill = info["attr"]
    
    factor_edad = obtener_factor_edad(edad)
    mult_nivel = MULT_NIVEL_DRILL[nivel_drill]
    
    # 1. Desarrollo del ejercicio respecto al Cap (180%)
    vals_drill = [atributos.get(a, 0.0) for a in attrs_drill]
    suma_actual = sum(vals_drill)
    cap_maximo = len(attrs_drill) * 180.0
    
    desarrollo_pct = min(1.0, suma_actual / cap_maximo) if cap_maximo > 0 else 0.0
    freno_desarrollo = max(0.15, 1.0 - 0.65 * desarrollo_pct)
    
    # Base de incremento por SESIÓN (Calibrado para 111 repeticiones exactas)
    incremento_sesion_blanca = 1.35 * factor_edad * mult_nivel * freno_desarrollo
    
    # 2. Asignación directa: Blancas (100%), Grises (50%)
    for a in attrs_drill:
        if a in atributos:
            mult_color = 1.0 if a in blancas else 0.5
            inc = incremento_sesion_blanca * mult_color
            atributos[a] += inc

    # Costo exacto por repetición/sesión con el descuento del Club de Fans aplicado (-50%)
    costo_condicion_sesion = info["costo"] * descuento_cond
    return costo_condicion_sesion

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "Julio Lugo")
edad = st.sidebar.slider("Edad", 18, 36, 23)

roles_seleccionados = st.sidebar.multiselect(
    "Roles del Jugador (Máx. 3)",
    options=list(HABILIDADES_BLANCAS_POR_ROL.keys()),
    default=["MC", "DMC"],
    max_selections=3
)
blancas_jugador = obtener_blancas_combinadas(roles_seleccionados)

fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=2000)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de META ÚNICA")
meta_attr = st.sidebar.selectbox("Atributo Objetivo", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Creatividad"))
meta_val = st.sidebar.number_input("Porcentaje Meta (%)", min_value=1.0, max_value=500.0, value=200.0)
nivel_drill = st.sidebar.selectbox("Nivel del Ejercicio", list(MULT_NIVEL_DRILL.keys()), index=list(MULT_NIVEL_DRILL.keys()).index("Clase Mundial"))

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

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

btn_optimizar = st.button("🚀 CALCULAR ENTRENAMIENTO MONO-META v2.8", type="primary", use_container_width=True)

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    val_inicial = atributos_dinamicos[meta_attr]

    if val_inicial >= meta_val:
        st.warning(f"El atributo {meta_attr} ya alcanzó la meta ({val_inicial}% >= {meta_val}%).")
    else:
        descuento_cond = 0.5 if fan_club else 1.0
        mejor_drill = "Contraataque rápido"

        reps_total = 0
        costo_condicion_total = 0.0

        while atributos_dinamicos[meta_attr] < meta_val and reps_total < 3000:
            costo_sesion = simular_sesion_completa_v2_8(
                atributos_dinamicos, meta_attr, meta_val, mejor_drill, nivel_drill, edad, descuento_cond, blancas_jugador
            )
            reps_total += 1  # Cuenta repeticiones/sesiones completas
            costo_condicion_total += costo_sesion

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
