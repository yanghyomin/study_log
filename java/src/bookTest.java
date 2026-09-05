class Book{
    String borrowed = "대출 가능";
    String title;
    String author;

    void setInfo(String title, String author){
        this.title = title;
        this.author = author;
    }

    void borrow(){
        if(borrowed.equals("대출 가능")){
            borrowed = "대출 중";
        }
        else{
            System.out.printf("이미 %s인 책입니다.\n", borrowed);
        }
    }

    void returnBook(){
        borrowed = "대출 가능";
    }

    void calculateLateFee(int overdueDats){
        if(overdueDats <= 3){
            System.out.printf("%d일 연체료: %d원\n",overdueDats,overdueDats*500);
        }
        else{
            System.out.printf("%d일 연체료: %d원\n",overdueDats,overdueDats*1000);
        }
    }

    void printStatus(){
        System.out.printf("%s - %s\n",title,borrowed);
    }
}

public class bookTest {
    public static void main(String[] args) {
        Book book1 = new Book();
        book1.setInfo("어린 왕자","생텍쥐페리");

        book1.borrow();
        book1.borrow();
        book1.printStatus();
        book1.calculateLateFee(5);
        book1.returnBook();
        book1.printStatus();

    }
}
