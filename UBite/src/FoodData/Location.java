package FoodData;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.ArrayList;

public class Location {
    public String location;
    public HashMap<String, Food> menu;
     public Location(String location){
         this.location = location;
         this.menu = populateMenu(location);
     }
     public HashMap<String, Food> getMenu(){
         return menu;
     }
     public void populateFood(String file, HashMap<String, Food> curMenu){
         ArrayList<String> macros = readFile(file);
         String foodName = macros.get(0); //first is name, save in var
         //for the rest, save as vars
         int calories = Integer.parseInt(macros.get(1));
         String alert = macros.get(2);
         int fat = Integer.parseInt(macros.get(3));
         int cholesterol = Integer.parseInt(macros.get(4));
         int sodium = Integer.parseInt(macros.get(5));
         int carb = Integer.parseInt(macros.get(6));
         int protein = Integer.parseInt(macros.get(7));
         int size = macros.size();
         ArrayList<String> ingredients = new ArrayList<>();
         for(int i = 8; i < size; i++){
             ingredients.add(macros.get(i));
         }
         //make a new food and put vars in
         Food food = new Food(calories, alert, fat, cholesterol, sodium, carb, protein, ingredients);
         //add name to hashmap, with food as value
         curMenu.put(foodName, food); //fio how to move this into the populate menu instead
     }

     public HashMap<String, Food> populateMenu(String location_name){ //debug
         HashMap<String, Food> curMenu = new HashMap<>();
         File directory = new File("src/" + location_name);
         File[] csvFiles = directory.listFiles((dir, name) -> name.toLowerCase().endsWith(".csv"));
         for (File csvFile : csvFiles) {
             populateFood(String.valueOf(csvFile), curMenu);
         }
         return curMenu;
         //populate food
     }
     public static ArrayList<String> readFile(String filename) {
         try {
             return new ArrayList<>(Files.readAllLines(Paths.get(filename)));
         } catch (IOException e) {
             return new ArrayList<>();
         }
     }
}
