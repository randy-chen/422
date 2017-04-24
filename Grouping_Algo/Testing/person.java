import java.util.*;

public class person{
    private String name;
    private ArrayList<ArrayList<String>> attributes;

    public person(String fullname){
        name = fullname;
        attributes = new ArrayList<ArrayList<String>>();
    }

    public String getName(){
        return name;
    }

    public void setName(String fullname){
        name = fullname;
    }

    public void addAttribute(ArrayList<String> attr_name){
        attributes.add(attr_name);
    }

    public ArrayList<ArrayList<String>> getAttributes(){
        return attributes;
    }

    public ArrayList<String> getAttribute(int i){
        return attributes.get(i);
    }

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
