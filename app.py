import streamlit as st

st.set_page_config(
    page_title="Optimizador Mono-Meta - Top Eleven",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Optimizador de Precisión (Mono-Meta) - Top Eleven")
st.caption("Especializado en llevar un atributo individual a su objetivo exacto con precisión matemática superior.")

DRILLS_BASE = {
    # ATAQUE
    "Remate 1 contra 1": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Definición", "Regate", "Aceleración"]},
    "¡Pasa y dispara!": {"cat": "Ataque", "int": "Fácil", "costo": 6.0, "attr": ["Disparo", "Pase", "Velocidad"]},
    "Jugadas balón parado": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Disparo", "Centro", "Cabeceado"]},
    "Técnica de disparo": {"cat": "Ataque", "int": "Medio", "costo": 7.5, "attr": ["Definición", "Disparo", "Agilidad"]},
    "Driblar en slalom": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Regate", "Pase", "Velocidad"]},
    "Jugar en las bandas": {"cat": "Ataque", "int": "Difícil", "costo": 9.0, "attr": ["Centro", "Definición", "Disparo", "Cabeceado"]},
    "Contraataque rápido": {"cat": "Ataque", "int": "Muy Difícil", "costo": 10.5, "attr": ["Pase", "Creatividad", "Centro", "Disparo"]},

    # DEFENSA
    "Análisis de vídeos": {"cat": "Defensa", "int": "Muy Fácil", "costo": 4.5, "attr": ["Colocación", "Creatividad", "Valentía"]},
    "Usa la cabeza": {"cat": "Defensa", "int": "Fácil", "costo": 6.0, "attr": ["Colocación", "Pase", "Cabeceado", "Creatividad"]},
    "Mantener la línea": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Colocación", "Concentración"]},
    "Parar al atacante": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Entradas", "Regate", "Valentía", "Fuerza"]},
    "Defender los centros": {"cat": "Defensa", "int": "Medio", "costo": 7.5, "attr": ["Marcaje", "Cabeceado", "Centro", "Valentía"]},
    "Juego de presión": {"cat": "Defensa", "int": "Difícil", "costo": 9.0, "attr": ["Marcaje", "Entradas", "Agresividad", "Colocación", "Valentía"]},

    # POSESIÓN
    "Control del balón": {"cat": "Posesión", "int": "Muy Fácil", "costo": 4.5, "attr": ["Regate", "Creatividad", "Concentración", "Cabeceado"]},
    "Balón prisionero": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Pase", "Entradas", "Agresividad", "Colocación"]},
    "Primer toque": {"cat": "Posesión", "int": "Fácil", "costo": 6.0, "attr": ["Pase", "Regate"]},
    "Cambio de banda rápido": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Pase", "Centro", "Creatividad", "Velocidad", "Colocación"]},
    "Mantenerse en carril": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Velocidad", "Colocación"]},
    "Juego de contacto": {"cat": "Posesión", "int": "Medio", "costo": 7.5, "attr": ["Regate", "Fuerza", "Marcaje", "Agresividad", "Valentía"]},
    "Pases antes de disparo": {"cat": "Posesión", "int": "Difícil", "costo": 9.0, "attr": ["Pase", "Definición", "Creatividad", "Colocación", "Anticipación"]},

    # FÍSICO Y MENTAL
    "Calentamiento": {"cat": "Físico y Mental", "int": "Muy Fácil", "costo": 4.5, "attr": ["Agresividad", "Cabeceado"]},
    "Estiramientos": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Agilidad", "Velocidad", "Fuerza"]},
    "Carioca con escalera": {"cat": "Físico y Mental", "int": "Fácil", "costo": 6.0, "attr": ["Agilidad", "Velocidad", "Concentración", "Agresividad"]},
    "Carrera larga": {"cat": "Físico y Mental", "int": "Medio", "costo": 7.5, "attr": ["Velocidad", "Concentración"]},
    "Carreras cortas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Velocidad", "Agilidad", "Fuerza", "Valentía"]},
    "Saltos de vallas": {"cat": "Físico y Mental", "int": "Difícil", "costo": 9.0, "attr": ["Velocidad", "Valentía", "Agresividad"]},
    "Gimnasio": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Fuerza"]},
    "Sprints": {"cat": "Físico y Mental", "int": "Muy Difícil", "costo": 10.5, "attr": ["Velocidad", "Aceleración", "Regate"]}
}

ATTR_ATAQUE = ["Disparo", "Definición", "Centro", "Pase", "Regate", "Cabeceado", "Creatividad"]
ATTR_DEFENSA = ["Marcaje", "Entradas", "Anticipación", "Colocación", "Agresividad", "Valentía", "Concentración"]
ATTR_FISICO = ["Velocidad", "Aceleración", "Fuerza", "Agilidad"]

TODOS_ATRIBUTOS = sorted(list(set(ATTR_ATAQUE + ATTR_DEFENSA + ATTR_FISICO)))

def obtener_factor_edad(edad):
    # Coeficiente dinámico de rendimiento por edad
    if edad <= 18:
        return 1.15
    elif edad <= 21:
        return 1.00
    elif edad <= 24:
        return 0.88
    elif edad <= 27:
        return 0.75
    else:
        return 0.60

