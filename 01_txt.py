#한글파일 > 다른이름으로 저장 > TXT > UTF-8 로 저장
#txt파일 > 다른이름으로 저장 > UTF-8 로 저장
#txt파일을 .py과 같은 폴더로 이동

def showfile(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()
showfile('education.txt')