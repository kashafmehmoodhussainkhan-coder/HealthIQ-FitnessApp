#ifndef HEALTHIQ_H
#define HEALTHIQ_H

#ifdef _WIN32
#define DLLIMPORT __declspec(dllexport)
#else
#define DLLIMPORT
#endif

// Function prototypes

// Calculate Basal Metabolic Rate
DLLIMPORT float calculateBMR(int Age, float Weight, float Height, const char Gender[]);

// Calculate Total Daily Energy Expenditure
DLLIMPORT float calcTDEE(float BMR, float activityFactor);

// Adjust Calories based on fitness goal
DLLIMPORT float adjustCalories(float TDEE, const char fitnessGoal[]);

// Calculate Body Mass Index
DLLIMPORT float calculateBMI(float Weight, float Height_cm);

// Get meal plan based on dietary preference
DLLIMPORT void getMealPlan(const char preference[], char output[]);

// Calculate macronutrient breakdown
DLLIMPORT void cal_macros(float calories, float *carbs, float *proteins, float *fats, const char fitnessGoal[]);

#endif // HEALTHIQ_H
