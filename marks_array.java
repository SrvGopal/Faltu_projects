import java.util.*;

public class y{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("ENter the number of the subjects ");
        int lenght = sc.nextInt();
        
        double [] marks = new double[lenght];

        for(int j = 0;j < lenght;j++){
            System.out.print("Enter the marks of the "+j+1+"th subject here");
            marks[j] = sc.nextDouble();

        }
        double sum = 0;
        for(int k = 0;k < lenght;k++){
            sum += marks[k];

        }
        System.out.println("The sum of the marks of this student is "+sum);
        double average = sum / lenght;

        System.out.println("The average marks of this student is "+average);
    
    }
}
