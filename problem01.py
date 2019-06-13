s = '/usr/local/bin/python'

s1 = ','.join(s[1:].split('/'))
print(s1)

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.
s1 = ','.join(s.rsplit('/', 1))
print(s1)