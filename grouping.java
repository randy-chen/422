/**
*   Author: Team CHARCL Industries Incorporated Internationale Limited Closed Squad
*   Project 1 for CIS 422 at the University of Oregon
*   "grouping.java" is the algorithmic implmentation and core of our program
**/

import java.util.*;
import java.io.*;

public class grouping{

    //Returns the number of common elements between two lists
    public static int getNumberOfCommonElements(ArrayList<String> list1, ArrayList<String> list2){
        List<String> common = new ArrayList<String>(list1);
        common.retainAll(list2);
        return common.size();
    }

    //Returns true if the 3 given person have at least the "weight" number of common elements in the given attribute
    //Returns false if otherwise
    public static boolean canGroup(person person1, person person2, person person3, int weight, int attribute){
        if(getNumberOfCommonElements(person1.getAttribute(attribute),person2.getAttribute(attribute)) >= weight){
            if(getNumberOfCommonElements(person1.getAttribute(attribute),person3.getAttribute(attribute)) >= weight){
                if(getNumberOfCommonElements(person3.getAttribute(attribute),person2.getAttribute(attribute)) >= weight){
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String [] args){
        // The first argument will be the inputted txt file
        File file = new File(args[0]);
        // We then create the list of people
        ArrayList<person> listOfPeople = new ArrayList<person>();
        // Our initial max weight is 5
        int MAX_WEIGHT = 5;
        // We read the text file
        try{
          Scanner scanner = new Scanner(file);
          int numAttr = Integer.parseInt(scanner.nextLine());
          while(scanner.hasNextLine()){
              String name = scanner.nextLine();
              person Person = new person(name);
              for(int i = 0; i < numAttr; i++){
                  ArrayList<String> list = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(",")));
                  Person.addAttribute(list);
              }
              listOfPeople.add(Person);
          }
        } catch(FileNotFoundException e) {
          e.printStackTrace();
        }
        // We then sort the list of people based on their total availability
        Collections.sort(listOfPeople, new Comparator<person>() {
                @Override
                public int compare(person person1, person person2){
                    return (person1.totalAvailability() - person2.totalAvailability());
                }
        });

        // This is where we do the greedy grouping
        ArrayList<ArrayList<String>> Groups = new ArrayList<>();
        for(int i = 0; i < listOfPeople.size(); i++){
            for(int j = i+1; j < listOfPeople.size(); j++){
                for(int k = j+1; k <listOfPeople.size(); k++){
                    for(int q = MAX_WEIGHT; q > 0; q--){
                        if(canGroup(listOfPeople.get(i),listOfPeople.get(j),listOfPeople.get(k),q,0)){
                            for(int r = MAX_WEIGHT; r > 0; r--){
                                if(canGroup(listOfPeople.get(i),listOfPeople.get(j),listOfPeople.get(k),r,1)){
                                    ArrayList<String> group = new ArrayList<>();
                                    group.add(listOfPeople.get(i).getName());
                                    group.add(listOfPeople.get(j).getName());
                                    group.add(listOfPeople.get(k).getName());
                                    Groups.add(group);
                                    listOfPeople.remove(i);
                                    listOfPeople.remove(j-1);
                                    listOfPeople.remove(k-2);
                                    if(listOfPeople.size() < 3){
                                        break;
                                    }
                                    r = 0;
                                    q = 0;
                                    i = 0;
                                    j = 1;
                                    k = 1;
                                }
                            }
                        }
                    }
                }
            }
        }

        //We then just start adding the remaining people to new groups or add them to pre-existing
        while(listOfPeople.size() > 0){
            if(listOfPeople.size() >= 3){
                ArrayList<String> group = new ArrayList<>();
                group.add(listOfPeople.get(0).getName());
                group.add(listOfPeople.get(1).getName());
                group.add(listOfPeople.get(2).getName());
                Groups.add(group);
                listOfPeople.remove(0);
                listOfPeople.remove(0);
                listOfPeople.remove(0);
            }else{
                for(int i = 0; i < Groups.size(); i++){
                    if(Groups.get(i).size() < 4){
                        Groups.get(i).add(listOfPeople.get(0).getName());
                        listOfPeople.remove(0);
                        if(listOfPeople.size() == 0){
                            i = Groups.size();
                        }
                    }
                }
            }
        }

        for(int i = 0; i < Groups.size(); i++){
            System.out.println(Groups.get(i).toString());
        }
        try{
          PrintWriter writer = new PrintWriter(args[1], "UTF-8");
          for(int i = 0; i < Groups.size(); i++){
              writer.println(Groups.get(i).toString());
          }
          writer.close();
        } catch (IOException e) {
          e.printStackTrace();
        }
    }
}
