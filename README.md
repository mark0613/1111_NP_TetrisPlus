# 1111_NP_TetrisPlus

## Start
1. `git clone https://github.com/mark0613/1111_NP_TetrisPlus.git`
2. `cd 1111_NP_TetrisPlus/`
3. 建立虛擬環境
   - `python3 -m venv venv`
4. 進入虛擬環境(指令視作業系統而定)
   - Windows：`venv/Scripts/activate`
   - Linux/MacOS：`source ./venv/bin/activate`
5. `pip install -r requirements.txt`

### Server Side
1. 建立資料庫 `tetris_plus`
2. `cd server/`
3. 複製 `.env.example` 為 `.env`，並修改內容
4. `python3 main.py`

### Client Side
1. `cd client/`
2. `python3 main.py`
