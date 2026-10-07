import time
import requests
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

EVENTS = [
    {
        "type": "Nghiên cứu & Huấn luyện",
        "desc": "Nâng cấp kỹ thuật và huấn luyện lính T3/T4.",
        "rewards": "Rương Ngọc, Tăng tốc 24h, 6,000 Điểm VIP"
    },
    {
        "type": "Săn Quái & Săn Sách",
        "desc": "Dùng thể lực đánh quái cấp 2 trở lên.",
        "rewards": "Rương Quái Tinh Anh, Bình Thể Lực"
    }
]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    idx = 0
    while True:
        curr = EVENTS[idx]
        nxt = EVENTS[(idx + 1) % len(EVENTS)]
        msg = f"🔥 *LORDS MOBILE - SỰ KIỆN MỚI*\n\n🟢 *Đang diễn ra:* {curr['type']}\n• Môt tả: {curr['desc']}\n\n⏳ *Sắp tới:* {nxt['type']}"
        send_telegram_message(msg)

        idx = (idx + 1) % len(EVENTS)
        time.sleep(3300) # Đợi 55 phút