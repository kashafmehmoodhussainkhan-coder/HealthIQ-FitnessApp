import ctypes
import streamlit as st

#LOAD DLL

dll_path = r"C:\Users\kasha\Documents\project3.dll"
fitness_dll = ctypes.CDLL(dll_path)

# FUNCTION SIGNATURES
fitness_dll.calculateBMR.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_char_p]
fitness_dll.calculateBMR.restype = ctypes.c_float
fitness_dll.calcTDEE.argtypes = [ctypes.c_float, ctypes.c_float]
fitness_dll.calcTDEE.restype = ctypes.c_float
fitness_dll.adjustCalories.argtypes = [ctypes.c_float, ctypes.c_char_p]
fitness_dll.adjustCalories.restype = ctypes.c_float
fitness_dll.calculateBMI.argtypes = [ctypes.c_float, ctypes.c_float]
fitness_dll.calculateBMI.restype = ctypes.c_float
fitness_dll.getMealPlan.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
fitness_dll.getMealPlan.restype = None
fitness_dll.cal_macros.argtypes = [ctypes.c_float, ctypes.POINTER(ctypes.c_float),
                                   ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_char_p]
fitness_dll.cal_macros.restype = None


st.set_page_config(page_title="HEALTHIQ", layout="centered", page_icon="💪")

# ============================
st.markdown("""
    <style>
    /* Page background gradient */
    .stApp {
        background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
        color: #222;
    }
    /* Header animation */
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.1);}
        100% {transform: scale(1);}
    }
    .logo {
        font-size: 50px;
        font-weight: bold;
        color: #FF4B4B;
        animation: pulse 2s infinite;
        text-align: center;
    }
    .description {
        text-align:center;
        font-size: 18px;
        color:#FF6F61;
        margin-bottom:20px;
    }
    .stButton>button {
        background: linear-gradient(to right, #FF4B4B, #FF6F61);
        color:white;
        font-weight:bold;
        border-radius:10px;
        height:45px;
        width:100%;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #FF6F61, #FF4B4B);
    }
    .card {
        background: #fff7f7;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .meal-icon {
        font-size: 25px;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================
# HEADER
# ============================
st.markdown('<div class="logo">HEALTHIQ</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Your personal fitness & nutrition assistant. Calculate BMR, TDEE, calories, BMI, macros and get meal plans instantly!</div>', unsafe_allow_html=True)

st.write("---")

# USER INPUT

age = st.number_input("Enter your age (years)", min_value=1, max_value=120, value=25)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

gender = st.selectbox("Gender", ["male", "female"])
fitness_goal = st.selectbox("Fitness Goal", ["lose weight", "gain weight", "maintain weight"])
diet_pref = st.selectbox("Dietary Preference", ["vegetarian", "non-vegetarian", "vegan", "gluten-free"])
activity_level = st.selectbox("Activity Level", ["sedentary", "lightly active", "moderately active", "very active", "extra active"])


# ACTIVITY FACTOR

activity_dict = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725,
    "extra active": 1.9
}
activity_factor = activity_dict.get(activity_level.lower(), 1.2)


# CALCULATIONS

if st.button("Generate My Fitness Plan"):
    # BMR
    bmr = fitness_dll.calculateBMR(age, weight, height, gender.encode('utf-8'))
    # TDEE
    tdee = fitness_dll.calcTDEE(bmr, activity_factor)
    # Adjusted calories
    calories = fitness_dll.adjustCalories(tdee, fitness_goal.encode('utf-8'))
    # BMI
    bmi = fitness_dll.calculateBMI(weight, height)
    # Macros
    carbs = ctypes.c_float()
    proteins = ctypes.c_float()
    fats = ctypes.c_float()
    fitness_dll.cal_macros(calories, ctypes.byref(carbs), ctypes.byref(proteins), ctypes.byref(fats), fitness_goal.encode('utf-8'))
    # Meal plan
    meal_output = ctypes.create_string_buffer(1024)
    fitness_dll.getMealPlan(diet_pref.encode('utf-8'), meal_output)
    meals = meal_output.value.decode().split("\n")

    # DISPLAY RESULTS 
    st.subheader("🏋️‍♂️ Fitness Results")
    st.markdown(f"""
        <div class="card">
        <b>BMR:</b> {bmr:.2f} kcal/day<br>
        <b>TDEE:</b> {tdee:.2f} kcal/day<br>
        <b>Recommended Calories:</b> {calories:.2f} kcal/day<br>
        <b>BMI:</b> {bmi:.2f}<br>
        <b>Macros (g/day):</b> Carbs: {carbs.value:.1f}, Proteins: {proteins.value:.1f}, Fats: {fats.value:.1f}
        </div>
    """, unsafe_allow_html=True)

    st.subheader("🍽️ Meal Plan")
    meal_icons = ["🥣", "🥗", "🍲"]
    for i, meal in enumerate(meals):
        st.markdown(f"""
            <div class="card">
            <span class="meal-icon">{meal_icons[i%3]}</span> {meal}
            </div>
        """, unsafe_allow_html=True)
