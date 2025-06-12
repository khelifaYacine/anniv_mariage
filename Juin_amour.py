import streamlit as st

st.set_page_config(page_title="Escape Game de Notre Amour", layout="wide")

# Initialisation de l'état
if "step" not in st.session_state:
    st.session_state.step = 1
if "validated" not in st.session_state:
    st.session_state.validated = False

# Fonction d'affichage stylisé
def show_message(title, content, bg_color="#FFEBF0", text_color="#CC0066", border_color="#FF3399"):
    st.markdown(f"""
        <div style='background-color:{bg_color};padding:20px;border-radius:10px;
        border:3px solid {border_color};text-align:center;'>
            <h3 style='color:{text_color};'>{title}</h3>
            <p style='font-size:20px;color:black;'>{content}</p>
        </div>
    """, unsafe_allow_html=True)

# Fonction de succès
def show_success(message):
    show_message("🎉 Bravo mon amour !", message, "#D1FFD6", "#32A852", "#32A852")

# Définition des étapes
steps = {
    1: {"riddle": "🔍 **Trouve le chiffre du jour le plus précieux de notre vie**", "answer": "18", "success": "💖 Le **18**, notre jour inoubliable.", "next": "🛏️ **Va dans notre chambre et cherche dans la table de nuit**"},
    2: {"riddle": "🗝️ **Code trouvé dans la table de nuit ?**", "answer": "amour", "success": "💌 **Notre amour**, résumé en un seul mot.", "next": "🚪 **Va voir sous l’armoire du salon**"},
    3: {"riddle": "📦 **Code sous l’armoire ?**", "answer": "rose", "success": "📸 **Rose**, le lien entre toutes nos aventures.", "next": "📖 **Cherche dans l’album photo**"},
    4: {"riddle": "📷 **Trouvé un code dans l’album les visages qu’on aime, les rires capturés, les instants figés mais jamais oubliés… Si tu cherches ce qui nous unit tous,  tape ce mot sur le site?**", "answer": "famille", "success": "👨‍👩‍👧‍👦 **Famille, notre union éternelle.**", "next": "💬 **Envoie un message WhatsApp avec ce code**", "image": "C:/Users/yacin/OneDrive/Streamlit 18 juin/anniv_mariage/DSC_3487.JPG"},
    5: {"riddle": "🎧 **Ecris moi le dernier mots de passe retrouvé  par whatsap ?**", "answer": "guitare", "success": "🎶 **Le son de la guitare... comme dans ta vidéo.**", "next": "🎥 **Trouve un code caché dans la guitare**", "video": "CHEMIN_DE_LA_VIDEO"},
    6: {"riddle": "🎸 **Énigme finale : entre le dernier code**", "answer": "surprise", "success": "🌟 **Tout réussi ! Prépare-toi pour une surprise magique ce soir.**", 
       "next": "✨ **Fin du jeu : Une soirée inoubliable t'attend !**",
       "final_message": "💃 **Mets ta plus belle robe ce soir, mon amour, une soirée féerique nous attend...** 🎆",
       "animation": "🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈"}
}

# 📜 Volet latéral pour afficher la progression
with st.sidebar:
    st.header("📜 Progression")
    for i in range(1, len(steps) + 1):
        if i < st.session_state.step:
            st.markdown(f"<p style='color:#32A852;font-size:18px;'>✅ Étape {i} : {steps[i]['next']}</p>", unsafe_allow_html=True)
        elif i == st.session_state.step:
            st.markdown(f"<p style='color:#CC0066;font-size:18px;'>▶️ Étape {i} (Active)</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:grey;font-size:18px;'>🔒 Étape {i} (Verrouillée)</p>", unsafe_allow_html=True)

# 🏆 Affichage de l'étape active uniquement
step_num = st.session_state.step
step = steps.get(step_num)

if step:
    st.markdown("---")
    show_message("🌹 Énigme en cours", step["riddle"])
    
    code_input = st.text_input(f"💬 Entre le code ici (Étape {step_num})", key=f"code_input_{step_num}").strip().lower()

    if st.button(f"✅ Valider étape {step_num}", key=f"validate_{step_num}"):
        if code_input == step["answer"]:
            show_success(step["success"])
            st.session_state.validated = True  # Active le bouton suivant après validation

    # 📜 Ajout du bouton pour avancer après validation
    if st.session_state.get("validated", False) and step_num < 6:
        if st.button("➡️ Passer à l’étape suivante"):
            st.session_state.step += 1
            st.session_state.validated = False  # Réinitialisation après passage à l'étape suivante
            st.rerun()

    # 📸 Affichage de la photo de mariage si l'étape est "famille"
    if step_num == 4 and "image" in step:
        st.image(step["image"], caption="💖 Notre mariage, un souvenir éternel.", use_column_width=True)

    # 🎥 Affichage de la vidéo si l'étape est "guitare"
    if step_num == 5 and "video" in step:
        st.video(step["video"])

    # 🎈 Affichage du message final seulement après validation correcte de l'étape 6
    if step_num == 6 and st.session_state.get("validated", False):
        show_message("💖 🌟 Félicitations, tu as tout réussi ! 🌟 💖", step["final_message"], "#FFEBF0", "#CC0066", "#FF3399")
        st.markdown(f"<div style='text-align:center;font-size:40px;'>{step['animation']}</div>", unsafe_allow_html=True)
