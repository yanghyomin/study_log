class Car{
    String name;
    int speed;
    boolean sold;

    void speedUp(){
        speed += 10;
    }
    void speedDown(){
        speed -= 10;
    }
    void setSold(){
        sold = true;
    }
}

public class CarTest {
    public static void main(String[] args) {
        Car c1 = new Car();
        Car c2 = new Car();

        c1.speed = 30;
        c2.speed = 20;

        System.out.printf("현재 c1의 속도: %d\n현재 c2의 속도: %d\n", c1.speed, c2.speed);

        c1.speedDown();
        System.out.println("c1 속도 다운");
        c2.speedUp();
        System.out.println("c2 속도 업");

        System.out.printf("현재 c1의 속도: %d\n현재 c2의 속도: %d\n", c1.speed, c2.speed);

        c1.setSold();
        System.out.println("c1 팔기");

        System.out.printf("c1 sold: %s\nc2 sold: %s", c1.sold,c2.sold);
    }
}
