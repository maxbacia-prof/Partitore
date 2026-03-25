import streamlit as st

st.set_page_config(page_title="Partitore di Tensione", page_icon="📉")

st.title("📉 Calcolatore Partitore di Tensione")
st.write("Calcola la tensione in uscita (Vout) tra due resistenze in serie.")


# Funzione virgola italiana
def ita(valore, dec=2):
    return f"{valore:.{dec}f}".replace('.', ',')


col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Dati del Circuito")
    vin = st.number_input("Tensione Ingresso (Vin) [V]", min_value=0.0, value=12.0, step=0.1)
    r1 = st.number_input("Resistenza R1 (Alto) [Ω]", min_value=0.1, value=1000.0, step=1.0)
    r2 = st.number_input("Resistenza R2 (Basso) [Ω]", min_value=0.1, value=1000.0, step=1.0)

    # Calcolo
    vout = vin * (r2 / (r1 + r2))
    v_r1 = vin - vout

with col2:
    st.subheader("Risultato")
    st.latex(r"V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}")
    st.header(f"{ita(vout)} V")

st.divider()

# --- Rappresentazione Grafica del Circuito ---
st.subheader("Schema del Circuito")

html_partitore = f"""
<div style="display: flex; justify-content: center; background-color: white; padding: 20px; border-radius: 10px;">
    <svg width="300" height="250" viewBox="0 0 300 250">
        <line x1="150" y1="10" x2="150" y2="40" stroke="black" stroke-width="2"/>
        <line x1="150" y1="100" x2="150" y2="130" stroke="black" stroke-width="2"/>
        <line x1="150" y1="190" x2="150" y2="220" stroke="black" stroke-width="2"/>
        <line x1="150" y1="115" x2="220" y2="115" stroke="black" stroke-width="2"/>

        <rect x="135" y="40" width="30" height="60" fill="white" stroke="black" stroke-width="2"/>
        <text x="110" y="75" font-family="Arial" font-weight="bold">R1</text>
        <text x="180" y="75" font-family="Arial" font-size="12">{ita(r1, 0)} Ω</text>

        <rect x="135" y="130" width="30" height="60" fill="white" stroke="black" stroke-width="2"/>
        <text x="110" y="165" font-family="Arial" font-weight="bold">R2</text>
        <text x="180" y="165" font-family="Arial" font-size="12">{ita(r2, 0)} Ω</text>

        <text x="135" y="10" font-family="Arial" font-weight="bold" fill="blue">Vin: {ita(vin, 1)}V</text>
        <circle cx="225" cy="115" r="4" fill="red"/>
        <text x="235" y="120" font-family="Arial" font-weight="bold" fill="red">Vout: {ita(vout)}V</text>

        <line x1="130" y1="220" x2="170" y2="220" stroke="black" stroke-width="2"/>
        <line x1="135" y1="225" x2="165" y2="225" stroke="black" stroke-width="2"/>
        <line x1="140" y1="230" x2="160" y2="230" stroke="black" stroke-width="2"/>
    </svg>
</div>
"""
st.markdown(html_partitore, unsafe_allow_html=True)

st.info(f"💡 La resistenza R1 sta dissipando {ita(v_r1, 1)}V, mentre R2 fornisce la tensione desiderata.")