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
import java.util.Scanner;

import static FoodData.Location.readFile;

public class Main {
    static Food meal = new Food(0,"",0,0,0,0,0,new ArrayList<>());

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Where are you dining?\n" +
                "(1) Student Union - Open\n" +
                "(2) One World Cafe - Under construction \n" +
                "(3) C3 Dining Hall - Under construction \n" +
                "(4) Govs Dining Hall - Under construction \n" +
                "(5) NSC - Under construction \n");
        int userInput = scanner.nextInt();
        if(userInput == 1){
            System.out.println("What dining facility are you at?  \n" +
                    "(1) Champa Sushi \n" +
                    "(2) Jamba Juice \n" +
                    "(3) Moes \n" +
                    "(4) Fowl Play \n" +
                    "(5) Stackers \n");
            userInput = scanner.nextInt();
            if(userInput == 1){
                System.out.println("What are you eating? \n" +
                        "(1) Raw Salmon Avocado Roll \n" +
                        "(2) Salmon Avocado Roll W/ Brown Rice \n" +
                        "(3) Smoked Salmon Avocado Roll \n" +
                        "(4) Smoked Salmon Avocado W/ Brown Rice \n" +
                        "(5) California Roll \n" +
                        "(6) Tuna Avocado Roll \n"
                );
                userInput = scanner.nextInt();
                //while(!input.isEmpty()){
                if(userInput == 1){
                    try (FileWriter writer = new FileWriter("output.txt")) {
                        writer.write("Champa_Sushi");
                        writer.write("Raw Salmon Avocado Roll");
                        writer.write(String.valueOf(1));
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                ArrayList<String> input = readFile("src/input.csv");//
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
                    //input = readFile("src/input.csv");
                //}
            }
        }

    }
}
