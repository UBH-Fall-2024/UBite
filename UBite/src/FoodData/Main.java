package FoodData;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static FoodData.Location.readFile;

public class Main {
    static Food meal = new Food(0,"",0,0,0,0,0,new ArrayList<>());

    public static void main(String[] args) throws IOException {
        ArrayList<String> input = readFile("src/input.csv");
        while(!input.isEmpty()){
            String locationName = input.get(0);
            String foodName = input.get(1);
            int servings = Integer.parseInt(input.get(2));

            Location location = new Location(locationName);
            HashMap<String, Food> menu = location.getMenu();
            Food food = menu.get(foodName);
            for(int i = 0; i < servings; i++){
                meal.calories += food.getCalories();
                meal.alert = food.getAlert();
                meal.totalFat = food.getTotalFat();
                meal.cholesterol = food.getCholesterol();
                meal.sodium = food.getSodium();
                meal.totalCarb = food.getTotalFat();
                meal.protein = food.getProtein();
                meal.ingredients = food.getIngredients();
            }
            Path path = Paths.get("output.txt");
            Files.write(path, List.of());
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
                writer.write(String.valueOf(food.getCalories()));
                writer.newLine();
                writer.write(String.valueOf(food.getAlert()));
                writer.newLine();
                writer.write(String.valueOf(food.getTotalFat()));
                writer.newLine();
                writer.write(String.valueOf(food.getCholesterol()));
                writer.newLine();
                writer.write(String.valueOf(food.getSodium()));
                writer.newLine();
                writer.write(String.valueOf(food.getTotalFat()));
                writer.newLine();
                writer.write(String.valueOf(food.getProtein()));
                writer.newLine();
                for(int i = 0; i < food.getIngredients().size(); i++){
                    writer.write(food.getIngredients().get(i));
                    writer.newLine();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            input = readFile("src/input.csv");
        }

    }
}
