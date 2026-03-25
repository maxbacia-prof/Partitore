import streamlit as st

st.set_page_config(page_title="Partitore", page_icon="📉")


# Funzione per la virgola italiana
def ita(valore, dec=2):
    return f"{valore:.{dec}f}".replace('.', ',')


st.title("📉 Calcolatore Partitore di Tensione")

col1, col2 = st.columns([2, 1])

with col1:
    vin = st.number_input("Vin [V]", min_value=0.0, value=12.0, step=0.1)
    r1 = st.number_input("R1 (Alto) [Ω]", min_value=0.1, value=1000.0)
    r2 = st.number_input("R2 (Basso) [Ω]", min_value=0.1, value=1000.0)

    # Calcoli
    vout = vin * (r2 / (r1 + r2))
    v_r1 = vin - vout

with col2:
    st.subheader("Risultato")
    st.latex(r"V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}")
    st.header(f"{ita(vout)} V")

st.divider()

# DISEGNO DEL CIRCUITO (Versione semplificata e robusta)
st.subheader("Schema del Circuito")

# Costruiamo la stringa SVG pezzo per pezzo per evitare errori di f-string
svg_code = f"""
<div style="display: flex; justify-content: center; background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
    <svg width="300" height="260" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg">
        <line x1="150" y1="20" x2="150" y2="50" stroke="black" stroke-width="2"/>
        <line x1="150" y1="110" x2="150" y2="140" stroke="black" stroke-width="2"/>
        <line x1="150" y1="200" x2="150" y2="230" stroke="black" stroke-width="2"/>
        <line x1="150" y1="125" x2="220" y2="125" stroke="black" stroke-width="2"/>
        <rect x="135" y="50" width="30" height="60" fill="none" stroke="black" stroke-width="2"/>
        <text x="100" y="85" font-family="Arial" font-weight="bold">R1</text>
        <rect x="135" y="140" width="30" height="60" fill="none" stroke="black" stroke-width="2"/>
        <text x="100" y="175" font-family="Arial" font-weight="bold">R2</text>
        <text x="150" y="15" font-family="Arial" font-weight="bold" fill="blue" text-anchor="middle">Vin: {ita(vin, 1)}V</text>
        <circle cx="225" cy="125" r="5" fill="red"/>
        <text x="235" y="130" font-family="Arial" font-weight="bold" fill="red">Vout: {ita(vout)}V</text>
        <line x1="130" y1="230" x2="170" y2="230" stroke="black" stroke-width="2"/>
        <line x1="140" y1="235" x2="160" y2="235" stroke="black" stroke-width="2"/>
    </svg>
</div>
"""

# QUESTA È LA RIGA FONDAMENTALE:
st.markdown(svg_code, unsafe_allow_html=True)

st.info(f"💡 Caduta su R1: {ita(v_r1, 1)}V")