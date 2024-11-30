import pyttsx3
import time
import random
import keyboard  # キーボード入力を検出するためのライブラリ

# 音声読み上げ用の関数
def speak(text, rate=150):
    """
    音声読み上げ関数
    """
    engine = pyttsx3.init()  # pyttsx3の初期化
    engine.setProperty('rate', rate)  # 読み上げ速度を設定
    engine.say(text)  # 読み上げ開始
    engine.runAndWait()  # 読み上げが完了するまで待機

def start_auction(item_number, item_name, grade, weight, starting_price):
    """
    入札処理を行う関数
    """
    current_price = starting_price  # 初期金額
    auction_duration = 5  # 5秒間入札がなければ終了

    # 上場番号と品物情報の読み上げ
    print(f"\n=== 上場番号 {item_number} ===")
    print(f"品物「{item_name}」、ランク「{grade}」、重さ「{weight}kg」、初期金額: {current_price}円")
    speak(f"上場番号 {item_number}。品物「{item_name}」、ランク「{grade}」、重さは {weight}kg。初期金額は {current_price}円です。", rate=150)

    # 読み上げが完了した後にタイマーを開始
    last_bid_time = time.time()

    print("\nスペースキーを押して入札を行います。終了するには 'q' を入力してください。")

    while True:
        # 現在の時刻と最終入札時間を比較
        elapsed_time = time.time() - last_bid_time
        if elapsed_time >= auction_duration:
            print(f"\n5秒間入札がなかったため、上場番号 {item_number} の入札は終了しました。最終金額は {current_price}円です。")
            speak(f"5秒間入札がなかったため、上場番号 {item_number} の入札は終了しました。最終金額は {current_price}円です。", rate=150)
            break  # 入札終了

        # キー入力の監視
        if keyboard.is_pressed('q'):  # 'q'を押したら終了
            print(f"上場番号 {item_number} の入札を終了します。最終金額は {current_price}円です。")
            speak(f"上場番号 {item_number} の入札を終了します。最終金額は {current_price}円です。", rate=150)
            break  # 入札終了

        if keyboard.is_pressed('space'):  # スペースキーで入札
            # 入札があった場合は金額を上げる（ランダムに金額を増加）
            increase = random.randint(100, 500)  # 100円から500円の間で金額を上げる
            current_price += increase

            # 入札金額の読み上げ
            print(f"新しい金額: {current_price}円")
            speak(f"新しい金額は {current_price}円です。", rate=150)

            # 最後の入札時間を更新（読み上げ完了後）
            last_bid_time = time.time()

            # 連続反応を許可するためスリープなし

def main():
    """
    メイン処理
    """
    print("=== 自動入札システム ===")
    print("各品物に上場番号を自動割り振りします。\n")

    item_list = []  # 入札する品物リスト
    item_count = int(input("入札する品物の数を入力してください: "))

    # 各品物の情報を入力
    for i in range(1, item_count + 1):
        print(f"\n--- 上場番号 {i} の情報を入力してください ---")
        item_name = input("品物の名前を入力: ")
        grade = input("ランク（格付け）を入力: ")
        weight = input("重さ（kg）を入力: ")
        starting_price = input("初期金額を入力: ")

        try:
            weight = float(weight)  # 重さを浮動小数点数として変換
            starting_price = int(starting_price)  # 金額を整数として変換
        except ValueError:
            print("無効な金額または重さが入力されました。スキップします。")
            continue

        # 品物情報をリストに追加
        item_list.append((i, item_name, grade, weight, starting_price))

    # 入札を開始
    for item in item_list:
        item_number, item_name, grade, weight, starting_price = item
        start_auction(item_number, item_name, grade, weight, starting_price)

    print("\nすべての入札が終了しました。ご参加ありがとうございました！")
    speak("すべての入札が終了しました。ご参加ありがとうございました！", rate=150)

if __name__ == "__main__":
    main()




