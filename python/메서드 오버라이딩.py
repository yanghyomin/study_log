# 2026-06-08

class bssm_one : # 부모클래스
  def __init__(self,name,score):
    self.name = name
    self.score = score


  def get_score(self):
    print(f"{self.name}의 평균은 {sum(self.score) / len(self.score)}")


class OneThree(bssm_one) : # 자식클래스
  def __init__(self,name,score,height): # 메서드 오버라이딩
    super().__init__(name,score)
    self.height = height

  def get_score(self):
    super().get_score()
    print(f"{self.score}")
    print(f"키는 : {self.height}")


class OneFour(bssm_one) :
  pass


# 출력문
s1 = OneThree('민세',[80,30,100],180)
s1.get_score()

s2 = OneFour('한성',[80,30,100])
s2.get_score()

# 출력결과:
'''
민세의 평균은 70.0
[80, 30, 100]
키는 : 180
한성의 평균은 70.0
'''