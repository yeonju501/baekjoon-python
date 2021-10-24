# 컵홀더 양끝좌석에 컵홀더 / LL 사이에는 컵홀더 x / S 좌석 사이에 컵홀더
# 좌석의 수 N 좌석정보
# S*을 붙인다 > LL*을 붙인다 > 앞에 *을 붙이고 시작
# 별을 센다 > S와 L을 센다 > 문자가 더 많으면 별 갯수 출력, 별이 더 많으면 문자 갯수
# *S*S*S* / *S*LL*S* / *S*LL*LL*LL*S*S*LL* / *S*LL*LL*S*S*LL*
seat = int(input())
ppl = input()
full_seat = '*'
couple_seat = 'LL*'*ppl.count('LL')
normal_seat = 'S*'*ppl.count('S')
full_seat += couple_seat + normal_seat
if full_seat.count('*') >= len(full_seat) - full_seat.count('*'):
    print(len(full_seat) - full_seat.count('*'))
else:
    print(full_seat.count('*'))


