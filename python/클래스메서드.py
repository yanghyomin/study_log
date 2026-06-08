# 2026-06-08

class fishbread:
  total = 0

  def __init__(self,name,price):
    self.name = name
    self.price = price
    fishbread.total += 1

  @classmethod
  def make_pat_bread(cls):
    print("팥붕 만들기")
    return cls("팥붕",600)

  @classmethod
  def make_sue_bread(cls):
    print("슈붕 만들기")
    return cls("슈붕",1000)

  @staticmethod # 정적 메서드
  def cal_bags(count):
    print(f"빵 {count}개에 필요한 봉투개수 : {count // 5}")


# 출력문
b1 = fishbread.make_pat_bread()
b2 = fishbread.make_sue_bread()

print(b1.name,b1.price)
print(b2.name,b2.price)
print(fishbread.total)

b4 = fishbread.cal_bags(10)

# 출력결과:
'''
팥붕 만들기
슈붕 만들기
팥붕 600
슈붕 1000
2
빵 10개에 필요한 봉투개수 : 2
'''