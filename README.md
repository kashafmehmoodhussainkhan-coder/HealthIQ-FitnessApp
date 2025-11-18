

# HealthIQ App

**HealthIQ App** is an interactive health and fitness application that calculates key health metrics and provides personalized meal suggestions. The application features a **Streamlit frontend** and a **backend DLL (`PROJECT3.DLL`)** to perform all core computations efficiently.

## Table of Contents

1. [Features](#features)
2. [Architecture](#architecture)
3. [Setup Instructions](#setup-instructions)
4. [Quick Start / Usage](#quick-start--usage)
5. [Example Input & Output](#example-input--output)
6. [DLL Notes](#dll-notes)
7. [Screenshots](#screenshots)
8. [License](#license)

---

## Features

* Calculate **Basal Metabolic Rate (BMR)** based on age, weight, height, and gender.
* Estimate **Total Daily Energy Expenditure (TDEE)** based on activity level.
* Adjust recommended daily **calorie intake** according to fitness goals (Lose weight, Gain weight, Maintain weight).
* Provide **diet-specific meal plans** for Vegan, Vegetarian, Non-Vegetarian, and Gluten-Free preferences.
* Simple, intuitive, and interactive **Streamlit interface** for easy input and results display.

---

## Architecture

The project consists of two main components:

1. **Frontend (Streamlit)**

   * Collects user input: age, gender, weight, height, fitness goal, dietary preference, and activity level.
   * Displays results including BMR, TDEE, recommended calories, and meal plan.

2. **Backend (`PROJECT3.DLL`)**

   * Handles all computations: BMR, TDEE, calorie adjustments, and meal planning.
   * Must match the system architecture (32-bit or 64-bit) for proper integration with Python.


---

## Setup Instructions

1. Ensure you have **Python 3.10 or higher** installed.
2. Place `PROJECT3.DLL` in the same folder as `HEALTHIQ_APP.py`.
3. Open a terminal or command prompt in the project directory.
4. Install Streamlit if not already installed:

```bash
pip install streamlit
```

5. Launch the application:

```bash
streamlit run HEALTHIQ_APP.py
```

---

## Quick Start / Usage

1. The app will open in your default browser.
2. Fill in your personal details on the input panel:

   * Age
   * Gender
   * Weight (kg)
   * Height (cm)
   * Fitness Goal
   * Dietary Preference
   * Activity Level
3. Click **Submit** (or the equivalent button).
4. The main panel will display:

   * Calculated BMR
   * TDEE (Total Daily Energy Expenditure)
   * Recommended daily calorie intake
   * Tailored meal plan based on dietary preference

---

## Example Input & Output

| Parameter          | Example Value  |
| ------------------ | -------------- |
| Age                | 25             |
| Gender             | Female         |
| Weight (kg)        | 60             |
| Height (cm)        | 165            |
| Fitness Goal       | Lose weight    |
| Dietary Preference | Vegetarian     |
| Activity Level     | Lightly active |

**Example Output:**

```
Calculated BMR: 1400 kcal/day
TDEE: 1925 kcal/day
Recommended Daily Calorie Intake: 1425 kcal/day

--- VEGETARIAN MEAL PLAN ---
Breakfast: Oats with almond butter and chia seeds.
Lunch: Lentil stew with quinoa and spinach.
Dinner: Tofu stir-fry with broccoli, carrots, and brown rice.
```

---

## DLL Notes

* Ensure `PROJECT3.DLL` matches your Python interpreter architecture (32-bit or 64-bit).
* If you encounter `OSError: [WinError 193] %1 is not a valid Win32 application`, verify your Python and DLL architectures match.
* `PROJECT3.DLL` handles all backend computations and meal planning logic.

---






## License
## Author: kashaf mehmood

This project is licensed under the **MIT License**.

