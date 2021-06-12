import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    private static int backpackSize;
    private static int numberOfItems;
    private static int[] values;
    private static int[] weights;

    public static void main(String[] args) throws IOException {

        //readDataFromFile("src/data1.txt"); // program dzialajacy na danych z pliku "data.txt"
        //readDataFromFile("src/data2.txt"); // program dzialajacy na danych z pliku "dataV2.txt"
        readDataFromConsole(); // program dzialajacy na danych z klawiatury

        int maxSum = 0;
        boolean[] arr = new boolean[numberOfItems];

        for (int i = 0; i<Math.pow(2, numberOfItems); i++){
            boolean[] tmpArr = new boolean[numberOfItems];
            int tmpSum = 0;

            for (int j = 0; j< numberOfItems; j++){
                if ( ( (i>>j) & 1 ) == 1 ) {
                    tmpArr[j] = true;
                    tmpSum += values[j];
                } else {
                    tmpArr[j] = false;
                }
            }

            if(tmpSum > maxSum){
                int tmpCapacity = 0;
                for (int k = 0; k< numberOfItems; k++){
                    if (tmpArr[k]) {
                        tmpCapacity += weights[k];
                    }
                }
                if (tmpCapacity <= backpackSize){
                    maxSum = tmpSum;
                    arr = tmpArr;
                }
            }

        }

        for (int i = 0; i < numberOfItems; i++) {
            if(arr[i]){
                System.out.println(values[i]+" "+weights[i]);
            }
        }

    }

    public static void readDataFromConsole() throws IOException {
        Scanner scanner = new Scanner(System.in);
        String dane = scanner.nextLine();
        backpackSize = Integer.parseInt(dane);
        dane = scanner.nextLine();
        numberOfItems = Integer.parseInt(dane);
        values = new int[numberOfItems];
        weights = new int[numberOfItems];

        for (int i = 0; i<numberOfItems; i++){
            dane = scanner.nextLine();
            String[] splited = dane.split(" ");
            values[i]= Integer.parseInt(splited[0]);
            weights[i]= Integer.parseInt(splited[1]);
        }
        scanner.close();
    }

    public static void readDataFromFile(String path) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(path));
        String dane = scanner.nextLine();
        backpackSize = Integer.parseInt(dane);
        dane = scanner.nextLine();
        numberOfItems = Integer.parseInt(dane);
        values = new int[numberOfItems];
        weights = new int[numberOfItems];

        for (int i = 0; i<numberOfItems; i++){
            dane = scanner.nextLine();
            String[] splited = dane.split(" ");
            values[i]= Integer.parseInt(splited[0]);
            weights[i]= Integer.parseInt(splited[1]);
        }
        scanner.close();
    }

}
