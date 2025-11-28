#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:12:44 2025

@author: ryles
"""

import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="AI for Impact – Cataract Detection",
    layout="centered",
    initial_sidebar_state="auto"
)

# Chargement du logo
logo = Image.open('assets/efrei_logo.png')  # Assure-toi que l'image est dans assets/

# Style personnalisé clair
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    h1, h2, h3 {
        color: #003366;
        text-align: center;
    }
    .team-member {
        text-align: center;
        font-size: 20px;
    }
    /* Modifie la couleur de la barre supérieure */
    header {
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)


# Logo EFREI
st.image(logo, width=150)

# En-tête
st.markdown("<div class='intro-box'>", unsafe_allow_html=True)
st.markdown("## 🧠 AI for Impact – Détection de la Cataracte")
st.markdown("### Hackathon EFREI 2025")
st.markdown("""
Bienvenue sur notre projet de hackathon visant à développer une solution de détection automatique de la cataracte à partir d’images ophtalmiques.  
Nous combinons Deep Learning, Analyse de données et Visualisation interactive pour avoir un impact concret dans le domaine médical.
<br><br>
La cataracte est une des principales causes de cécité dans le monde. Le diagnostic rapide et précis de la cataracte est crucial pour 
la gestion et le traitement.
<br><br>
Cependant, les méthodes traditionnelles peuvent être lentes, coûteuses et dépendent d'experts médicaux.
Ce projet vise à automatiser le diagnostic à l'aide de l'intelligence artificielle pour une détection précoce et précise.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Membres de l'équipe
st.markdown("### 👨‍💻 Équipe")
cols = st.columns(4)
for col, name in zip(cols, ["Bilal", "Ryles", "Bacar", "Patience"]):
    col.markdown(f"<div class='team-member'>{name}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center;'>Projet réalisé dans le cadre du Hackathon 2025 – EFREI Paris</div>", unsafe_allow_html=True)
