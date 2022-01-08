# ColoringMapAlgorithm-CSP-
## Condition Satisfaction Algorithm
### Output
![UML](https://github.com/KeremTAN/ColoringMapAlgorithm-CSP-/blob/master/img/countries.png)
### Condition
![UML](https://github.com/KeremTAN/ColoringMapAlgorithm-CSP-/blob/master/img/condition.png)

<b>Our 1st method</b> has 2 parameters and does the sorting of the countries. </br>
In its parameter, it takes the graph structure of the countries and the list of names of the unsorted countries. </br>
Note: the graph structure of countries is defined as a local variable dictionary. </br>
It is important that we sort our countries from the most to the least number of neighbors, because if we don't do this and  </br>
color the countries with the fewest neighbors first, the colors of the countries with  </br>
the fewest neighbors will coincide with those of the neighboring countries. </br> 
Our method returns the sorted countries after sorting.  </br> </br>
<b>Our 2nd method</b> has 2 parameters and checks for correct coloring of country colors.  </br>
In its parameter, it takes the graph structure of the countries and the color dictionary of the countries.  </br>
First of all, it checks the countries that are on our graph and have not yet been added to our dictionary.  </br>
Then, we compare the colors of the countries and their neighbors in our dictionary through our graph.  </br>
If a country and any of its neighbors have the same color, we return the wrong value.  </br> </br>
<b>Our 3rd method</b> has 3 parameters and does the coloring of the countries.  </br>
In its parameter, it takes the graph structure of the countries, an empty dictionary for us to color, and an unsorted list of countries' names.  </br>
This method first calls our 1st method and sorts our unordered countries.  </br>
Our method traverses the sorted lists of countries and colors with indices to color our countries.  </br>
After coloring a country, it performs control with our 2nd method.  </br>
If it returns a false value to us, it colors the same country again, reducing the index it uses to hover by 1.  </br>
It also increments our solver-counter by 1.  </br>
When the number of elements of our solver-counter and our colors list are equal, it gives the message "unsolved problem".  </br>
After that, our method returns a false value with an empty dictionary and ends our program.  </br>
If our 2nd method returns true, it resets our solver-counter and continues coloring the countries.  </br>
After all countries are colored, our method returns two values. One is the colored dictionary of countries and the other is the correct value.
