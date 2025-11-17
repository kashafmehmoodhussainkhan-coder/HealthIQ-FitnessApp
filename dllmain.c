#include "HEALTHIQ.h"
#include <stdio.h>
#include <string.h>

// CALCULATE BMR
DLLIMPORT float calculateBMR(int Age, float Weight, float Height, const char Gender[]) {
    if (strcmp(Gender, "male") == 0)
        return (10 * Weight) + (6.25 * Height) - (5 * Age) + 5;
    else if (strcmp(Gender, "female") == 0)
        return (10 * Weight) + (6.25 * Height) - (5 * Age) - 161;
    else
        return 0;
}

// CALCULATE TDEE
DLLIMPORT float calcTDEE(float BMR, float activityFactor) {
    return BMR * activityFactor;
}

// ADJUST CALORIES BASED ON GOAL
DLLIMPORT float adjustCalories(float TDEE, const char fitnessGoal[]) {
    if (strcmp(fitnessGoal, "lose weight") == 0)
        return TDEE - 500;
    else if (strcmp(fitnessGoal, "gain weight") == 0)
        return TDEE + 500;
    else
        return TDEE;
}

// CALCULATE BMI
DLLIMPORT float calculateBMI(float Weight, float Height_cm) {
    float height_m = Height_cm / 100.0;
    return Weight / (height_m * height_m);
}

// MEAL PLAN BASED ON DIETARY PREFERENCE
DLLIMPORT void getMealPlan(const char preference[], char output[]) {
    if (strcmp(preference, "vegetarian") == 0) {
        strcpy(output, "Breakfast: Oats with almond butter and chia seeds.\n"
                       "Lunch: Lentil stew with quinoa and spinach.\n"
                       "Dinner: Tofu stir-fry with broccoli, carrots, and brown rice.");
    } else if (strcmp(preference, "non vegetarian") == 0 || strcmp(preference, "non-vegetarian") == 0) {
        strcpy(output, "Breakfast: Scrambled eggs with spinach.\n"
                       "Lunch: Grilled chicken with brown rice and veggies.\n"
                       "Dinner: Baked salmon with sweet potato and green beans.");
    } else if (strcmp(preference, "vegan") == 0) {
        strcpy(output, "Breakfast: Smoothie with banana, almond milk, and peanut butter.\n"
                       "Lunch: Quinoa salad with chickpeas, cucumber, and avocado.\n"
                       "Dinner: Vegan curry with coconut milk, tofu, and mixed vegetables.");
    } else if (strcmp(preference, "gluten-free") == 0 || strcmp(preference, "gluten free") == 0) {
        strcpy(output, "Breakfast: Gluten-free pancakes with blueberries and maple syrup.\n"
                       "Lunch: Grilled chicken with quinoa and steamed vegetables.\n"
                       "Dinner: Grilled fish with roasted sweet potatoes and broccoli.");
    } else {
        strcpy(output, "Invalid dietary preference.");
    }
}

// CALCULATE MACROS
DLLIMPORT void cal_macros(float calories, float *carbs, float *proteins, float *fats, const char fitnessGoal[]) {
    float carb_p, protein_p, fat_p;

    if (strcmp(fitnessGoal, "lose weight") == 0) {
        carb_p = 0.40;
        protein_p = 0.30;
        fat_p = 0.30;
    } else if (strcmp(fitnessGoal, "gain weight") == 0) {
        carb_p = 0.55;
        protein_p = 0.25;
        fat_p = 0.20;
    } else {
        carb_p = 0.50;
        protein_p = 0.25;
        fat_p = 0.25;
    }

    *carbs = calories * carb_p / 4.0;
    *proteins = calories * protein_p / 4.0;
    *fats = calories * fat_p / 9.0;
}
