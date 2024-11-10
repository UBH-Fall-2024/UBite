def component_submit(request):
    if request.method == "POST":
        restaurant_name = request.form["restaurant"]
        food_submission["restaurant"] = restaurant_name
        return redirect(url_for("get-food-data", location = restaurant_name))

    return render_template("index.html")