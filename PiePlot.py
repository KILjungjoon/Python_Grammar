import matplotlib.pyplot as plt
plt.rc('font', size=15)        # 기본 폰트 크기  https://wooono.tistory.com/271

ratio = [91, 29, 64, 7]
labels =  ["Majoritarian", "Combined", "PR", "No Directed Elections"]
explode = [0.05, 0.05, 0.05, 0.05]

fig = plt.figure(figsize=(5,5)) ## 캔버스 생성
fig.set_facecolor('white')   # 캔버스 배경색을 하얀색으로 설정
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True)
plt.show()