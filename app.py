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

def calcular_reps_reales(val_inicio, val_fin, mult_drill, factor_edad):
    val_curr = val_inicio
    reps_acumuladas = 0
    tramos = [
        (0.0, 100.0, 1.00),
        (100.0, 150.0, 0.55),
        (150.0, 200.0, 0.30),
        (200.0, 300.0, 0.12),
        (300.0, 500.0, 0.05)
    ]
    for t_min, t_max, mult_res in tramos:
        if val_curr >= val_fin:
            break
        if val_curr < t_max:
            tramo_fin = min(val_fin, t_max)
            delta = tramo_fin - val_curr
            ganancia_efectiva_rep = mult_drill * factor_edad * mult_res * 0.90
            reps_tramo = delta / ganancia_efectiva_rep
            reps_acumuladas += reps_tramo
            val_curr = tramo_fin
            
    return max(1, int(round(reps_acumuladas)))

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
    
    metas_raw = [
        {"attr": meta1_attr, "meta": meta1_val},
        {"attr": meta2_attr, "meta": meta2_val},
        {"attr": meta3_attr, "meta": meta3_val}
    ]
    
    metas = sorted(metas_raw, key=lambda x: x["meta"], reverse=True)

    descuento_cond = 0.5 if fan_club else 1.0
    factor_edad = max(0.35, 1.0 - (edad - 18) * 0.035)

    plan_rutinas = []
    costo_condicion_total = 0.0

    for m in metas:
        val_actual_dinamico = atributos_dinamicos[m["attr"]]
        
        if m["meta"] > val_actual_dinamico:
            drills_compatibles = {k: v for k, v in DRILLS_BASE.items() if m["attr"] in v["attr"]}
            if drills_compatibles:
                eval_m = []
                for name, info in drills_compatibles.items():
                    mult_int = MULT_INTENSIDAD.get(info["int"], 1.0)
                    costo_rep_cond = info["costo"] * descuento_cond
                    reps_req = calcular_reps_reales(val_actual_dinamico, m["meta"], mult_int, factor_edad)
                    costo_tot = reps_req * costo_rep_cond
                    eval_m.append({"nombre": name, "info": info, "reps": reps_req, "costo_total": costo_tot, "mult": mult_int})
                
                best_drill = sorted(eval_m, key=lambda x: x["costo_total"])[0]
                plan_rutinas.append({
                    "meta_attr": m["attr"], 
                    "target": m["meta"], 
                    "val_previo": val_actual_dinamico,
                    "drill": best_drill["nombre"], 
                    "reps": best_drill["reps"], 
                    "costo": best_drill["costo_total"]
                })
                costo_condicion_total += best_drill["costo_total"]

                delta_ganado = m["meta"] - val_actual_dinamico
                for attr_drill in best_drill["info"]["attr"]:
                    if attr_drill == m["attr"]:
                        atributos_dinamicos[attr_drill] = m["meta"]
                    elif attr_drill in atributos_dinamicos:  # PROTECCIÓN PARA EVITAR KeyError (e.g. "Puños")
                        atributos_dinamicos[attr_drill] += round(delta_ganado * 0.75, 1)

    packs_necesarios = round(costo_condicion_total / 15.0, 1)

    st.success(f"¡Plan Optimizado Mínimo Costo para *{nombre_jugador}*!")

    k1, k2, k3 = st.columns(3)
    k1.metric("Gasto Real Total Condición", f"-{round(costo_condicion_total, 1)}%")
    k2.metric("Maletines Verdes Necesarios", f"{packs_necesarios} Packs")
    k3.metric("Packs Restantes", f"{round(packs_disponibles - packs_necesarios, 1)}")

    st.markdown("---")
    st.subheader("📋 Circuito de Rutinas Eficiente (Sin Repeticiones Redundantes)")
    
    if not plan_rutinas:
        st.info("🎉 ¡Todos los atributos objetivo ya fueron alcanzados dinámicamente con los entrenamientos anteriores!")
    else:
        for plan in plan_rutinas:
            st.info(f"🎯 *Para {plan['meta_attr']} ({plan['target']}%): Ejecutar *{plan['drill']}* ➡️ *{plan['reps']} repeticiones** (Gasto: -{round(plan['costo'], 1)}% Condición)")

    st.markdown("---")
    st.subheader("📊 Pronóstico de la Ficha Técnica Final Proyectada")

    col_res_ataq, col_res_def, col_res_fis = st.columns(3)
    dict_metas_declaradas = {m["attr"]: m["meta"] for m in metas_raw}

    with col_res_ataq:
        st.markdown("#### ⚔️ Ataque")
        for attr in ATTR_ATAQUE:
            val_orig = valores_actuales[attr]
            val_final = atributos_dinamicos[attr]
            diff = round(val_final - val_orig, 1)
            
            if attr in dict_metas_declaradas:
                st.write(f"🎯 *{attr} (META)*: {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ *{attr} (Cascada)*: {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ *{attr}*: {val_orig}% (0.0%)")

    with col_res_def:
        st.markdown("#### 🛡️ Defensa")
        for attr in ATTR_DEFENSA:
            val_orig = valores_actuales[attr]
            val_final = atributos_dinamicos[attr]
            diff = round(val_final - val_orig, 1)
            
            if attr in dict_metas_declaradas:
                st.write(f"🎯 *{attr} (META)*: {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ *{attr} (Cascada)*: {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ *{attr}*: {val_orig}% (0.0%)")

    with col_res_fis:
        st.markdown("#### ⚡ Físico & Mental")
        for attr in ATTR_FISICO:
            val_orig = valores_actuales[attr]
            val_final = atributos_dinamicos[attr]
            diff = round(val_final - val_orig, 1)
            
            if attr in dict_metas_declaradas:
                st.write(f"🎯 *{attr} (META)*: {val_final}% (🟢 +{diff}%)")
            elif diff > 0:
                st.write(f"⚡ *{attr} (Cascada)*: {val_final}% (🟢 +{diff}%)")
            else:
                st.write(f"⚪ *{attr}*: {val_orig}% (0.0%)")