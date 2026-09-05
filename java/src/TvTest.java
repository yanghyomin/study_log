class TV {
    // 맴버 변수 = 속성
    String color;
    boolean power;
    int channel;

    // 메서드 = 기능
    void power(){
        power = !power;
    }
    void channelUp(){
        channel++;
    }
    void channelDown(){
        channel--;
    }
}



public class TvTest {
    public static void main(String[] args) {
        TV t =new TV();
        t.channel = 7;
        t.channelDown();

        System.out.println(t.channel);
    }
}
