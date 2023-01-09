'''
정수(integer)는
양의 정수(1, 2, 3, 4, 5, ...), 음의 정수(-1, -2, -3, -4, -5, ...), 0 과 같이
소숫점 아래에 수가 없는 수라고 할 수 있다.

변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

예시
n = input()
n = int(n)
print(n)
와 같은 형태로 가능하다.

참고
input() 을 사용하면 키보드로 입력(input)한 값을 가져온다.

 

변수 = input()
를 실행시키면 키보드로 입력한 값을 왼쪽의 변수에 저장(할당, asign) 한다.

변수는 어떤 값(정수, 실수, 문자, 문자열 등)을 저장할 수 있는 공간의 별명이라고 할 수 있다.
변수는 일반적으로 알파벳(a~z, A~Z)이나 언더라인 '_'으로 시작하는 단어를 사용하고, 숫자(0~9)로 시작하는 단어는 사용할 수 없다.
숫자로 시작하는 단어는 수로 인식하기 때문이다.
(python의 경우 한글 변수도 사용할 수 있지만, 영문을 사용하는 것이 예상하지 못하는 오류를 방지할 수 있다.)

'=' 연산자는 오른쪽의 계산 결과 값을 왼쪽의 변수에 저장하라는 의미의 대입연산자이다.
왼쪽의 결과값과 오른쪽의 결과값이 같다는 의미의 수학식의 등호와는 의미가 다르다. 
'''

print(int(input()))
