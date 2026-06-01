# 2026-06-01

# 상속
class Animal: # 부모 클래스
  def __init__(self,name):
    self.name = name
  
  def make_sound(self):
    print('동물이 소리를 냅니다.')


class Dog(Animal): # 자식 클래스
  
  def make_sound(self):
    print('강아지가 멍멍 하고 웁니다.')

dog1 = Dog('개죽이')
dog1.make_sound()

print(dog1.name)
# 출력 결과 예시 : 강아지가 멍멍 하고 웁니다.\n개죽이