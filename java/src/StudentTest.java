import java.util.Scanner;

class Student{
    String name;
    int age;
    float average;

    void setInfo(String name, int age, float average){
        this.name = name;
        this.age = age;
        this.average = average;
    }

    String getAchievementLevel(){
        if(average >= 90){
            return "우수";
        }
        else if(average >= 70){
            return "보통";
        }
        else{
            return "노력 필요";
        }
    }
    void printInfo(){
        System.out.printf("학생: %s, 나이: %d세, 평균: %.1f, 성취도: %s", name,age,average,getAchievementLevel());
    }
}

public class StudentTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student student1 = new Student();

        String name = sc.nextLine();
        int age = sc.nextInt();
        float average = sc.nextFloat();
        student1.setInfo(name,age,average);

        student1.printInfo();
    }
}