def simular_repeticion_dinamica(atributos, attr_objetivo, meta_val, drill_nombre, factor_edad, descuento_cond):
    info = DRILLS_BASE[drill_nombre]
    attrs_drill = info["attr"]
    
    # 1. Calcular el Promedio Actual del Ejercicio (Drill Average)
    valores_ejercicio = [atributos[a] for a in attrs_drill if a in atributos]
    promedio_ejercicio = sum(valores_ejercicio) / len(valores_ejercicio)
    
    # 2. Factor de Frenado Dinámico basado en el promedio global del ejercicio
    # Cuanto mayor es el promedio del ejercicio, menor es la ganancia global por repetición
    eficiencia = max(0.08, 1.85 - (promedio_ejercicio / 100.0))
    
    # 3. Ganancia base por repetición (Set completo de 6 slots)
    ganancia_base = 0.72 * factor_edad * eficiencia
    
    # 4. Distribución en los atributos del ejercicio
    for a in attrs_drill:
        if a in atributos:
            val_act = atributos[a]
            # Soft-cap individual: si una habilidad supera los 180%, su absorción baja y se distribuye al resto
            factor_individual = 1.0 if val_act < 180.0 else (0.5 if val_act < 250.0 else 0.25)
            
            incremento = ganancia_base * factor_individual
            atributos[a] += incremento
            
    # Garantizar que el atributo objetivo no sobrepase visualmente la meta si así lo prefieres
    if atributos[attr_objetivo] > meta_val:
        atributos[attr_objetivo] = meta_val

    costo_condicion = info["costo"] * descuento_cond
    return costo_condicion

# SIDEBAR
st.sidebar.header("👤 Perfil del Jugador")
nombre_jugador = st.sidebar.text_input("Nombre", "Julio Lugo")
edad = st.sidebar.slider("Edad", 18, 36, 23)
fan_club = st.sidebar.checkbox("Descuento Club de Fans (-50%)", value=True)
packs_disponibles = st.sidebar.number_input("Green Packs en cuenta", min_value=0, max_value=5000, value=2000)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Configuración de META ÚNICA")

meta_attr = st.sidebar.selectbox("Atributo Objetivo", TODOS_ATRIBUTOS, index=TODOS_ATRIBUTOS.index("Creatividad"))
meta_val = st.sidebar.number_input("Porcentaje Meta (%)", min_value=1.0, max_value=500.0, value=200.0)

# PANEL CENTRAL
st.subheader("📋 Porcentajes Actuales del Jugador (%)")

c_at, c_de, c_fi = st.columns(3)
valores_actuales = {}

# Carga de valores por defecto idénticos a tus capturas
def_defaults = {
    "Pase": 246.0, "Creatividad": 131.0, "Centro": 92.0, "Disparo": 151.0, "Definición": 53.0,
    "Regate": 217.0, "Cabeceado": 183.0, "Marcaje": 221.0, "Entradas": 210.0, "Colocación": 192.0,
    "Valentía": 209.0, "Velocidad": 161.0, "Fuerza": 102.0
}

with c_at:
    st.markdown("### ⚔️ Ataque")
    for attr in ATTR_ATAQUE:
        default = def_defaults.get(attr, 80.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=default, key=attr)

with c_de:
    st.markdown("### 🛡️ Defensa")
    for attr in ATTR_DEFENSA:
        default = def_defaults.get(attr, 75.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=default, key=attr)

with c_fi:
    st.markdown("### ⚡ Físico & Mental")
    for attr in ATTR_FISICO:
        default = def_defaults.get(attr, 85.0)
        valores_actuales[attr] = st.number_input(f"{attr}", min_value=1.0, max_value=500.0, value=default, key=attr)

st.markdown("---")

btn_optimizar = st.button("🚀 CALCULAR ENTRENAMIENTO MONO-META", type="primary", use_container_width=True)

if btn_optimizar:
    atributos_dinamicos = valores_actuales.copy()
    val_inicial = atributos_dinamicos[meta_attr]

    if val_inicial >= meta_val:
        st.warning(f"El atributo {meta_attr} ya alcanzó o superó la meta ({val_inicial}% >= {meta_val}%).")
    else:
        descuento_cond = 0.5 if fan_club else 1.0
        factor_edad = obtener_factor_edad(edad)

        drills_principales = [k for k, v in DRILLS_BASE.items() if meta_attr in v["attr"]]
        mejor_drill = drills_principales[0] if drills_principales else "Contraataque rápido"

        reps_total = 0
        costo_condicion_total = 0.0

        while atributos_dinamicos[meta_attr] < meta_val and reps_total < 3000:
            costo_rep = simular_repeticion_dinamica(
                atributos_dinamicos, meta_attr, meta_val, mejor_drill, factor_edad, descuento_cond
            )
            reps_total += 1
            costo_condicion_total += costo_rep

        packs_necesarios = round(costo_condicion_total / 15.0, 1)

        st.success(f"¡Plan Mono-Meta Finalizado para {nombre_jugador}!")

        k1, k2, k3 = st.columns(3)
        k1.metric("Gasto Total Condición", f"-{round(costo_condicion_total, 1)}%")
        k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
        k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

        st.markdown("---")
        st.subheader("📋 Rutina Seleccionada")
        st.info(f"🎯 Ejercicio Recomendado: *{mejor_drill}* ➡️ *{reps_total} repeticiones* (Gasto: -{round(costo_condicion_total, 1)}% Condición)")
