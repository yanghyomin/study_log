class Thermometer{
    float temperature;

    void setTemperature(float temperature){
        this.temperature = temperature;
    }
    void increase(){
        temperature++;
    }
    float toFahrenheit(){
        return temperature*9/5+32;
    }
    boolean isFreezing(){
        return temperature <= 0;
    }
    void printTemperature(){
        System.out.printf("섭씨: %.1f, 화씨: %.1f, 결빙: %b",temperature, toFahrenheit(), isFreezing());
    }
}

public class ThermometerTest {
    public static void main(String[] args) {
        Thermometer temp1 = new Thermometer();
        temp1.setTemperature(20);
        temp1.increase();
        temp1.increase();
        temp1.printTemperature();
    }
}
