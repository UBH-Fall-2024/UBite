package FoodData;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;

public class Food {
    //public Allergen allergies;
    public double calories;
    public String alert;
    public double totalFat;
    public double cholesterol;
    public double sodium;
    public double totalCarb;
    public double protein;
    public ArrayList<String> ingredients;

    public Food(double calories, String alert, double totalFat, double cholesterol, double sodium, double totalCarb, double protein, ArrayList<String> ingredients){
        this.calories = calories;
        this.alert = alert;
        this.totalFat = totalFat;
        this.cholesterol = cholesterol;
        this.sodium = sodium;
        this.totalCarb = totalCarb;
        this.protein = protein;
        this.ingredients = ingredients;
    }

    public ArrayList<String> getIngredients() {
        return ingredients;
    }
    public double getCalories() {
        return calories;
    }
    public String getAlert() {
        return alert;
    }

    public double getTotalFat() {
        return totalFat;
    }

    public double getCholesterol() {
        return cholesterol;
    }

    public double getSodium() {
        return sodium;
    }
    public double getProtein(){
        return protein;
    }

}
