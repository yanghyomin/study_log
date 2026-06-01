# 2026-06-01

## 예시 1
class Account:
  interest_rate = 0.02 # 클래스변수
  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
  def apply_interest(self):
    self.balance += (self.balance * self.interest_rate)

# 테스트 코드
acc = Account("권민세", 10000)
acc.deposit(5000)
acc.apply_interest()
print(f"{acc.owner}님의 최종 잔액: {acc.balance}원") 
# 출력 결과 예시: 권민세님의 최종 잔액: 15300.0원

## 예시 2
class Product:
  free_shipping_limit = 30000 #클래스변수
  def __init__(self,name,price):
    self.name = name
    self.price = price
  def get_shipping_fee(self):
    if self.price < self.free_shipping_limit:
      return "배송비 3,000원이 부과됩니다."
    return "무료 배송 대상입니다."
  
# 테스트 코드
p1 = Product("무선 마우스", 25000)
p2 = Product("기계식 키보드", 45000)

print(f"{p1.name}: {p1.get_shipping_fee()}") # 배송비 부과 안내 출력
print(f"{p2.name}: {p2.get_shipping_fee()}") # 무료 배송 안내 출력