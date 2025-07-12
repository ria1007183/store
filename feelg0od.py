# 1. 폴더 만들기
mkdir seq2sound
cd seq2sound

# 2. 필요한 파일 생성 및 코드 붙여넣기
# (app.py, utils.py, sequence_to_midi.py 등)
# VSCode 열어서 붙여넣어도 됨
code .

# 3. 깃 초기화 및 GitHub에 연결
git init
git remote add origin https://github.com/사용자ID/저장소이름.git

# 4. 커밋하고 푸시
git add .
git commit -m "Initial commit"
git push -u origin main

# 가상환경 (선택)
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 실행
streamlit run app.py
