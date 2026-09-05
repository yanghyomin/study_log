class Pet{
    String name;
    String type;
    int age;

    String getAgeGroup(){
        if(age <= 1){
            return "아기";
        }
        else if(age <= 7){
            return "성체";
        }
        else{
            return "노령";
        }
    }

    void printInfo(){
        System.out.printf("이름: %s, 종류: %s, 나이: %d살, 성장 단계: %s\n", name, type, age, getAgeGroup());
    }
}

public class MovieTicketTest {
    public static void main(String[] args) {
        Pet pet1 = new Pet();
        Pet pet2 = new Pet();

        pet1.name = "초코";
        pet1.type = "강아지";
        pet1.age = 3;

        pet2.name = "나비";
        pet2.type = "고양이";
        pet2.age = 9;

        pet1.printInfo();
        pet2.printInfo();

    }
}
