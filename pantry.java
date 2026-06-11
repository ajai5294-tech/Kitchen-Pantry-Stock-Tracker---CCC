import java.util.ArrayList;
public class pantry{
    private ArrayList<items> storage = new ArrayList<>();
    public pantry()
    {
        ArrayList<items> storage = new ArrayList<>();
    }
    public String checkForLowStock()
    {
        int count = 0;
        System.out.println("Low on: ")
        for (int i = 0; i < storage.size(); ++ i)
        {
            if (storage.get(i).getCapacity() <= )//minimum reqiurment
                System.out.println(storage.get(i).getBrandName());
                else
                {
                    count ++;
                }
        }
        if (count == storage.size())
        {
            System.out.println("Nothing");
        }
    }
    
}