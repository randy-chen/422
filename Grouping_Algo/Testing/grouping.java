import java.util.*;

public class grouping{
    static Scanner scanner = new Scanner(System.in);
    
    public static int getNumberOfCommonElements(ArrayList<String> list1, ArrayList<String> list2){
        List<String> common = new ArrayList<String>(list1);
        common.retainAll(list2);
        return common.size();
    }

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
        int numAttr = Integer.parseInt(scanner.nextLine());
        ArrayList<person> listOfPeople = new ArrayList<person>();
        while(scanner.hasNextLine()){
            String name = scanner.nextLine();
            person Person = new person(name);
            for(int i = 0; i < numAttr; i++){
                ArrayList<String> list = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" , ")));
                Person.addAttribute(list);
            }
            listOfPeople.add(Person);
        }
        for(person item: listOfPeople){
            System.out.println(item.getName());
        }
        ArrayList<ArrayList<String>> Groups = new ArrayList<>();
        for(int i = 0; i < listOfPeople.size(); i++){
            for(int j = i+1; j < listOfPeople.size(); j++){
                for(int k = j+1; k <listOfPeople.size(); k++){
                    if(canGroup(listOfPeople.get(i),listOfPeople.get(j),listOfPeople.get(k),0,0)){
                        ArrayList<String> group = new ArrayList<>();
                        group.add(listOfPeople.get(i).getName());
                        group.add(listOfPeople.get(j).getName());
                        group.add(listOfPeople.get(k).getName());
                        Groups.add(group);
                        listOfPeople.remove(i);
                        listOfPeople.remove(j);
                        listOfPeople.remove(k);
                        if(listOfPeople.size() < 3){
                            break;
                        }
                    } 
                }
            }
        }
        if(listOfPeople.size() > 0){
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
                    }
                }
            }
        }

        for(int i = 0; i < Groups.size(); i++){
            System.out.print(Groups.get(i).toString());
        }
        System.out.println("\n");
    }
}
