/**
*   Author: Team CHARCL Industries Incorporated Internationale Limited Closed Squad
*   Project 1 for CIS 422 at the University of Oregon
*   "person.java" will be the java class that represents each individuals in "grouping.java"
**/
import java.util.*;

public class person{
    //Here is their name
    private String name;
    //Here are their characteristics - note that even though our current implmentation
    //Defaults to 2 attributes, we could easily add more
    private ArrayList<ArrayList<String>> attributes;

    public person(String fullname){
        name = fullname;
        attributes = new ArrayList<ArrayList<String>>();
    }

    //Returns the name of this person
    public String getName(){
        return name;
    }

    //Sets the name of this person
    public void setName(String fullname){
        name = fullname;
    }

    //Adds a whole new attributes list (e.g. age, eye color, etc.)
    public void addAttribute(ArrayList<String> attr_name){
        attributes.add(attr_name);
    }

    //Returns all of the attribute lists
    public ArrayList<ArrayList<String>> getAttributes(){
        return attributes;
    }

    //Returns the ith attribute list
    public ArrayList<String> getAttribute(int i){
        return attributes.get(i);
    }

    //Returns the number of elements in all lists e.g. all their availability in schedules and languages
    public int totalAvailability(){
        int sum = 0;
        for(int i = 0; i < attributes.size(); i++){
            for(int j = 0; j < attributes.get(i).size(); j++){
                sum++;
            }
        }
        return sum;
    }
}
