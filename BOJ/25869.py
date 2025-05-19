w, h, d = map(int, input().split())

window_w = w - (d * 2)
window_h = h - (d * 2)

window_w = window_w if window_w > 0 else 0
window_h = window_h if window_h > 0 else 0

print(window_w * window_h)