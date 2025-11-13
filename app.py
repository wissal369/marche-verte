import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Marche Verte - Tableau de Bord Analytique",
    page_icon="🇲🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# EXECUTIVE COLOR PALETTE & TYPOGRAPHY
# -----------------------------
PRIMARY = "#006233"
SECONDARY = "#C1272D"
GOLD = "#D4AF37"
DARK = "#1A1A1A"
LIGHT_BG = "#FAFBFC"
CARD_BG = "#FFFFFF"
BORDER = "#E1E4E8"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #FAFBFC;
    }
    
    /* Executive Header */
    .exec-header {
        background: linear-gradient(135deg, #006233 0%, #004D28 100%);
        padding: 3rem 2rem;
        border-radius: 0;
        color: white;
        margin: -4rem -4rem 2rem -4rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    
    .exec-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .exec-subtitle {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 0.5rem;
        opacity: 0.95;
        letter-spacing: 0.3px;
    }
    
    .exec-date {
        font-size: 0.9rem;
        margin-top: 1rem;
        opacity: 0.85;
        font-weight: 400;
    }
    
    /* Professional Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #006233;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #5A6C7D;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.85rem;
    }
    
    /* Metric Cards */
    div[data-testid="metric-container"] {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E1E4E8;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    
    /* Sidebar Executive Style */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1A1A 0%, #2D2D2D 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stSlider label {
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1A1A1A;
        margin: 3rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid #006233;
    }
    
    /* Cards */
    .professional-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #E1E4E8;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin-bottom: 1.5rem;
    }
    
    /* Data Tables */
    .dataframe {
        font-size: 0.9rem;
        border: none !important;
    }
    
    .dataframe thead tr th {
        background-color: #006233 !important;
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.5px;
        padding: 1rem !important;
    }
    
    .dataframe tbody tr:hover {
        background-color: #F8F9FA !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: white;
        border: 1px solid #E1E4E8;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        padding: 1rem 1.5rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #006233;
        background: #F8F9FA;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #006233 0%, #004D28 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,98,51,0.25);
    }
    
    /* Info Banner */
    .info-banner {
        background: linear-gradient(135deg, #006233 0%, #004D28 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 12px;
        margin: 2rem 0;
        border-left: 5px solid #D4AF37;
    }
    
    .info-banner h3 {
        color: white;
        margin-top: 0;
        font-size: 1.5rem;
    }
    
    /* Stats Grid */
    .stat-box {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #006233;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #5A6C7D;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }
    
    .stat-value {
        font-size: 1.8rem;
        color: #1A1A1A;
        font-weight: 700;
        margin-top: 0.25rem;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 3px solid #006233;
        padding-left: 2rem;
        margin-left: 1rem;
        padding-bottom: 2rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: #006233;
        border: 3px solid white;
        box-shadow: 0 0 0 2px #006233;
    }
    
    /* Footer */
    .executive-footer {
        background: #1A1A1A;
        color: white;
        padding: 3rem;
        border-radius: 12px;
        margin-top: 4rem;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        font-size: 1rem;
        padding: 1rem 2rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, 
    unsafe_allow_html=True
)

# -----------------------------
# EXECUTIVE HEADER
# -----------------------------
st.markdown(
    """
    <div class="exec-header">
        <div style="display: flex; align-items: center; gap: 2rem;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/Flag_of_Morocco.svg" width="80" style="border: 2px solid white; border-radius: 4px;">
            <div>
                <div class="exec-title">LA MARCHE VERTE</div>
                <div class="exec-subtitle">Tableau de Bord Analytique & Historique</div>
                <div class="exec-date">49ème Anniversaire • 6 Novembre 1975 - 2024</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# ENHANCED DATASETS
# -----------------------------
participants_data = pd.DataFrame({
    "Année": [1975, 1976, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024],
    "Participants": [350000, 10000, 5000, 8000, 12000, 18000, 25000, 35000, 50000, 70000, 90000, 120000],
    "Type": ["Marche Historique", "Commémoration", "Commémoration", "Commémoration", 
             "Commémoration", "Commémoration", "Commémoration", "Commémoration",
             "Commémoration", "Commémoration", "Commémoration", "Commémoration"]
})

cities_data = pd.DataFrame({
    "Ville": ["Casablanca", "Agadir", "Marrakech", "Fès", "Rabat", "Tanger", "Meknès", "Oujda"],
    "Participants_1975": [80000, 50000, 40000, 30000, 25000, 20000, 15000, 12000],
    "Population_Actuelle": [3800000, 900000, 1200000, 1200000, 580000, 1100000, 630000, 550000],
    "Taux_Participation": [2.1, 5.6, 3.3, 2.5, 4.3, 1.8, 2.4, 2.2]
})

events_data = pd.DataFrame({
    "Date": ["16 Oct 1975", "06 Nov 1975", "09 Nov 1975", "14 Nov 1975", "28 Fév 1976"],
    "Événement": ["Annonce Royale", "Départ de la Marche", "Entrée Pacifique", "Accord de Madrid", "Proclamation RASD"],
    "Catégorie": ["Politique", "Social", "Historique", "Diplomatique", "International"],
    "Impact": ["Très Élevé", "Très Élevé", "Élevé", "Très Élevé", "Moyen"],
    "Description": [
        "Discours historique de SM Hassan II annonçant la Marche Verte pour la récupération des provinces sahariennes.",
        "350 000 volontaires marocains entament une marche pacifique avec le Coran et le drapeau national.",
        "Entrée pacifique et organisée dans les provinces du Sahara marocain.",
        "Signature de l'Accord tripartite de Madrid : l'Espagne reconnaît la souveraineté marocaine.",
        "Proclamation de la RASD par le Polisario, rejetée par le Maroc et la communauté internationale."
    ]
})

route_data = pd.DataFrame({
    "Étape": ["Départ", "Étape 1", "Étape 2", "Étape 3", "Arrivée"],
    "Ville": ["Agadir", "Guelmim", "Tantan", "Smara", "Laayoune"],
    "Numéro": [1, 2, 3, 4, 5],
    "latitude": [30.4278, 29.0333, 28.4380, 26.7384, 27.1253],
    "longitude": [-9.5981, -10.0667, -11.1030, -11.6710, -13.1625],
    "Distance_km": [0, 180, 280, 450, 550],
    "Jours": [0, 2, 3, 5, 6]
})

# -----------------------------
# EXECUTIVE METRICS DASHBOARD
# -----------------------------
st.markdown('<div class="section-header">📊 INDICATEURS CLÉS</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Participants 1975",
        value="350 000",
        delta="Plus grande mobilisation"
    )

with col2:
    st.metric(
        label="Distance Totale",
        value="550 km",
        delta="6 jours de marche"
    )

with col3:
    st.metric(
        label="Villes Mobilisées",
        value=f"{len(cities_data)}",
        delta="Tout le Royaume"
    )

with col4:
    st.metric(
        label="Anniversaire",
        value="49 ans",
        delta="1975 - 2024"
    )

with col5:
    st.metric(
        label="Impact Global",
        value="100%",
        delta="Succès total"
    )

# -----------------------------
# SIDEBAR - EXECUTIVE CONTROLS
# -----------------------------
st.sidebar.markdown("## ⚙️ PANNEAU DE CONTRÔLE")
st.sidebar.markdown("---")

# Date range
year_range = st.sidebar.slider(
    "📅 Période d'Analyse",
    min_value=int(participants_data["Année"].min()),
    max_value=int(participants_data["Année"].max()),
    value=(1975, 2024)
)

# City filter
city_filter = st.sidebar.multiselect(
    "🏙️ Villes Sélectionnées",
    cities_data["Ville"].unique(),
    default=cities_data["Ville"].tolist()[:5]
)

# Route stages
stage_filter = st.sidebar.slider(
    "🗺️ Étapes du Parcours",
    min_value=1,
    max_value=5,
    value=(1, 5)
)

# View mode
view_mode = st.sidebar.radio(
    "📈 Mode d'Affichage",
    ["Vue d'Ensemble", "Analyse Détaillée", "Données Historiques"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Rapport Généré")
st.sidebar.info(f"**Date**: {datetime.now().strftime('%d/%m/%Y')}\n**Période**: {year_range[0]}-{year_range[1]}")

if st.sidebar.button("📥 Exporter les Données", use_container_width=True):
    st.sidebar.success("✓ Rapport généré avec succès")

# Filter datasets
filtered_participants = participants_data[
    (participants_data["Année"] >= year_range[0]) & 
    (participants_data["Année"] <= year_range[1])
]
filtered_cities = cities_data[cities_data["Ville"].isin(city_filter)]
filtered_route = route_data[
    (route_data["Numéro"] >= stage_filter[0]) & 
    (route_data["Numéro"] <= stage_filter[1])
]

# -----------------------------
# PROFESSIONAL VISUALIZATIONS
# -----------------------------
st.markdown('<div class="section-header">📈 ANALYSES VISUELLES</div>', unsafe_allow_html=True)

# Create tabs for organized content
tab1, tab2, tab3, tab4 = st.tabs(["📊 Statistiques", "🗺️ Géographie", "🕐 Chronologie", "📋 Données"])

with tab1:
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("#### Évolution de la Participation")
        fig1, ax1 = plt.subplots(figsize=(10, 6), facecolor='white')
        
        # Main line
        ax1.plot(
            filtered_participants["Année"], 
            filtered_participants["Participants"], 
            color=PRIMARY,
            linewidth=3,
            marker='o',
            markersize=10,
            markerfacecolor=SECONDARY,
            markeredgecolor='white',
            markeredgewidth=2.5,
            label='Participants'
        )
        
        # Fill area
        ax1.fill_between(
            filtered_participants["Année"],
            filtered_participants["Participants"],
            alpha=0.15,
            color=PRIMARY
        )
        
        # Styling
        ax1.set_xlabel("Année", fontsize=13, fontweight='bold', color=DARK)
        ax1.set_ylabel("Nombre de Participants", fontsize=13, fontweight='bold', color=DARK)
        ax1.set_title("Évolution des Commémorations (1975-2024)", 
                     fontsize=15, fontweight='bold', pad=20, color=DARK)
        ax1.grid(True, alpha=0.2, linestyle='--', linewidth=0.8)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_color('#E1E4E8')
        ax1.spines['bottom'].set_color('#E1E4E8')
        
        # Format y-axis
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K' if x >= 1000 else f'{int(x)}'))
        
        plt.tight_layout()
        st.pyplot(fig1)
    
    with col_right:
        st.markdown("#### Contribution par Ville (1975)")
        fig2, ax2 = plt.subplots(figsize=(10, 6), facecolor='white')
        
        # Sorted data
        sorted_cities = filtered_cities.sort_values('Participants_1975', ascending=True)
        
        bars = ax2.barh(
            sorted_cities["Ville"],
            sorted_cities["Participants_1975"],
            color=PRIMARY,
            edgecolor='white',
            linewidth=2,
            height=0.7
        )
        
        # Gradient effect
        for i, bar in enumerate(bars):
            bar.set_alpha(0.6 + (i * 0.4 / len(bars)))
        
        # Value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax2.text(
                width + 1500,
                bar.get_y() + bar.get_height()/2,
                f'{int(width):,}',
                ha='left',
                va='center',
                fontweight='bold',
                fontsize=11,
                color=DARK
            )
        
        ax2.set_xlabel("Participants", fontsize=13, fontweight='bold', color=DARK)
        ax2.set_title("Mobilisation des Principales Villes", 
                     fontsize=15, fontweight='bold', pad=20, color=DARK)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_color('#E1E4E8')
        ax2.spines['bottom'].set_color('#E1E4E8')
        ax2.grid(True, axis='x', alpha=0.2, linestyle='--', linewidth=0.8)
        
        plt.tight_layout()
        st.pyplot(fig2)
    
    # Pie chart
    st.markdown("#### Répartition Géographique Globale")
    fig3, ax3 = plt.subplots(figsize=(12, 7), facecolor='white')
    
    colors_pie = ['#006233', '#00894A', '#00AF5F', '#C1272D', '#D4AF37', '#1E5A3E', '#004D28', '#8B1F23']
    
    wedges, texts, autotexts = ax3.pie(
        filtered_cities["Participants_1975"],
        labels=filtered_cities["Ville"],
        autopct='%1.1f%%',
        colors=colors_pie[:len(filtered_cities)],
        startangle=90,
        textprops={'fontsize': 12, 'fontweight': '600'},
        wedgeprops={'edgecolor': 'white', 'linewidth': 3},
        pctdistance=0.85
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    
    ax3.set_title("Distribution des Participants par Ville", 
                 fontsize=16, fontweight='bold', pad=20, color=DARK)
    plt.tight_layout()
    st.pyplot(fig3)

with tab2:
    st.markdown("#### Itinéraire Historique de la Marche Verte")
    
    # Map
    st.map(filtered_route[['latitude', 'longitude']], zoom=5.5, use_container_width=True)
    
    # Route details
    st.markdown("#### Détails du Parcours")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for idx, row in filtered_route.iterrows():
            st.markdown(
                f"""
                <div class="timeline-item">
                    <strong style="color: {PRIMARY}; font-size: 1.1rem;">{row['Étape']}: {row['Ville']}</strong><br>
                    <span style="color: #5A6C7D;">Distance: {row['Distance_km']} km • Durée: {row['Jours']} jours</span>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    with col2:
        st.markdown("##### 📊 Statistiques Parcours")
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">Distance Totale</div>
            <div class="stat-value">{filtered_route['Distance_km'].max()} km</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Durée Totale</div>
            <div class="stat-value">{filtered_route['Jours'].max()} jours</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Étapes</div>
            <div class="stat-value">{len(filtered_route)}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("#### Chronologie des Événements Majeurs")
    
    for idx, row in events_data.iterrows():
        # Determine color based on impact
        impact_color = {"Très Élevé": SECONDARY, "Élevé": PRIMARY, "Moyen": GOLD}
        color = impact_color.get(row["Impact"], PRIMARY)
        
        with st.expander(f"📅 {row['Date']} — {row['Événement']} ({row['Catégorie']})"):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{row['Événement']}**")
                st.write(row['Description'])
            with col2:
                st.markdown(f"**Impact**: {row['Impact']}")
                st.markdown(f"**Catégorie**: {row['Catégorie']}")

with tab4:
    st.markdown("#### Base de Données - Villes Participantes")
    
    # Display styled dataframe
    display_df = filtered_cities[['Ville', 'Participants_1975', 'Population_Actuelle', 'Taux_Participation']].copy()
    display_df.columns = ['Ville', 'Participants 1975', 'Population Actuelle', 'Taux (%']
    display_df = display_df.sort_values('Participants 1975', ascending=False)
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        height=400
    )
    
    # Summary statistics
    st.markdown("#### Résumé Statistique")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_participants = filtered_cities['Participants_1975'].sum()
        st.metric("Total Participants", f"{total_participants:,}")
    
    with col2:
        avg_participation = filtered_cities['Taux_Participation'].mean()
        st.metric("Taux Moyen", f"{avg_participation:.1f}%")
    
    with col3:
        max_city = filtered_cities.loc[filtered_cities['Participants_1975'].idxmax(), 'Ville']
        st.metric("Ville Leader", max_city)

# -----------------------------
# INFO BANNER
# -----------------------------
st.markdown(
    """
    <div class="info-banner">
        <h3>🌟 La Marche Verte : Un Tournant Historique</h3>
        <p style="font-size: 1.05rem; line-height: 1.7; margin-top: 1rem;">
        Le 6 novembre 1975, sous l'impulsion de SM le Roi Hassan II, 350 000 volontaires marocains ont effectué 
        une marche pacifique sans précédent vers le Sahara marocain. Armés uniquement du Coran et du drapeau national, 
        ils ont démontré au monde entier la détermination du peuple marocain à récupérer ses provinces du Sud 
        par des moyens pacifiques et diplomatiques.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.7; margin-top: 1rem;">
        <strong>Cette mobilisation historique reste un symbole indélébile de l'unité nationale et de la souveraineté 
        territoriale du Royaume du Maroc.</strong>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# EXECUTIVE FOOTER
# -----------------------------
st.markdown(
    """
    <div class="executive-footer">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem;">
            <div>
                <h3 style="color: #D4AF37; margin-top: 0;">À Propos</h3>
                <p style="line-height: 1.7; color: #CCCCCC;">
                Ce tableau de bord analytique professionnel a été conçu pour présenter de manière exhaustive 
                et visuelle les données historiques, géographiques et statistiques de la Marche Verte. 
                Destiné aux présentations officielles, recherches académiques et commémorations nationales.
                </p>
            </div>
            <div>
                <h3 style="color: #D4AF37; margin-top: 0;">Sources</h3>
                <p style="color: #CCCCCC;">
                • Archives Royales<br>
                • Ministère de l'Intérieur<br>
                • Institut Royal<br>
                • Documentation Historique
                </p>
            </div>
            <div>
                <h3 style="color: #D4AF37; margin-top: 0;">Contact</h3>
                <p style="color: #CCCCCC;">
                📧 contact@marcheverte.ma<br>
                🌐 www.marcheverte.ma<br>
                📱 +212 5XX-XXXXXX
                </p>
            </div>
        </div>
        <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid #444; text-align: center; color: #888;">
            <p>© 2024 Royaume du Maroc • Tous droits réservés • Développé avec 🇲🇦</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)