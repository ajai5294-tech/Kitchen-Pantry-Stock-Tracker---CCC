public class items{
    private double capacity;
    private String brandName;
    private double cost;
    public items(String brandName)
    {
        brandName = brandName;
        capacity = 100;
    }
    public String getBrandName()
    {
        return brandName;
    }
    public double getCapacity()
    {
        return capacity;
    }
    public void reduceCapacity(double amountUsed)
    {
        capacity -= amountUsed;
    }
}