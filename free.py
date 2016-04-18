#-*-coding:cp949
name = 'zed' # " 이나 ' 이나 상관없다.
height_cm = 180
cm_to_inch = 1.0/2.54 # 단위 변환 변수
height_inch = height_cm*cm_to_inch

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inch
# 보니까 %s에서 %r의 차이는 작은따옴표가 있나 없나 차이다. %r 쓰면 작따 붙음. 저 둘은 문자열 내삽인데 %d 대신
# 숫자 내삽도 가능. 그러나 반대로 %d에서 %r,%s로 바꿀수는 없다.


