#p203
#re 모듈관련 함수 import
from re import findall,sub

#텍스트 전처리
texts = ['우리날 대한민국, 우리나라%$만세', '비아그&라 500gram 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생보장 마감 임박'
         '나는 홍길동']

# (1) 텍스트 전처리 함수
def crean_text(text):
    #1~6단계
    text_re = text.lower()
    text_re2 = sub('[1-9]','',text_re)
    texts_re3 = sub('[,.?!;:]',''text_re2)
    texts_re4 = sub('[@#$%^&*()]','', texts_re3)
    texts_re5 = sub('[a-z]','', texts_re4)
    texts_re6 = ''.join(texts_re5.split())
    return texts_re6

# (2) 함수 호출
texts_result = [clean_text(text) for text in texts]
print(texts_result)
#출력 결과
'''
['우리나라 대한민국 우리날 만세','비아그라 정력 최고','나는 대한민국 사람','보험료 원에 평생 보장 마감 임박','나는 홍길동']
'''